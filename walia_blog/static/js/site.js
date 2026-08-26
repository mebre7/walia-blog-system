document.addEventListener('DOMContentLoaded', function () {
  const revealTargets = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  revealTargets.forEach(function (target) {
    observer.observe(target);
  });

  // Theme toggle: dark/light mode
  const themeToggle = document.getElementById('themeToggle');
  const themeIcon = document.getElementById('themeIcon');
  const html = document.documentElement;

  // Initialize theme from localStorage or system preference
  if (themeToggle && themeIcon) {
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initialTheme = savedTheme || (prefersDark ? 'dark' : 'light');

    html.setAttribute('data-theme', initialTheme);
    themeIcon.textContent = initialTheme === 'dark' ? '🌙' : '☀️';
    console.log('Theme initialized to:', initialTheme);

    // Toggle theme on button click
    themeToggle.addEventListener('click', function (e) {
      e.preventDefault();
      const currentTheme = html.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      themeIcon.textContent = newTheme === 'dark' ? '🌙' : '☀️';
      console.log('Theme toggled to:', newTheme);
    });
  } else {
    console.warn('Theme toggle elements not found:', { themeToggle, themeIcon });
  }

  // Simpler alternative: Use this if above doesn't work
  function initThemeToggle() {
    const btn = document.getElementById('themeToggle');
    const icon = document.getElementById('themeIcon');
    const root = document.documentElement;

    if (!btn || !icon) return;

    // Get saved theme or detect system preference
    let theme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    root.setAttribute('data-theme', theme);
    icon.textContent = theme === 'dark' ? '🌙' : '☀️';

    // Click handler
    btn.addEventListener('click', function() {
      theme = theme === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', theme);
      localStorage.setItem('theme', theme);
      icon.textContent = theme === 'dark' ? '🌙' : '☀️';
    });
  }

  // Initialize immediately
  initThemeToggle();

  const radios = document.querySelectorAll('input[name="post_type"]');
  const label = document.querySelector('[data-selected-topic]');
  const hint = document.querySelector('[data-selected-topic-copy]');
  const tone = document.querySelector('[data-post-tone]');
  const format = document.querySelector('[data-post-format]');
  const summary = document.querySelector('[data-selection-summary]');

  function refreshSelection() {
    if (!radios.length || !tone || !format) return;

    const selected = document.querySelector('input[name="post_type"]:checked');
    if (!selected) return;

    const selectedTopic = selected.value;
    const toneValue = tone.value;
    const formatValue = format.value;

    if (label) label.textContent = selectedTopic;
    if (hint) hint.textContent = 'Craft it as a ' + toneValue.toLowerCase() + ' ' + formatValue.toLowerCase() + ' that fits ' + selectedTopic.toLowerCase() + '.';
    if (summary) summary.textContent = selectedTopic + ' · ' + toneValue + ' · ' + formatValue;

    document.querySelectorAll('.pill-radio').forEach(function (el) {
      const input = el.querySelector('input');
      el.classList.toggle('is-active', Boolean(input && input.checked));
    });
  }

  radios.forEach(function (radio) {
    radio.addEventListener('change', refreshSelection);
  });

  if (tone) tone.addEventListener('change', refreshSelection);
  if (format) format.addEventListener('change', refreshSelection);

  document.querySelectorAll('[data-bg]').forEach(function (card) {
    const backgroundImage = card.getAttribute('data-bg');
    if (backgroundImage) {
      card.style.backgroundImage = 'linear-gradient(180deg, rgba(5, 11, 21, 0.10), rgba(5, 11, 21, 0.84)), url("' + backgroundImage + '")';
    }
  });

  const latestReadsScroll = document.querySelector('[data-latest-scroll]');
  const scrollButtons = document.querySelectorAll('[data-scroll-down]');

  function scrollLatestReads() {
    if (!latestReadsScroll) return;
    const step = Math.max(220, Math.floor(latestReadsScroll.clientHeight * 0.8));
    latestReadsScroll.scrollBy({ top: step, behavior: 'smooth' });
  }

  scrollButtons.forEach(function (button) {
    button.addEventListener('click', scrollLatestReads);
  });

  if (latestReadsScroll) {
    latestReadsScroll.addEventListener('scroll', function () {
      const distanceToBottom = latestReadsScroll.scrollHeight - latestReadsScroll.scrollTop - latestReadsScroll.clientHeight;
      if (distanceToBottom < 120) {
        scrollLatestReads();
      }
    });
  }

  refreshSelection();

  // Initialize all custom dropdowns (open menu only on click)
  document.querySelectorAll('.custom-dropdown').forEach(function (root) {
    const btn = root.querySelector('.category-dropdown-btn');
    const menu = root.querySelector('.custom-dropdown-menu');
    const label = root.querySelector('.category-dropdown-label');
    const input = root.querySelector('.interest-input') || root.querySelector('input[type="hidden"][name="interest"]');
    if (!btn || !menu || !label || !input) return;

    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      const opened = menu.classList.toggle('show');
      btn.setAttribute('aria-expanded', opened ? 'true' : 'false');
    });

    menu.addEventListener('click', function (e) {
      const item = e.target.closest('.dropdown-item');
      if (!item) return;
      const id = item.getAttribute('data-id');
      const name = item.getAttribute('data-name') || item.textContent.trim();
      input.value = id || name;
      label.textContent = name;
      menu.classList.remove('show');
      btn.setAttribute('aria-expanded', 'false');
    });
  });

  // Close any open dropdown when clicking outside
  document.addEventListener('click', function (e) {
    document.querySelectorAll('.custom-dropdown').forEach(function (root) {
      if (!root.contains(e.target)) {
        const menu = root.querySelector('.custom-dropdown-menu');
        const btn = root.querySelector('.category-dropdown-btn');
        if (menu) menu.classList.remove('show');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      }
    });
  });
});
