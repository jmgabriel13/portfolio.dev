'use strict';

// Navigation remains visible without JavaScript.
const navToggle = document.querySelector('[data-nav-toggle]');
const siteNav = document.querySelector('[data-site-nav]');
const mobileViewport = window.matchMedia('(max-width: 760px)');

if (navToggle && siteNav) {
  const menuLabel = navToggle.querySelector('[data-menu-label]');
  let navigationHadFocus = false;
  const setMenuOpen = (isOpen, restoreFocus = false) => {
    siteNav.classList.toggle('is-open', isOpen);
    navToggle.setAttribute('aria-expanded', String(isOpen));
    if (menuLabel) menuLabel.textContent = isOpen ? 'Close' : 'Menu';
    if (restoreFocus) navToggle.focus();
  };
  navToggle.addEventListener('click', () =>
    setMenuOpen(navToggle.getAttribute('aria-expanded') !== 'true'),
  );
  siteNav.addEventListener('click', (event) => {
    const link = event.target.closest('a');
    if (!link || !mobileViewport.matches) return;
    setMenuOpen(false);
    const target = document.querySelector(link.getAttribute('href'));
    if (target) {
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
      target.addEventListener('blur', () => target.removeAttribute('tabindex'), { once: true });
    }
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && navToggle.getAttribute('aria-expanded') === 'true')
      setMenuOpen(false, true);
  });
  const closeWhenOutside = (event) => {
    if (!siteNav.contains(event.target) && !navToggle.contains(event.target)) setMenuOpen(false);
  };
  document.addEventListener('click', closeWhenOutside);
  document.addEventListener('focusin', (event) => {
    navigationHadFocus = siteNav.contains(event.target);
    closeWhenOutside(event);
  });
  document.addEventListener('pointerdown', (event) => {
    if (!siteNav.contains(event.target)) navigationHadFocus = false;
  });
  const syncNavigation = () => {
    const focusWillBeHidden =
      mobileViewport.matches && (navigationHadFocus || siteNav.contains(document.activeElement));
    const toggleHadFocus = document.activeElement === navToggle;
    navToggle.hidden = !mobileViewport.matches;
    setMenuOpen(false, focusWillBeHidden);
    if (!mobileViewport.matches && toggleHadFocus) siteNav.querySelector('a')?.focus();
  };
  document.documentElement.classList.add('nav-ready');
  syncNavigation();
  mobileViewport.addEventListener('change', syncNavigation);
}

// Content is never hidden while waiting for an animation or observer.
const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
if ('IntersectionObserver' in window && !motionPreference.matches) {
  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        if (!motionPreference.matches) entry.target.classList.add('is-entering');
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.1 },
  );
  document.querySelectorAll('[data-reveal]').forEach((element) => {
    revealObserver.observe(element);
    element.addEventListener('animationend', () => element.classList.remove('is-entering'), {
      once: true,
    });
  });
}
