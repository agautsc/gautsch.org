/* Game switcher for gautsch.org/games.
   One tag in each game page:  <script src="/games/switcher.js" defer></script>
   It adds a small tab on the left edge. The tab opens a shelf of every game.
   To add a game: add a row to GAMES and put its 800x1000 cover in /games/.
   The tab can be moved per game with `tab` (a CSS `top` value) if it covers something. */
(function () {
  'use strict';
  if (window.top !== window.self) return;          // not inside the Claude vs. Astra frames, or an embed
  if (!/^https?:$/.test(location.protocol)) return; // not in the offline copies
  if (window.__gameSwitcher) return;
  window.__gameSwitcher = true;

  var GAMES = [
    { path: '/bro/',            name: 'Bro!',             art: 'bro.webp',           color: '#3a5cff' },
    { path: '/math-jack/',      name: 'Math Jack',        art: 'math-jack.webp',     color: '#2f8a66' },
    { path: '/the-fly/',        name: 'The Fly',          art: 'the-fly.webp',       color: '#e3402f' },
    { path: '/the-fly-bosses/', name: 'The Fly: Bosses',  art: 'the-fly.webp',       color: '#6aa84f', badge: 'Bosses' },
    { path: '/turkey-escape/',  name: 'Turkey Escape',    art: 'turkey-escape.webp', color: '#c0552a' },
    { path: '/boom-square/',    name: 'Boom Square',      art: 'boom-square.webp',   color: '#e0623a' },
    { path: '/mosquito-keys/',  name: 'Mosquito Keys',    art: 'mosquito-keys.webp', color: '#e8836a' },
    { path: '/dog-hog-nyc/',    name: 'Dog Hog NYC',      art: 'dog-hog-nyc.webp',   color: '#f4b81c', tab: '27%' },
    { path: '/excite-dog/',     name: 'Excite Hog',       art: 'excite-hog.webp',    color: '#f4b81c', tab: '27%' }
  ];
  var BASE = '/games/';
  var here = location.pathname.replace(/index\.html$/, '');
  var current = null;
  GAMES.forEach(function (g) { if (here.indexOf(g.path) === 0) current = g; });

  var host = document.createElement('div');
  host.id = 'game-switcher';
  host.style.cssText = 'position:fixed;inset:0;z-index:2147483647;pointer-events:none;';
  var root = host.attachShadow({ mode: 'open' });

  var css = [
    ':host{all:initial}',
    '*{box-sizing:border-box}',
    '.tab{position:fixed;left:0;top:' + ((current && current.tab) || '50%') + ';transform:translateY(-50%);pointer-events:auto;',
    ' width:calc(30px + env(safe-area-inset-left,0px));height:64px;padding:0 0 0 env(safe-area-inset-left,0px);margin:0;border:0;',
    ' border-radius:0 14px 14px 0;background:#211e22;color:#f4b81c;cursor:pointer;opacity:.6;',
    ' box-shadow:0 0 0 2px rgb(255 255 255 / .55),0 4px 14px rgb(0 0 0 / .35);',
    ' display:grid;place-items:center;transition:opacity .15s,width .15s;-webkit-tap-highlight-color:transparent;touch-action:manipulation}',
    /* a wider, invisible touch target */
    '.tab::after{content:"";position:absolute;inset:-8px -14px -8px 0}',
    '.tab:hover,.tab:focus-visible{opacity:1;width:calc(38px + env(safe-area-inset-left,0px))}',
    '.tab:focus-visible{outline:3px solid #f4b81c;outline-offset:2px}',
    '.tab svg{width:22px;height:22px;display:block}',
    '.open .tab{display:none}',

    '.veil{position:fixed;inset:0;pointer-events:none;background:rgb(15 13 17 / 0);transition:background .2s;display:flex;align-items:stretch;justify-content:flex-start}',
    '.open .veil{pointer-events:auto;background:rgb(15 13 17 / .62)}',
    '.shelf{pointer-events:auto;width:min(430px,92vw);max-height:100%;display:flex;flex-direction:column;',
    ' background:#211e22;color:#f1ede6;font:16px/1.3 system-ui,-apple-system,"Segoe UI",sans-serif;',
    ' border-radius:0 22px 22px 0;box-shadow:8px 0 40px rgb(0 0 0 / .5);',
    ' transform:translateX(-105%);transition:transform .22s cubic-bezier(.2,.9,.3,1.1);visibility:hidden;',
    ' padding-left:env(safe-area-inset-left,0px)}',
    '.open .shelf{transform:none;visibility:visible}',
    '.top{display:flex;align-items:center;gap:10px;padding:16px 14px 10px 18px}',
    '.top h2{margin:0;flex:1;font:800 24px/1 system-ui,-apple-system,"Segoe UI",sans-serif;letter-spacing:-.01em}',
    '.stripe{display:flex;gap:4px;height:6px;margin:0 18px 12px}',
    '.stripe i{flex:1;border-radius:2px}',
    'button.x{width:44px;height:44px;border:0;border-radius:50%;background:rgb(241 237 230 / .12);color:inherit;font:700 22px/1 system-ui,sans-serif;cursor:pointer}',
    'button.x:hover{background:rgb(241 237 230 / .22)}',
    '.grid{list-style:none;margin:0;padding:4px 16px 16px;overflow-y:auto;overscroll-behavior:contain;display:grid;gap:14px 12px;grid-template-columns:repeat(3,minmax(0,1fr))}',
    '@media (max-width:360px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}',
    'a.game{display:block;color:inherit;text-decoration:none;border-radius:12px;position:relative;-webkit-tap-highlight-color:transparent}',
    '.cover{display:block;aspect-ratio:4/5;border-radius:10px;overflow:hidden;background:var(--c);box-shadow:0 0 0 2px rgb(241 237 230 / .16);transition:transform .15s}',
    '.cover img{display:block;width:100%;height:100%;object-fit:cover}',
    'a.game:hover .cover,a.game:focus-visible .cover{transform:rotate(-2deg) scale(1.04);box-shadow:0 0 0 3px #f4b81c}',
    'a.game:focus-visible,button:focus-visible{outline:3px solid #f4b81c;outline-offset:3px}',
    '.name{display:block;margin-top:6px;font-weight:700;font-size:14px;text-align:center;text-wrap:balance}',
    '.flag{position:absolute;top:6px;left:6px;padding:3px 7px;border-radius:999px;background:#f4b81c;color:#211e22;font-weight:800;font-size:11px;line-height:1.2}',
    '.flag.b{background:#211e22;color:#f1ede6;left:auto;right:6px}',
    'a.now .cover{box-shadow:0 0 0 3px #f4b81c}',
    '.foot{display:flex;gap:10px;align-items:center;padding:12px 16px calc(14px + env(safe-area-inset-bottom,0px));border-top:1px solid rgb(241 237 230 / .14)}',
    'button.lucky{flex:1;min-height:48px;border:0;border-radius:999px;background:#f4b81c;color:#211e22;font:800 17px/1 system-ui,-apple-system,"Segoe UI",sans-serif;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;gap:9px}',
    'button.lucky:hover{filter:brightness(1.07)}',
    'button.lucky svg{width:22px;height:22px}',
    '.spin svg{animation:roll .5s ease-in-out}',
    '@keyframes roll{to{transform:rotate(360deg)}}',
    'a.all{color:#f1ede6;font-size:14px;padding:12px 6px;white-space:nowrap}',
    '@media (prefers-reduced-motion:reduce){.shelf,.veil,.tab,.cover{transition:none}.spin svg{animation:none}}'
  ].join('\n');

  var PAD = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M12.5 5h7v7.5H27v7h-7.5V27h-7v-7.5H5v-7h7.5z" fill="currentColor"/><circle cx="16" cy="16" r="2.4" fill="#211e22"/></svg>';
  var DICE = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="4" fill="#211e22"/><g fill="#f4b81c"><circle cx="8" cy="8" r="1.7"/><circle cx="16" cy="8" r="1.7"/><circle cx="12" cy="12" r="1.7"/><circle cx="8" cy="16" r="1.7"/><circle cx="16" cy="16" r="1.7"/></g></svg>';

  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  var tiles = GAMES.map(function (g) {
    var now = g === current;
    return '<li><a class="game' + (now ? ' now' : '') + '" href="' + g.path + '" style="--c:' + g.color + '"' + (now ? ' aria-current="page"' : '') + '>' +
      '<span class="cover"><img data-src="' + BASE + g.art + '" alt="" width="800" height="1000"></span>' +
      (now ? '<span class="flag">Playing</span>' : '') +
      (g.badge ? '<span class="flag b">' + esc(g.badge) + '</span>' : '') +
      '<span class="name">' + esc(g.name) + '</span></a></li>';
  }).join('');

  root.innerHTML = '<style>' + css + '</style>' +
    '<div class="wrap">' +
    '<button class="tab" type="button" aria-label="Switch games" aria-expanded="false" title="Switch games">' + PAD + '</button>' +
    '<div class="veil"><div class="shelf" role="dialog" aria-modal="true" aria-label="Switch games">' +
    '<div class="top"><h2>Switch games</h2><button class="x" type="button" aria-label="Close">&times;</button></div>' +
    '<div class="stripe" aria-hidden="true"><i style="background:#3a5cff"></i><i style="background:#2f8a66"></i><i style="background:#e8836a"></i><i style="background:#f4b81c"></i></div>' +
    '<ul class="grid">' + tiles + '</ul>' +
    '<div class="foot"><button class="lucky" type="button">' + DICE + 'Surprise me</button><a class="all" href="' + BASE + '">All games</a></div>' +
    '</div></div></div>';

  var wrap = root.querySelector('.wrap');
  var tab = root.querySelector('.tab');
  var veil = root.querySelector('.veil');
  var shelf = root.querySelector('.shelf');
  var lucky = root.querySelector('.lucky');
  var isOpen = false;

  function open() {
    if (isOpen) return;
    isOpen = true;
    // Covers load the first time the shelf opens, so the games don't pay for them.
    Array.prototype.forEach.call(root.querySelectorAll('img[data-src]'), function (im) {
      im.src = im.getAttribute('data-src'); im.removeAttribute('data-src');
    });
    // Games that pause when the window loses focus will pause here too.
    try { window.dispatchEvent(new Event('blur')); } catch (e) {}
    wrap.classList.add('open');
    tab.setAttribute('aria-expanded', 'true');
    var first = root.querySelector('a.game:not(.now)') || root.querySelector('.x');
    setTimeout(function () { first.focus({ preventScroll: true }); }, 30);
  }
  function close() {
    if (!isOpen) return;
    isOpen = false;
    wrap.classList.remove('open');
    tab.setAttribute('aria-expanded', 'false');
    tab.blur();
  }

  tab.addEventListener('click', open);
  root.querySelector('.x').addEventListener('click', close);
  veil.addEventListener('click', function (e) { if (e.target === veil) close(); });
  lucky.addEventListener('click', function () {
    var others = GAMES.filter(function (g) { return g !== current; });
    var pick = others[Math.floor(Math.random() * others.length)];
    lucky.classList.add('spin');
    setTimeout(function () { location.href = pick.path; }, 380);
  });

  // Touches and clicks on the tab or the shelf never reach the game underneath.
  ['pointerdown', 'pointerup', 'pointermove', 'pointercancel', 'mousedown', 'mouseup', 'mousemove',
   'touchstart', 'touchend', 'touchmove', 'click', 'dblclick', 'contextmenu', 'wheel'].forEach(function (t) {
    host.addEventListener(t, function (e) { e.stopPropagation(); }, { passive: true });
  });

  // While the shelf is open the keyboard belongs to it, not to the game.
  function focusables() { return Array.prototype.slice.call(root.querySelectorAll('.x, a.game, .lucky, a.all')); }
  window.addEventListener('keydown', function (e) {
    if (!isOpen) return;
    e.stopImmediatePropagation();
    var k = e.key;
    if (k === 'Escape') { e.preventDefault(); close(); return; }
    var f = focusables(), i = f.indexOf(root.activeElement);
    var step = (k === 'ArrowRight' || k === 'ArrowDown') ? 1 : (k === 'ArrowLeft' || k === 'ArrowUp') ? -1 : 0;
    if (k === 'Tab') { step = e.shiftKey ? -1 : 1; }
    if (step) {
      e.preventDefault();
      f[(i + step + f.length) % f.length].focus();
    } else if (k === ' ' && root.activeElement && root.activeElement.tagName === 'A') {
      e.preventDefault(); root.activeElement.click();
    }
  }, true);
  ['keyup', 'keypress'].forEach(function (t) {
    window.addEventListener(t, function (e) { if (isOpen) e.stopImmediatePropagation(); }, true);
  });

  function mount() { document.body.appendChild(host); }
  if (document.body) mount(); else document.addEventListener('DOMContentLoaded', mount);
})();
