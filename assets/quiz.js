(function () {
  var root = document.getElementById('qz');
  if (!root) return;
  var Q = JSON.parse(document.getElementById('qz-data').textContent);
  var UI = JSON.parse(document.getElementById('qz-ui').textContent);
  var byId = {};
  Q.forEach(function (q) { byId[q.id] = q; });
  var KEY = 'st-quiz-wrong';
  function loadWrong() { try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; } }
  function saveWrong(a) { try { localStorage.setItem(KEY, JSON.stringify(a)); } catch (e) {} }
  var wrong = loadWrong();
  function markWrong(id, isWrong) {
    var i = wrong.indexOf(id);
    if (isWrong && i < 0) wrong.push(id);
    if (!isWrong && i >= 0) wrong.splice(i, 1);
    saveWrong(wrong);
    document.getElementById('qz-wn').textContent = wrong.length;
  }
  document.getElementById('qz-wn').textContent = wrong.length;
  var L = 'ABCD';

  function card(q, n, mode) {
    var el = document.createElement('article');
    el.className = 'qcard m-' + q.m;
    el.dataset.id = q.id;
    var opts = q.o.map(function (o, i) {
      return '<button type="button" class="qopt" data-i="' + i + '"><b>' + L[i] + '</b><span>' + o + '</span></button>';
    }).join('');
    if (mode === 'mock') opts += '<button type="button" class="qopt qopt-e" data-i="-1"><span>' + UI.e + '</span></button>';
    el.innerHTML = '<div class="qhead"><span class="qnum">' + n + '</span><span class="cw">W' + q.w + '</span></div>' +
      '<div class="qtext">' + q.q + '</div><div class="qopts">' + opts + '</div><div class="qexp" hidden></div>';
    return el;
  }
  function reveal(el, q, chosen) {
    el.classList.add('done');
    var bs = el.querySelectorAll('.qopt');
    for (var i = 0; i < bs.length; i++) {
      var k = +bs[i].dataset.i;
      bs[i].disabled = true;
      if (k === q.a) bs[i].classList.add('right');
      if (k === chosen && k !== q.a) bs[i].classList.add('bad');
    }
    var ok = chosen === q.a;
    var exp = el.querySelector('.qexp');
    exp.hidden = false;
    exp.innerHTML = '<b class="' + (ok ? 'ok' : 'no') + '">' + (chosen === -1 ? UI.skipped : ok ? UI.correct : UI.wrong) +
      '</b> ' + q.e + ' <a href="' + q.h + '">' + UI.check + ': ' + q.t + ' →</a>';
    return ok;
  }

  // ---------------- practice
  var filter = 'all', right = 0, done = 0;
  function renderPractice() {
    var box = document.getElementById('qz-practice');
    box.innerHTML = '';
    right = 0; done = 0; score();
    var n = 0;
    Q.forEach(function (q) {
      if (filter !== 'all' && String(q.w) !== filter) return;
      var el = card(q, ++n, 'practice');
      el.addEventListener('click', function (e) {
        var b = e.target.closest('.qopt');
        if (!b || el.classList.contains('done')) return;
        var ok = reveal(el, q, +b.dataset.i);
        done++; if (ok) right++;
        markWrong(q.id, !ok);
        score();
      });
      box.appendChild(el);
    });
  }
  function score() { document.getElementById('qz-score').textContent = done ? (UI_plain('score') + ' ' + right + ' / ' + done) : ''; }
  function UI_plain(k) { var d = document.createElement('div'); d.innerHTML = UI[k]; var m = document.documentElement.className.indexOf('mode-en') >= 0 ? '.l-en' : '.l-zh'; var x = d.querySelector(m); return x ? x.textContent : d.textContent; }
  root.querySelector('.qz-filter').addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    filter = b.dataset.w;
    var all = this.querySelectorAll('button');
    for (var i = 0; i < all.length; i++) all[i].setAttribute('aria-pressed', all[i] === b ? 'true' : 'false');
    renderPractice();
  });

  // ---------------- mock exam
  var timer = null, left = 3600, picks = [], answers = {};
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function pick32() {
    var byW = {};
    Q.forEach(function (q) { (byW[q.w] = byW[q.w] || []).push(q); });
    var out = [], rest = [];
    Object.keys(byW).forEach(function (w) { var s = shuffle(byW[w].slice()); out = out.concat(s.slice(0, 3)); rest = rest.concat(s.slice(3)); });
    out = out.concat(shuffle(rest).slice(0, Math.max(0, 32 - out.length)));
    return out.sort(function (a, b) { return a.w - b.w; });
  }
  function startMock() {
    picks = pick32(); answers = {}; left = 3600;
    document.getElementById('qz-mock-start').hidden = true;
    document.getElementById('qz-result').hidden = true;
    var m = document.getElementById('qz-mock'); m.hidden = false;
    var list = document.getElementById('qz-mock-list'); list.innerHTML = '';
    picks.forEach(function (q, i) {
      var el = card(q, i + 1, 'mock');
      el.addEventListener('click', function (e) {
        var b = e.target.closest('.qopt'); if (!b || el.classList.contains('done')) return;
        answers[q.id] = +b.dataset.i;
        var bs = el.querySelectorAll('.qopt');
        for (var k = 0; k < bs.length; k++) bs[k].classList.toggle('picked', bs[k] === b);
        prog();
      });
      list.appendChild(el);
    });
    prog(); tick();
    clearInterval(timer); timer = setInterval(tick, 1000);
    window.scrollTo(0, root.offsetTop - 70);
  }
  function prog() { document.getElementById('qz-prog').textContent = Object.keys(answers).length + ' / ' + picks.length; }
  function tick() {
    var t = document.getElementById('qz-timer');
    var mm = Math.floor(left / 60), ss = left % 60;
    t.textContent = (mm < 10 ? '0' : '') + mm + ':' + (ss < 10 ? '0' : '') + ss;
    t.classList.toggle('low', left < 300);
    if (left-- <= 0) submit();
  }
  function submit() {
    clearInterval(timer);
    var ok = 0, bad = 0, skip = 0;
    var els = document.querySelectorAll('#qz-mock-list .qcard');
    for (var i = 0; i < els.length; i++) {
      var q = byId[els[i].dataset.id];
      var a = answers.hasOwnProperty(q.id) ? answers[q.id] : -1;
      reveal(els[i], q, a);
      if (a === -1) skip++; else if (a === q.a) { ok++; markWrong(q.id, false); } else { bad++; markWrong(q.id, true); }
    }
    var r = document.getElementById('qz-result');
    r.hidden = false;
    r.innerHTML = '<div class="qz-res"><b>' + ok + ' / ' + picks.length + '</b><span>✔ ' + ok + '</span><span>✘ ' + bad + '</span><span>– ' + skip + '</span>' +
      '<button type="button" class="btn" id="qz-again">' + UI.retry + '</button></div>';
    document.getElementById('qz-again').onclick = startMock;
    document.getElementById('qz-submit').disabled = true;
    r.scrollIntoView({ behavior: 'smooth' });
  }
  document.getElementById('qz-start').onclick = function () { document.getElementById('qz-submit').disabled = false; startMock(); };
  document.getElementById('qz-submit').onclick = submit;

  // ---------------- wrong list
  function renderWrong() {
    var box = document.getElementById('qz-wrong'); box.innerHTML = '';
    if (!wrong.length) { box.innerHTML = '<p class="qz-empty">' + UI.none + '</p>'; return; }
    var clr = document.createElement('button'); clr.type = 'button'; clr.className = 'btn'; clr.innerHTML = UI.clear;
    clr.onclick = function () { wrong = []; saveWrong(wrong); document.getElementById('qz-wn').textContent = 0; renderWrong(); };
    box.appendChild(clr);
    wrong.slice().forEach(function (id, i) {
      var q = byId[id]; if (!q) return;
      var el = card(q, i + 1, 'practice');
      el.addEventListener('click', function (e) {
        var b = e.target.closest('.qopt'); if (!b || el.classList.contains('done')) return;
        markWrong(q.id, !reveal(el, q, +b.dataset.i));
      });
      box.appendChild(el);
    });
  }

  // ---------------- tabs
  root.querySelector('.qz-tabs').addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    var tabs = this.querySelectorAll('button');
    for (var i = 0; i < tabs.length; i++) tabs[i].setAttribute('aria-selected', tabs[i] === b ? 'true' : 'false');
    var ps = root.querySelectorAll('.qz-panel');
    for (var j = 0; j < ps.length; j++) ps[j].hidden = ps[j].dataset.panel !== b.dataset.tab;
    if (b.dataset.tab === 'wrong') renderWrong();
  });
  document.addEventListener('langchange', score);
  renderPractice();
})();
