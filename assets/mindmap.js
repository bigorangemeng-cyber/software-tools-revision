/* Interactive mind map: horizontal tree, collapsible, zoomable, bilingual.
   Markup: <div class="mm" data-src="ID" data-open="3" [data-tools]></div>
           <script type="application/json" id="ID">{...tree...}</script>
   Node: {en, zh, k: root|module|week|section|concept, m: module, h: href, c: [children]} */
(function () {
  var NS = 'http://www.w3.org/2000/svg';
  var ctx = document.createElement('canvas').getContext('2d');
  var FONT = getComputedStyle(document.body).fontFamily || 'sans-serif';
  var K = {
    root:    { s1: 17,   s2: 13,   w1: 750, w2: 500, h: 44, px: 18 },
    module:  { s1: 14.5, s2: 12.5, w1: 700, w2: 500, h: 34, px: 14 },
    week:    { s1: 13.5, s2: 12,   w1: 650, w2: 400, h: 30, px: 12 },
    section: { s1: 13,   s2: 11.5, w1: 600, w2: 400, h: 26, px: 10 },
    concept: { s1: 12.5, s2: 11.5, w1: 500, w2: 400, h: 22, px: 8 }
  };
  var HGAP = 54, VGAP = 7, PAD = 20;

  function mode() {
    var m = document.documentElement.className.match(/mode-(en|zh|both)/);
    return m ? m[1] : 'both';
  }
  function strip(t) { return t ? t.replace(/^(W\d+|\d+\.\d+)\s+/, '') : t; }
  function labels(n) {
    var L = labels0(n);
    if (L[1] && L[0] !== L[1]) L[1] = strip(L[1]);
    return L;
  }
  function labels0(n) {
    var md = mode();
    if (md === 'en') return [n.en, ''];
    if (md === 'zh') return [n.zh || n.en, (n.k === 'concept' || n.k === 'week') && n.zh !== n.en ? n.en : ''];
    return [n.en, n.zh && n.zh !== n.en ? n.zh : ''];
  }
  // in zh mode, concepts/weeks show "中文  English" (English term stays visible for the exam)
  function measure(txt, size, weight) { ctx.font = weight + ' ' + size + 'px ' + FONT; return ctx.measureText(txt).width; }
  function el(tag, attrs, parent) {
    var e = document.createElementNS(NS, tag);
    for (var a in attrs) e.setAttribute(a, attrs[a]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function count(n) { var c = 0; (n.c || []).forEach(function (k) { c += 1 + count(k); }); return c; }

  function MindMap(host) {
    this.host = host;
    this.tree = JSON.parse(document.getElementById(host.getAttribute('data-src')).textContent);
    this.scale = 1;
    var od = parseInt(host.getAttribute('data-open') || '9', 10);
    (function init(n, d) { n.o = d < od; (n.c || []).forEach(function (k) { init(k, d + 1); }); })(this.tree, 0);
    this.wrap = document.createElement('div');
    this.wrap.className = 'mm-canvas';
    host.appendChild(this.wrap);
    if (host.hasAttribute('data-tools')) this.tools();
    this.drag();
    this.render();
    var self = this;
    document.addEventListener('langchange', function () { self.render(); });
  }

  MindMap.prototype.tools = function () {
    var self = this, bar = document.createElement('div');
    bar.className = 'mm-tools';
    var defs = [
      ['mm-d1', '模块 Modules', function () { self.openTo(1); }],
      ['mm-d2', '各讲 Weeks', function () { self.openTo(2); }],
      ['mm-d3', '小节 Sections', function () { self.openTo(3); }],
      ['mm-d4', '全部 All', function () { self.openTo(9); }],
      ['mm-sep'],
      ['mm-zo', '−', function () { self.zoom(1 / 1.2); }],
      ['mm-zi', '+', function () { self.zoom(1.2); }],
      ['mm-zf', '⤢', function () { self.fit(); }]
    ];
    defs.forEach(function (d) {
      if (d[0] === 'mm-sep') { var s = document.createElement('span'); s.className = 'mm-sep'; bar.appendChild(s); return; }
      var b = document.createElement('button');
      b.type = 'button'; b.className = d[0]; b.textContent = d[1];
      b.addEventListener('click', d[2]);
      bar.appendChild(b);
    });
    this.host.insertBefore(bar, this.wrap);
  };
  MindMap.prototype.openTo = function (depth) {
    (function set(n, d) { n.o = d < depth; (n.c || []).forEach(function (k) { set(k, d + 1); }); })(this.tree, 0);
    this.render();
  };
  MindMap.prototype.zoom = function (f) {
    this.zoomed = true;
    this.scale = Math.max(0.35, Math.min(2.2, this.scale * f));
    this.apply();
  };
  MindMap.prototype.fit = function () {
    var w = this.wrap.clientWidth - 4;
    this.scale = Math.max(0.82, Math.min(1, w / this.W));
    this.apply();
  };
  MindMap.prototype.apply = function () {
    if (!this.svg) return;
    this.svg.setAttribute('width', Math.round(this.W * this.scale));
    this.svg.setAttribute('height', Math.round(this.H * this.scale));
  };
  MindMap.prototype.drag = function () {
    var w = this.wrap, sx, sy, sl, st, on = false, moved = false;
    w.addEventListener('pointerdown', function (e) {
      if (e.button !== 0 || e.target.closest('.mm-node')) return;
      on = true; moved = false; sx = e.clientX; sy = e.clientY; sl = w.scrollLeft; st = w.scrollTop;
      w.classList.add('grabbing');
    });
    window.addEventListener('pointermove', function (e) {
      if (!on) return;
      var dx = e.clientX - sx, dy = e.clientY - sy;
      if (Math.abs(dx) + Math.abs(dy) > 3) moved = true;
      w.scrollLeft = sl - dx; w.scrollTop = st - dy;
    });
    window.addEventListener('pointerup', function () { on = false; w.classList.remove('grabbing'); });
  };

  MindMap.prototype.render = function () {
    var self = this, root = this.tree, cols = [], y = PAD, prevParent = null;
    // measure
    (function m(n, d) {
      var st = K[n.k] || K.concept, L = labels(n);
      n.d = d; n.l1 = L[0]; n.l2 = L[1];
      n.w1 = measure(L[0], st.s1, st.w1);
      n.w2 = L[1] ? measure(L[1], st.s2, st.w2) + 8 : 0;
      n.w = n.w1 + n.w2 + st.px * 2 + (n.h && n.c && n.c.length ? 16 : 0);
      n.hh = st.h;
      cols[d] = Math.max(cols[d] || 0, n.w);
      if (n.o) (n.c || []).forEach(function (k) { k.p = n; m(k, d + 1); });
    })(root, 0);
    // y positions
    (function place(n) {
      var kids = n.o ? (n.c || []) : [];
      if (!kids.length) {
        if (prevParent && prevParent !== n.p) y += 6;
        prevParent = n.p;
        n.y = y + n.hh / 2; y += n.hh + VGAP;
      } else {
        kids.forEach(place);
        n.y = (kids[0].y + kids[kids.length - 1].y) / 2;
      }
    })(root);
    var xs = [PAD];
    for (var i = 1; i < cols.length; i++) xs[i] = xs[i - 1] + cols[i - 1] + HGAP;
    this.W = xs[cols.length - 1] + cols[cols.length - 1] + PAD + 30;
    this.H = y + PAD;

    var svg = el('svg', { viewBox: '0 0 ' + this.W + ' ' + this.H, class: 'mm-svg', role: 'img' });
    var gl = el('g', { class: 'mm-links' }, svg), gn = el('g', {}, svg);
    (function draw(n) {
      var st = K[n.k] || K.concept, x = xs[n.d], top = n.y - n.hh / 2;
      var g = el('g', { class: 'mm-node k-' + n.k + (n.m ? ' m-' + n.m : '') + (n.h ? ' has-link' : ''), transform: 'translate(' + x + ',' + top + ')', tabindex: '0' }, gn);
      el('rect', { width: n.w, height: n.hh, rx: n.k === 'concept' ? 6 : n.hh / 2 > 14 ? 12 : 8 }, g);
      var t = el('text', { x: st.px, y: n.hh / 2, 'dominant-baseline': 'central' }, g);
      var a = el('tspan', { class: 't1', 'font-size': st.s1, 'font-weight': st.w1 }, t);
      a.textContent = n.l1;
      if (n.l2) { var b = el('tspan', { class: 't2', dx: 8, 'font-size': st.s2, 'font-weight': st.w2 }, t); b.textContent = n.l2; }
      if (n.h && n.c && n.c.length) { var go = el('text', { class: 'mm-go', x: n.w - st.px - 6, y: n.hh / 2, 'dominant-baseline': 'central', 'font-size': 12 }, g); go.textContent = '↗'; }
      var tip = el('title', {}, g); tip.textContent = n.en + (n.zh && n.zh !== n.en ? ' · ' + n.zh : '');
      var kids = n.c || [];
      if (kids.length) {
        var cx = n.w + 9;
        var tg = el('g', { class: 'mm-toggle', transform: 'translate(' + cx + ',' + n.hh / 2 + ')' }, g);
        el('circle', { r: n.o ? 6 : 9 }, tg);
        var tt = el('text', { 'text-anchor': 'middle', 'dominant-baseline': 'central', 'font-size': n.o ? 10 : 9.5 }, tg);
        tt.textContent = n.o ? '−' : count(n);
      }
      g.addEventListener('click', function (e) {
        var link = e.target.closest('.mm-go');
        if (n.h && (!kids.length || link)) { location.href = n.h; return; }
        if (kids.length) { n.o = !n.o; self.render(); }
      });
      g.addEventListener('keydown', function (e) { if (e.key === 'Enter') g.dispatchEvent(new MouseEvent('click', { bubbles: true })); });
      if (n.o) kids.forEach(function (k) {
        var x1 = x + n.w + (kids.length ? 15 : 0), y1 = n.y, x2 = xs[k.d], y2 = k.y, mx = (x1 + x2) / 2;
        el('path', { d: 'M' + x1 + ',' + y1 + ' C' + mx + ',' + y1 + ' ' + mx + ',' + y2 + ' ' + x2 + ',' + y2, class: 'mm-link' + (k.m ? ' m-' + k.m : '') }, gl);
        draw(k);
      });
    })(root);
    this.wrap.innerHTML = '';
    this.wrap.appendChild(svg);
    this.svg = svg;
    if (this.host.classList.contains('mm-week') && !this.zoomed) this.fit(); else this.apply();
    if (!this.centered && this.wrap.scrollHeight > this.wrap.clientHeight) {
      this.centered = true;
      this.wrap.scrollTop = Math.max(0, root.y * this.scale - this.wrap.clientHeight / 2);
    }
  };

  var maps = document.querySelectorAll('.mm');
  for (var i = 0; i < maps.length; i++) new MindMap(maps[i]);
})();
