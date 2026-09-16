(() => {
  const box = document.querySelector('.rh-conversation');
  if (!box) return;
  const bar = document.querySelector('.rh-bottom-bar');
  if (!bar) return;
  const toggle = bar.querySelector('.rh-deeper-toggle');
  const close = box.querySelector('.rh-conversation-close');
  const drawer = document.createElement('dialog');
  drawer.id = 'rh-conversation-drawer';
  drawer.className = 'rh-conversation-drawer';
  drawer.setAttribute('aria-labelledby', 'rh-conversation-title');
  // Keep the inline panel and its anchor usable when dialogs are unavailable.
  if (typeof drawer.showModal === 'function') {
    box.before(drawer);
    drawer.append(box);
    toggle.hidden = false;
    close.hidden = false;
    bar.querySelector('.rh-conversation-fallback').hidden = true;
    toggle.addEventListener('click', () => {
      drawer.showModal();
      toggle.setAttribute('aria-expanded', 'true');
      document.documentElement.classList.add('rh-drawer-open');
      close.focus({preventScroll: true});
    });
    close.addEventListener('click', () => drawer.close());
    drawer.addEventListener('keydown', (event) => {
      if (event.key !== 'Tab') return;
      const controls = [...drawer.querySelectorAll('button, a[href], summary, textarea')]
        .filter(control => !control.disabled && control.tabIndex >= 0 && control.getClientRects().length);
      const first = controls[0];
      const last = controls[controls.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
    drawer.addEventListener('close', () => {
      toggle.setAttribute('aria-expanded', 'false');
      document.documentElement.classList.remove('rh-drawer-open');
      toggle.focus({preventScroll: true});
    });
    drawer.addEventListener('click', (event) => {
      const rect = drawer.getBoundingClientRect();
      if (event.target === drawer && (event.clientX < rect.left || event.clientX > rect.right ||
          event.clientY < rect.top || event.clientY > rect.bottom)) drawer.close();
    });
  }
  const previous = bar.querySelector('a[rel="prev"]');
  const next = bar.querySelector('a[rel="next"]');
  [previous, next].forEach((link, index) => {
    if (!link) return;
    link.setAttribute('aria-keyshortcuts', index === 0 ? 'ArrowLeft k' : 'ArrowRight j');
    link.title += index === 0 ? ' (← or K)' : ' (→ or J)';
  });
  document.addEventListener('keydown', (event) => {
    if (drawer.open || event.defaultPrevented || event.repeat || event.isComposing ||
        event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
    const target = event.target;
    if (target instanceof Element && (target.isContentEditable || target.closest(
      'input, textarea, select, button, summary, audio, video, [role="textbox"], [role="slider"], [role="combobox"], [role="listbox"], [role="menu"], [role="tablist"]'
    ))) return;
    if (!window.getSelection().isCollapsed) return;
    const link = event.key === 'ArrowLeft' || event.key === 'k' ? previous
      : event.key === 'ArrowRight' || event.key === 'j' ? next : null;
    if (!link) return;
    event.preventDefault();
    link.click();
  });
  const button = box.querySelector('.rh-conversation-copy');
  const prompt = box.querySelector('textarea');
  const status = box.querySelector('[role="status"]');
  const details = box.querySelector('details');
  const sizeBar = () => document.documentElement.style.setProperty('--rh-bottom-height', `${bar.getBoundingClientRect().height}px`);
  document.body.classList.add('rh-has-bottom-bar');
  if ('ResizeObserver' in window) new ResizeObserver(sizeBar).observe(bar);
  button.hidden = false;
  sizeBar();

  const progress = bar.querySelector('.rh-reading-progress');
  const rabbit = bar.querySelector('.rh-progress-rabbit');
  const article = document.querySelector('.rh-page');
  if (progress && rabbit && article) {
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let frame = 0;
    let percent = -1;
    let lastScrollY = window.scrollY;
    const updateProgress = () => {
      frame = 0;
      if (window.scrollY !== lastScrollY) {
        rabbit.style.setProperty('--rh-rabbit-facing', window.scrollY < lastScrollY ? '-1' : '1');
        lastScrollY = window.scrollY;
      }
      // The article is finished when its bottom clears the fixed footer.
      const rect = article.getBoundingClientRect();
      const start = rect.top + window.scrollY;
      const readingHeight = window.innerHeight - bar.getBoundingClientRect().height;
      const distance = Math.max(0, rect.height - readingHeight);
      const fraction = distance > 0
        ? Math.min(1, Math.max(0, (window.scrollY - start) / distance))
        : (rect.bottom <= readingHeight ? 1 : 0);
      const travel = Math.max(0, progress.clientWidth - rabbit.offsetWidth);
      // Scroll position drives every pose; no animation runs while reading still.
      const hops = Math.max(1, Math.round(travel / 85));
      const phase = (fraction * hops) % 1;
      const lift = Math.sin(phase * Math.PI);
      rabbit.style.setProperty('--rh-rabbit-x', `${fraction * travel}px`);
      rabbit.style.setProperty('--rh-rabbit-hop', `${motion.matches ? 0 : -26 * lift}px`);
      rabbit.style.setProperty('--rh-rabbit-tilt', `${motion.matches ? 0 : -9 * Math.sin(phase * 2 * Math.PI)}deg`);
      rabbit.style.setProperty('--rh-rabbit-kick', `${motion.matches ? 0 : 18 * lift}deg`);
      const nextPercent = Math.round(fraction * 100);
      if (nextPercent !== percent) {
        progress.setAttribute('aria-valuenow', String(nextPercent));
        percent = nextPercent;
      }
    };
    const scheduleProgress = () => {
      if (!frame) frame = requestAnimationFrame(updateProgress);
    };
    progress.hidden = false;
    window.addEventListener('scroll', scheduleProgress, {passive: true});
    window.addEventListener('resize', scheduleProgress);
    window.addEventListener('pageshow', scheduleProgress);
    motion.addEventListener('change', scheduleProgress);
    if ('ResizeObserver' in window) {
      const observer = new ResizeObserver(scheduleProgress);
      observer.observe(article);
      observer.observe(bar);
    }
    updateProgress();
  }
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(prompt.value);
      status.textContent = 'Copied. Paste it into your robot.';
    } catch {
      details.open = true;
      prompt.focus({preventScroll: true});
      prompt.select();
      details.scrollIntoView({block: 'center'});
      status.textContent = 'Select and copy the prompt below.';
    }
  });
})();
