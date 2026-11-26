(function () {
  var root = document.documentElement;
  function current() {
    var m = (root.className.match(/mode-(en|zh|both)/) || [])[1];
    return m || 'both';
  }
  function mark(m) {
    var bs = document.querySelectorAll('[data-mode]');
    for (var i = 0; i < bs.length; i++) bs[i].setAttribute('aria-pressed', bs[i].getAttribute('data-mode') === m ? 'true' : 'false');
  }
  function set(m) {
    root.classList.remove('mode-en', 'mode-zh', 'mode-both');
    root.classList.add('mode-' + m);
    try { localStorage.setItem('st-lang', m); } catch (e) {}
    mark(m);
    var ev;
    try { ev = new Event('langchange'); } catch (e) { ev = document.createEvent('Event'); ev.initEvent('langchange', true, true); }
    document.dispatchEvent(ev);
  }
  mark(current());
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('[data-mode]');
    if (b) set(b.getAttribute('data-mode'));
  });

  // filter for glossary / commands tables
  var q = document.getElementById('q');
  if (q) {
    var rows = Array.prototype.slice.call(document.querySelectorAll('table.filterable tbody tr'));
    var blocks = Array.prototype.slice.call(document.querySelectorAll('.cmdblock'));
    q.addEventListener('input', function () {
      var v = q.value.trim().toLowerCase();
      rows.forEach(function (r) { r.hidden = !!v && r.textContent.toLowerCase().indexOf(v) < 0; });
      blocks.forEach(function (b) { b.hidden = !!v && !b.querySelector('tbody tr:not([hidden])'); });
    });
  }

  // keep the current week visible in the sidebar
  var cur = document.querySelector('.sidebar [aria-current="page"]');
  if (cur && cur.scrollIntoView && window.innerWidth > 860) cur.scrollIntoView({ block: 'nearest' });
})();
