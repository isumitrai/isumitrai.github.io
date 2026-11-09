#!/usr/bin/env python3
"""
Master Page Generator for Sumit Rai Portfolio V2
Generates index.html, projects.html, about.html, resume.html, and playground.html.
Adheres strictly to the V2 redesign brief:
- Minimal, editorial, sophisticated aesthetic
- 2 font families (Bricolage Grotesque for headings, Inter for body/UI)
- Black, White/Warm Paper, Accent Orange color scheme
- Preserves Sumit Rai brand identity, real assets, verified experience
- Dedicated resume with working PDF download & print styles
- Dedicated about page with editorial storytelling
- Structured case study layouts with compact info blocks
- Interactive Command+K quick navigation palette
"""

import os

# Base HTML Header
def get_head(title="Sumit Rai — Senior Product Designer | AI Builder", active_page="index"):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="Sumit Rai — Senior Product Designer &amp; AI Builder with 7+ years of product design and 10+ years of overall design experience across SaaS, AI, EdTech, FinTech, and consumer platforms." />
  <meta name="author" content="Sumit Rai" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
"""

def get_nav(active_page):
    return f"""
<header class="nav-wrap" id="siteHeader">
  <div class="nav-pill">
    <div class="nav-logo-group">
      <a href="index.html" class="nav-logo" title="Sumit Rai — Homepage">
        <span class="sr-mark">SR</span>
        <span>Sumit Rai</span>
      </a>
    </div>

    <nav class="nav-tabs" aria-label="Main Navigation">
      <a href="projects.html" class="{'active' if active_page in ['projects'] else ''}">Work</a>
      <a href="about.html" class="{'active' if active_page == 'about' else ''}">About</a>
      <a href="resume.html" class="{'active' if active_page == 'resume' else ''}">Resume</a>
      <a href="playground.html" class="{'active' if active_page == 'playground' else ''}">Playground</a>
    </nav>

    <div class="nav-right-actions">
      <button class="nav-cmd-btn" id="cmdPaletteTrigger" aria-label="Quick search and jump (Cmd+K)">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
        <span>Search</span>
        <kbd>⌘K</kbd>
      </button>
    </div>
  </div>
</header>

<button class="theme-toggle-floating" id="themeToggle" aria-label="Toggle dark mode">
  <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
  <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
</button>
"""

footer_html = """
<footer>
  <div class="footer-inner">
    <div class="footer-status-pill">
      <span class="dot"></span>
      <span>Open to Freelance &amp; Product Collaborations</span>
    </div>

    <h2 class="footer-tagline">
      Let's build something together.
    </h2>

    <div class="footer-email-box">
      <div class="footer-email-pill">
        <a class="pill-left" href="mailto:sumitraiworks@gmail.com" title="Send email to Sumit Rai">
          <span class="email-text">sumitraiworks@gmail.com</span>
        </a>
        <button class="copy-btn" id="copyEmailBtn" title="Copy email address" aria-label="Copy email address">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          <span class="copy-toast">Copied!</span>
        </button>
      </div>
    </div>

    <div class="footer-bottom-row">
      <span>&copy; Sumit Rai &middot; Senior Product Designer &amp; AI Builder &middot; Delhi, India</span>
      <div class="flinks">
        <a href="https://www.linkedin.com/in/isumitrai/" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://x.com/isumitrai" target="_blank" rel="noopener">X</a>
        <a href="https://www.instagram.com/isumitrai/" target="_blank" rel="noopener">Instagram</a>
      </div>
    </div>
  </div>
</footer>

<!-- Command + K Navigation Modal -->
<div class="cmd-modal" id="cmdModal" role="dialog" aria-modal="true" aria-label="Quick Command Palette">
  <div class="cmd-box">
    <div class="cmd-header">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
      <input type="text" class="cmd-input" id="cmdInput" placeholder="Type a destination or action..." autocomplete="off" />
      <span class="cmd-esc">ESC</span>
    </div>
    <div class="cmd-list" id="cmdList">
      <a href="index.html" class="cmd-item">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          <span>Home</span>
        </span>
        <span class="cmd-shortcut">H</span>
      </a>
      <a href="projects.html" class="cmd-item">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
          <span>Selected Work (Projects)</span>
        </span>
        <span class="cmd-shortcut">W</span>
      </a>
      <a href="about.html" class="cmd-item">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 1 0-16 0"/></svg>
          <span>About Sumit</span>
        </span>
        <span class="cmd-shortcut">A</span>
      </a>
      <a href="resume.html" class="cmd-item">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
          <span>Resume &amp; Experience</span>
        </span>
        <span class="cmd-shortcut">R</span>
      </a>
      <a href="assets/Sumit_Rai_Resume.pdf" download class="cmd-item">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <span>Download Resume PDF</span>
        </span>
        <span class="cmd-shortcut">PDF</span>
      </a>
      <a href="playground.html" class="cmd-item">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m10 15 5-3-5-3v6Z"/></svg>
          <span>Playground &amp; UI Experiments</span>
        </span>
        <span class="cmd-shortcut">P</span>
      </a>
      <a href="mailto:sumitraiworks@gmail.com" class="cmd-item">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
          <span>Email Sumit (sumitraiworks@gmail.com)</span>
        </span>
        <span class="cmd-shortcut">@</span>
      </a>
      <div class="cmd-item" id="cmdToggleTheme">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/></svg>
          <span>Toggle Dark / Light Mode</span>
        </span>
        <span class="cmd-shortcut">T</span>
      </div>
    </div>
  </div>
</div>
"""

global_js = """
// ---- Global Theme, Header & Command Palette Management ----
(function(){
  // Dark/Light Mode
  const root = document.documentElement;
  const themeToggle = document.getElementById('themeToggle');
  const storedTheme = localStorage.getItem('sr_theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  if (storedTheme === 'dark') root.setAttribute('data-theme', 'dark');

  function toggleTheme(){
    const isDark = root.getAttribute('data-theme') === 'dark';
    const next = isDark ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    localStorage.setItem('sr_theme', next);
  }

  if (themeToggle) themeToggle.addEventListener('click', toggleTheme);

  // Scroll Header Auto-Hide
  const header = document.getElementById('siteHeader');
  let lastY = window.scrollY, ticking = false;
  window.addEventListener('scroll', function(){
    if (!ticking) {
      window.requestAnimationFrame(function(){
        const curY = window.scrollY;
        if (header && curY > 80 && curY > lastY) {
          header.classList.add('nav-hidden');
        } else if (header) {
          header.classList.remove('nav-hidden');
        }
        lastY = curY;
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });

  // Copy Email Clipboard
  const copyBtn = document.getElementById('copyEmailBtn');
  if (copyBtn) {
    copyBtn.addEventListener('click', function(e){
      e.preventDefault();
      navigator.clipboard.writeText('sumitraiworks@gmail.com').then(function(){
        copyBtn.classList.add('copied');
        setTimeout(function(){ copyBtn.classList.remove('copied'); }, 2000);
      });
    });
  }

  // Command + K Palette
  const cmdModal = document.getElementById('cmdModal');
  const cmdTrigger = document.getElementById('cmdPaletteTrigger');
  const cmdInput = document.getElementById('cmdInput');
  const cmdList = document.getElementById('cmdList');
  const cmdThemeBtn = document.getElementById('cmdToggleTheme');

  function openCmd(){
    if (!cmdModal) return;
    cmdModal.classList.add('active');
    if (cmdInput) {
      cmdInput.value = '';
      cmdInput.focus();
    }
    filterCmd('');
  }

  function closeCmd(){
    if (!cmdModal) return;
    cmdModal.classList.remove('active');
  }

  if (cmdTrigger) cmdTrigger.addEventListener('click', openCmd);
  if (cmdModal) {
    cmdModal.addEventListener('click', function(e){
      if (e.target === cmdModal) closeCmd();
    });
  }

  document.addEventListener('keydown', function(e){
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (cmdModal && cmdModal.classList.contains('active')) {
        closeCmd();
      } else {
        openCmd();
      }
    } else if (e.key === 'Escape' && cmdModal && cmdModal.classList.contains('active')) {
      closeCmd();
    }
  });

  if (cmdThemeBtn) {
    cmdThemeBtn.addEventListener('click', function(){
      toggleTheme();
      closeCmd();
    });
  }

  function filterCmd(q){
    if (!cmdList) return;
    const items = cmdList.querySelectorAll('.cmd-item');
    const query = q.trim().toLowerCase();
    items.forEach(function(item){
      const text = item.textContent.toLowerCase();
      item.style.display = (!query || text.includes(query)) ? 'flex' : 'none';
    });
  }

  if (cmdInput) {
    cmdInput.addEventListener('input', function(e){
      filterCmd(e.target.value);
    });
  }
})();
"""

# Projects Database with complete structured case studies
PROJECTS = [
    {
        "id": "edumanage",
        "title": "EduManage",
        "full_title": "EduManage — Smart Educational Management Dashboard",
        "category": "SaaS Product · CMS",
        "year": "2024 — 2026",
        "tagline": "A modern institution dashboard shaped around academic operations, content management, and day-to-day school workflows.",
        "image": "./assets/proj_edumanage.png",
        "role": "Senior Product Designer (Lead UI/UX, Information Architecture)",
        "focus_areas": "SaaS Dashboard · Multi-Tenant CMS · Academic Workflows · Design System",
        "timeline": "2024 — 2026",
        "in_short": "Streamlined fragmented school administrative workflows into an intuitive, high-clarity operational workspace.",
        "overview": "EduManage is an enterprise-grade institution management dashboard engineered to bring student records, curriculum administration, examination schedules, and faculty workflows into a cohesive, single-screen command centre. The product serves academic coordinators and school directors who require rapid operational overview without informational clutter.",
        "challenge": "Educational institutions traditionally rely on disconnected legacy tools, disparate spreadsheets, and fragmented notification channels. Coordinators struggled with slow data retrieval, disjointed approval cycles, and cognitive overload during peak examination and enrollment cycles.",
        "my_role": "As the Senior Product Designer, I directed end-to-end user research, information architecture, component design systems, and rapid clickable prototypes. I worked directly alongside school administrators, product management, and engineering teams from problem definition to live release.",
        "approach": "I mapped administrative user journeys to uncover recurring bottlenecks. Rather than reproducing paper forms digitally, I structured the interface around role-based modular cards, contextual status widgets, and high-density data tables optimized for quick scanning and keyboard navigation.",
        "solution": "Designed a unified multi-tenant dashboard incorporating automated attendance telemetry, course schedule visualization, multi-tiered permission management, and an actionable alert drawer that surfaces critical deadlines before they escalate.",
        "outcome": "Significantly reduced coordinator task completion times, minimized administrative data entry errors, and established a scalable design system now adopted across multiple sister educational portals.",
        "tags": ["SaaS", "Dashboard", "CMS", "EdTech"]
    },
    {
        "id": "quayo",
        "title": "Quayo Basket",
        "full_title": "Quayo Basket — Grocery App & Brand Identity System",
        "category": "Grocery App · Brand Identity",
        "year": "2024 — 2026",
        "tagline": "A grocery mobile app paired with a fresh retail brand identity system for a clearer, friendlier shopping experience.",
        "image": "./assets/proj_quayo.png",
        "role": "Lead Product Designer & Brand Strategist",
        "focus_areas": "Mobile UX/UI · Brand Identity · Grocery Checkout Flows · Micro-interactions",
        "timeline": "2024 — 2026",
        "in_short": "Crafted an inviting visual language and simplified multi-category grocery shopping to boost repeat orders.",
        "overview": "Quayo Basket combines an intuitive on-demand grocery shopping application with a comprehensive retail brand identity. The project aimed to deliver effortless fresh produce discovery, transparent pricing, and rapid checkout experiences for busy urban households.",
        "challenge": "Grocery consumers drop off when search yields overwhelming category trees, item quantities are confusing to adjust, or cart substitutions are poorly communicated. The client needed both an app that felt effortless and a memorable brand personality that stood out in a competitive market.",
        "my_role": "I led both product design and visual identity. This included user journey mapping, design of the mobile interface (iOS & Android), brand guidelines, packaging touchpoints, icon systems, and prototype user testing.",
        "approach": "I designed for one-handed thumb interaction, focusing heavily on quick quantity adjustments directly from search results and shelf views. I paired clean typography with warm orange and green accents that evoke freshness without overwhelming the product photography.",
        "solution": "Delivered an end-to-end mobile app featuring visual basket meters, smart past-order reordering in two taps, real-time inventory substitution preferences, and an optimized single-screen checkout flow.",
        "outcome": "The refreshed shopping experience lowered checkout abandonment rates, boosted repeat weekly cart creation, and established an authentic brand identity that resonated with customers across digital and physical packaging.",
        "tags": ["Mobile App", "UI/UX", "Branding", "E-Commerce"]
    },
    {
        "id": "musafir",
        "title": "Musafir",
        "full_title": "Musafir — Travel Marketplace Landing Page Redesign",
        "category": "Web Design · Marketplace",
        "year": "2024 — 2025",
        "tagline": "A travel marketplace landing page redesigned for stronger conversion paths, clear destination framing, and confident decision-making.",
        "image": "./assets/proj_musafir.png",
        "role": "Product & Visual Designer",
        "focus_areas": "Landing Page Architecture · Destination Discovery · Conversion Rate Optimization",
        "timeline": "2024 — 2025",
        "in_short": "Transformed an information-dense travel portal into an editorial, high-converting discovery destination.",
        "overview": "Musafir is a premier travel discovery and booking platform connecting travelers with curated journeys and vacation packages. The redesign focused on overhauling the public-facing web landing experience to elevate destination storytelling while maximizing booking search intent.",
        "challenge": "The previous landing page suffered from banner blindness, cluttered deal carousels, and vague search filters that caused prospective travelers to leave without exploring destinations or entering the search funnel.",
        "my_role": "I served as Product & Visual Designer, responsible for competitive UX benchmarking, wireframing, high-fidelity responsive UI design, visual art direction, and conversion funnels.",
        "approach": "I structured the homepage as an editorial travel magazine: large, inspiring destination imagery paired with concise package highlights, verified guest reviews, transparent pricing tags, and a prominent persistent search bar.",
        "solution": "Introduced a modern search module with interactive date-flexibility toggles, thematic collections ('Weekend Escapes', 'Cultural Expeditions'), social proof badges, and clear visual hierarchy guiding visitors smoothly toward booking queries.",
        "outcome": "The redesigned landing page achieved notable improvements in search initiation rates and dwell time, establishing a trustworthy first impression that reinforced Musafir's position as an aspirational travel provider.",
        "tags": ["Web Design", "Travel", "Marketplace", "Conversion"]
    },
    {
        "id": "community",
        "title": "Community",
        "full_title": "Community — Student Learning Hub & EdTech Platform",
        "category": "EdTech · Community Platform",
        "year": "2023 — 2025",
        "tagline": "A student learning hub designed to support academic growth through shared peer discussions, study resources, and platform-led engagement.",
        "image": "./assets/proj_community.png",
        "role": "Product Designer (FIITJEE / Edfora Ecosystem)",
        "focus_areas": "EdTech Platform Design · Peer Interaction Workflows · Resource Architecture",
        "timeline": "2023 — 2025",
        "in_short": "Designed approachable study circles, resource bookmarks, and peer engagement structures for active student participation.",
        "overview": "Community is an educational collaboration platform designed to empower students preparing for competitive academic milestones. It bridges solitary studying with peer motivation through question-and-answer channels, mentor-moderated study rooms, and curated subject repositories.",
        "challenge": "Students studying for high-stakes exams often experience isolation and hesitation when asking questions in large public forums. The objective was to cultivate a safe, distraction-free environment that incentivizes constructive knowledge sharing.",
        "my_role": "As Product Designer, I spearheaded user research interviews with students and educators, mapped community governance workflows, designed responsive desktop and tablet interfaces, and collaborated with frontend engineers on implementation.",
        "approach": "I broke down intimidating monolithic forums into topic-focused micro-communities. Emphasized clear thread hierarchy, verified solution badges from educators, and lightweight bookmarking so students could preserve revision notes effortlessly.",
        "solution": "Built a clean, minimal learning platform incorporating contextual markdown equation support, peer study circles, weekly revision leaderboards, and a distraction-free reader mode for academic materials.",
        "outcome": "Doubled daily active peer discussions, reduced average unanswered question duration, and created a positive digital study environment embraced by both educators and competitive learners.",
        "tags": ["EdTech", "Platform", "Community", "Collaboration"]
    }
]

# Client Brands List
BRANDS = [
    {"name": "MakeMyTrip", "img": "./assets/src/brands01.jpg"},
    {"name": "FIITJEE", "img": "./assets/src/brands02.jpg"},
    {"name": "JADE", "img": "./assets/src/brands03.jpg"},
    {"name": "Holy Basti", "img": "./assets/src/brands04.jpg"},
    {"name": "Modicare", "img": "./assets/src/brands05.jpg"},
    {"name": "ToHelp", "img": "./assets/src/brands06.jpg"},
    {"name": "Allied Digital", "img": "./assets/src/brands07.jpg"},
    {"name": "Mamily", "img": "./assets/src/brands08.jpg"},
    {"name": "Quant Legaltech", "img": "./assets/src/brands09.jpg"},
    {"name": "Navtech", "img": "./assets/src/brands10.jpg"},
    {"name": "BJP", "img": "./assets/src/brands11.jpg"},
    {"name": "Fantasy World", "img": "./assets/src/brands12.jpg"},
    {"name": "Young", "img": "./assets/src/brands13.jpg"},
    {"name": "Quayo Basket", "img": "./assets/src/brands14.jpg"},
    {"name": "Fluid", "img": "./assets/src/brands15.jpg"},
    {"name": "Maxima", "img": "./assets/src/brands16.jpg"},
    {"name": "Prans", "img": "./assets/src/brands17.jpg"},
    {"name": "Sonata", "img": "./assets/src/brands18.jpg"},
    {"name": "Gecko Bold", "img": "./assets/src/brands19.jpg"},
    {"name": "KidKidz", "img": "./assets/src/brands20.jpg"}
]

# -------------------------------------------------------------
# PAGE 1: INDEX.HTML (HOMEPAGE)
# -------------------------------------------------------------
def build_index():
    projects_cards_html = ""
    for p in PROJECTS:
        projects_cards_html += f"""
      <article class="proj-card" onclick="window.location.href='projects.html#{p['id']}'" role="button" tabindex="0" aria-label="View case study for {p['title']}">
        <div class="proj-image">
          <img src="{p['image']}" alt="{p['full_title']}" loading="lazy" />
        </div>
        <div class="proj-body">
          <div class="proj-meta">
            <span class="proj-category">{p['category']}</span>
            <span class="proj-year">{p['year']}</span>
          </div>
          <h3 class="proj-title">{p['title']}</h3>
          <p class="proj-desc">{p['tagline']}</p>
          <div class="proj-link-row">
            <span class="proj-view-link">View Case Study &rarr;</span>
            <div class="proj-tech-tags">
              <span class="proj-tag">{p['tags'][0]}</span>
              <span class="proj-tag">{p['tags'][1]}</span>
            </div>
          </div>
        </div>
      </article>
"""

    brands_html = ""
    for b in BRANDS:
        brands_html += f"""
        <div class="brand-cell" title="{b['name']}">
          <img src="{b['img']}" alt="{b['name']} logo" loading="lazy" />
        </div>
"""

    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <!-- SECTION 01 — HERO / INTRODUCTION -->
    <section class="hero">
      <div class="status-pill">
        <span class="dot"></span>
        <span>Senior Product Designer &middot; AI Builder</span>
      </div>

      <h1 class="hero-greeting">Hi, I'm Sumit Rai.</h1>
      <p class="hero-statement">I design products, build experiences and explore what's next.</p>
      <p class="hero-description">
        I'm a Senior Product Designer and AI Builder, exploring the intersection of design, technology and thoughtful product experiences.
      </p>

      <div class="cta-row">
        <a href="#work" class="btn btn-primary">View My Work &darr;</a>
        <a href="about.html" class="btn btn-secondary">More About Me &rarr;</a>
      </div>
    </section>

    <!-- SECTION 02 — WORK I'M PROUD OF -->
    <section class="home-work-section" id="work">
      <div class="section-header-row">
        <div class="section-title-wrap">
          <span class="eyebrow"><span class="dot"></span> Selected Projects</span>
          <h2>Work I'm Proud Of</h2>
          <p>Selected digital products shaped across SaaS, EdTech, mobile apps, and marketplace platforms.</p>
        </div>
        <a href="projects.html" class="section-header-link">See All My Work &rarr;</a>
      </div>

      <div class="proj-grid">
        {projects_cards_html}
      </div>

      <div class="see-all-wrap">
        <a href="projects.html" class="btn btn-secondary">See All My Work &rarr;</a>
      </div>
    </section>

    <!-- SECTION 03 — MY APPROACH -->
    <section class="approach-section">
      <div class="approach-quote-box">
        <span class="eyebrow"><span class="dot"></span> Design Philosophy</span>
        <h2>Good design starts with understanding.</h2>
        <p class="approach-lead">
          I explore the problem, question assumptions, connect ideas and turn them into experiences that make sense for people and businesses.
        </p>
      </div>

      <div class="approach-grid">
        <div class="approach-card">
          <span class="approach-num">01 / DISCOVER</span>
          <h3>Explore &amp; Understand</h3>
          <p>Dig into the core problem, understand business goals, and listen closely to user workflows before pushing pixels.</p>
        </div>
        <div class="approach-card">
          <span class="approach-num">02 / CONNECT</span>
          <h3>Question Assumptions</h3>
          <p>Connect complex system architecture with human interaction, validating hypotheses with rapid prototypes.</p>
        </div>
        <div class="approach-card">
          <span class="approach-num">03 / DELIVER</span>
          <h3>Ship with Purpose</h3>
          <p>Build scalable design systems, partner tightly with engineering, and iterate toward measurable business clarity.</p>
        </div>
      </div>
    </section>

    <!-- SECTION 04 — ABOUT PREVIEW -->
    <section class="about-preview-section">
      <div class="about-preview-grid">
        <div class="about-preview-content">
          <span class="eyebrow"><span class="dot"></span> Background &amp; Mindset</span>
          <h2>Designing thoughtful digital experiences since 2015.</h2>
          <p>
            I'm a designer and product thinker with 7+ years dedicated to digital product design since 2019, and 10+ years of overall design craft spanning branding, interfaces, and systems.
          </p>
          <p>
            My work spans SaaS, AI, EdTech, FinTech, HealthTech, and consumer platforms. Lately, I explore how AI and emerging technologies reshape human-computer interfaces, bridging design strategy with functional code.
          </p>
          <div style="margin-top:24px;">
            <a href="about.html" class="btn btn-secondary">More About Me &rarr;</a>
          </div>
        </div>

        <div class="about-stats-grid">
          <div class="stat-box">
            <span class="stat-number">7+</span>
            <span class="stat-label">Years in Product</span>
            <span class="stat-desc">Dedicated product design since 2019</span>
          </div>
          <div class="stat-box">
            <span class="stat-number">10+</span>
            <span class="stat-label">Years Total Craft</span>
            <span class="stat-desc">Visual, brand &amp; UI experience since 2015</span>
          </div>
          <div class="stat-box">
            <span class="stat-number">6+</span>
            <span class="stat-label">Industries Shipped</span>
            <span class="stat-desc">SaaS, EdTech, FinTech, HealthTech &amp; AI</span>
          </div>
          <div class="stat-box">
            <span class="stat-number">AI</span>
            <span class="stat-label">Emerging Tech</span>
            <span class="stat-desc">AI-native workflows &amp; interactive prototypes</span>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 05 — SELECTED EXPERIENCE / JOURNEY -->
    <section class="experience-section">
      <div class="section-header-row">
        <div class="section-title-wrap">
          <span class="eyebrow"><span class="dot"></span> Professional Journey</span>
          <h2>Selected Experience</h2>
          <p>Roles and founding product work across high-impact design studios and tech teams.</p>
        </div>
        <a href="resume.html" class="section-header-link">View Full Resume &rarr;</a>
      </div>

      <div class="timeline-list">
        <div class="timeline-item">
          <div class="timeline-company">
            <span class="comp-name">Raimage Design</span>
            <span class="comp-role">Founding Designer</span>
          </div>
          <div class="timeline-details">
            <p>Independent Design Studio. Leading end-to-end product design, brand systems, and AI-native interface explorations for high-growth ventures.</p>
          </div>
          <div class="timeline-period">2025 &mdash; Present</div>
        </div>

        <div class="timeline-item">
          <div class="timeline-company">
            <span class="comp-name">Edfora Infotech</span>
            <span class="comp-role">Senior Product Designer</span>
          </div>
          <div class="timeline-details">
            <p>EdTech / FIITJEE ecosystem. Directed product design for student learning hubs, institutional dashboards, and unified component design systems.</p>
          </div>
          <div class="timeline-period">2023 &mdash; 2025</div>
        </div>

        <div class="timeline-item">
          <div class="timeline-company">
            <span class="comp-name">Design Matra</span>
            <span class="comp-role">Product Designer</span>
          </div>
          <div class="timeline-details">
            <p>Owned UX/UI design across SaaS, FinTech, HealthTech, and E-Commerce products. Iterated core onboarding and checkout funnels.</p>
          </div>
          <div class="timeline-period">2021 &mdash; 2023</div>
        </div>

        <div class="timeline-item">
          <div class="timeline-company">
            <span class="comp-name">Kitaro Trading</span>
            <span class="comp-role">Graphic &amp; UI Designer</span>
          </div>
          <div class="timeline-details">
            <p>Designed brand identities, consumer interfaces, and established foundational design standards across multi-channel digital touchpoints.</p>
          </div>
          <div class="timeline-period">2015 &mdash; 2021</div>
        </div>
      </div>

      <!-- BRANDS WORKED WITH -->
      <div class="brands-wrap">
        <div class="section-header-row" style="margin-bottom:16px;">
          <div class="section-title-wrap">
            <span class="eyebrow"><span class="dot"></span> Client &amp; Brand Partners</span>
            <h3 style="font-size:1.3rem;">Brands I've Helped Shape</h3>
          </div>
        </div>
        <div class="brands-grid">
          {brands_html}
        </div>
      </div>

      <!-- TOOLS STACK -->
      <div class="tools-wrap">
        <div class="section-header-row" style="margin-bottom:16px;">
          <div class="section-title-wrap">
            <span class="eyebrow"><span class="dot"></span> Toolkit &amp; Environment</span>
            <h3 style="font-size:1.3rem;">Tools I Use to Think, Design &amp; Build</h3>
          </div>
        </div>
        <div class="tools-grid">
          <div class="tool-chip"><svg viewBox="0 0 38 57" fill="none"><path d="M19 28.5a9.5 9.5 0 1 1 19 0 9.5 9.5 0 0 1-19 0z" fill="#1ABCFE"/><path d="M0 47.5A9.5 9.5 0 0 1 9.5 38H19v9.5a9.5 9.5 0 0 1-19 0z" fill="#0ACF83"/><path d="M19 0v19h9.5a9.5 9.5 0 0 0 0-19H19z" fill="#FF7262"/><path d="M0 9.5A9.5 9.5 0 0 0 9.5 19H19V0H9.5A9.5 9.5 0 0 0 0 9.5z" fill="#F24E1E"/><path d="M0 28.5A9.5 9.5 0 0 0 9.5 38H19V19H9.5A9.5 9.5 0 0 0 0 28.5z" fill="#A259FF"/></svg><span>Figma</span></div>
          <div class="tool-chip"><svg viewBox="0 0 14 21" fill="currentColor"><path d="M0 0h14v7H7L0 0zm0 7h7l7 7H7v7L0 14V7z"/></svg><span>Framer</span></div>
          <div class="tool-chip"><svg viewBox="0 0 128 128" fill="#4353FF"><path d="M94.5 38.1c-6.9 0-13.1 3.4-16.9 8.7-2.4-5.5-7.9-9.4-14.3-9.4-5.2 0-9.8 2.4-12.9 6.2V38.7H33.5v50.6h17V66.7c0-5.2 4.2-9.4 9.4-9.4s9.4 4.2 9.4 9.4v22.6h17V66.7c0-5.2 4.2-9.4 9.4-9.4s9.4 4.2 9.4 9.4v22.6h17V63.5c0-14-11.3-25.4-25.2-25.4z"/></svg><span>Webflow</span></div>
          <div class="tool-chip"><svg viewBox="0 0 32 32" fill="none"><path d="M28.5 4.5l-8.5 8-8.5-8-7.5 4 8 8-8 8 7.5 4 8.5-8 8.5 8 3.5-2v-22z" fill="#0078D7"/></svg><span>VS Code</span></div>
          <div class="tool-chip"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 3l14 9-7 2-4 7L5 3z"/></svg><span>Cursor</span></div>
          <div class="tool-chip"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="12" cy="12" rx="10" ry="5" transform="rotate(-30 12 12)"/><ellipse cx="12" cy="12" rx="10" ry="5" transform="rotate(30 12 12)"/></svg><span>Spline 3D</span></div>
          <div class="tool-chip"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 20L12 4l8 16"/><path d="M7 14h10"/></svg><span>Midjourney</span></div>
          <div class="tool-chip"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.459 4.208c.746.606 1.026.56 2.428.466l13.215-.793c.28 0 .047-.28-.046-.326L17.86 1.968c-.42-.326-.981-.7-2.055-.607L3.01 2.295c-.466.046-.56.28-.374.466zm.793 3.08v13.904c0 .747.373 1.027 1.214.98l14.523-.84c.841-.046.935-.56.935-1.167V6.354c0-.606-.233-.933-.748-.887l-15.177.887c-.56.047-.747.327-.747.933zm14.337.745c.093.42 0 .84-.42.888l-.7.14v10.264c-.608.327-1.168.514-1.635.514-.748 0-.935-.234-1.495-.933l-4.577-7.186v6.952L12.21 19s0 .84-1.168.84l-3.222.186c-.093-.186 0-.653.327-.746l.84-.233V9.854L7.822 9.76c-.094-.42.14-1.026.793-1.073l3.456-.233 4.764 7.279v-6.44l-1.215-.14c-.093-.514.28-.887.747-.933zM1.936 1.035l13.31-.98c1.634-.14 2.055-.047 3.082.7l4.249 2.986c.7.513.934.653.934 1.213v16.378c0 1.026-.373 1.634-1.68 1.726l-15.458.934c-.98.047-1.448-.093-1.962-.747l-3.129-4.06c-.56-.747-.793-1.306-.793-1.96V2.667c0-.839.374-1.54 1.447-1.632z"/></svg><span>Notion</span></div>
          <div class="tool-chip"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg><span>GitHub</span></div>
          <div class="tool-chip"><svg viewBox="0 0 24 24" fill="#FF9A00"><path d="M7.045 0h9.91C20.4 0 24 3.6 24 8.045v7.91C24 20.4 20.4 24 15.955 24h-9.91C2.1 24 0 21.9 0 15.955v-7.91C0 3.6 2.1 0 7.045 0zm5.098 6.02L9.58 13.33h1.72l.566-1.602h2.812l.565 1.602H17L14.427 6.02H12.14zm1.286 2.14l.955 2.726h-1.91l.955-2.726zm-7.44-.957c.467 0 .814.135 1.04.404.227.27.34.664.34 1.183 0 .533-.126.95-.378 1.25-.252.3-.617.45-1.092.45H5.25V7.2h.74zm-.123 2.4c.28 0 .49-.09.628-.272.138-.18.207-.454.207-.822 0-.335-.06-.582-.18-.74-.12-.16-.31-.24-.564-.24h-.308v2.074h.217z"/></svg><span>Illustrator</span></div>
          <div class="tool-chip"><svg viewBox="0 0 24 24" fill="#31A8FF"><path d="M7.045 0h9.91C20.4 0 24 3.6 24 8.045v7.91C24 20.4 20.4 24 15.955 24h-9.91C2.1 24 0 21.9 0 15.955v-7.91C0 3.6 2.1 0 7.045 0zm2.49 6.14H7.44V17.1H9.1v-4.185c.185.015.45.022.797.022.836 0 1.49-.22 1.963-.664.473-.445.71-1.063.71-1.856 0-.763-.22-1.358-.664-1.783-.44-.425-1.11-.64-2.01-.64-.6 0-1.13.05-1.362.106zm.09 1.41c.122-.023.31-.034.564-.034.79 0 1.185.382 1.185 1.148 0 .822-.42 1.233-1.258 1.233-.232 0-.41-.01-.49-.034V7.55zm6.9-1.53c-.834 0-1.514.283-2.044.848-.528.565-.793 1.304-.793 2.217 0 .85.257 1.54.77 2.065.514.525 1.196.788 2.047.788.854 0 1.546-.27 2.076-.81.53-.54.795-1.25.795-2.13 0-.884-.267-1.594-.8-2.13-.533-.536-1.22-.847-2.05-.847zm.02 1.384c.43 0 .756.166.977.498.22.33.33.805.33 1.422 0 .618-.112 1.086-.336 1.406-.224.32-.55.48-.977.48-.42 0-.742-.162-.965-.487-.223-.325-.334-.8-.334-1.422 0-.616.11-1.087.332-1.41.222-.325.543-.487.972-.487z"/></svg><span>Photoshop</span></div>
          <div class="tool-chip"><svg viewBox="0 0 24 24" fill="#0052CC"><path d="M11.571 11.513H0a5.218 5.218 0 0 0 5.232 5.215h2.13v2.057A5.215 5.215 0 0 0 12.575 24V12.518a1.005 1.005 0 0 0-1.004-1.005zm5.723-5.756H5.757a5.215 5.215 0 0 0 5.215 5.214h2.129v2.058a5.218 5.218 0 0 0 5.215 5.214V6.762a1.005 1.005 0 0 0-1.022-1.005zM23.013 0H11.455a5.215 5.215 0 0 0 5.215 5.215h2.129v2.057A5.215 5.215 0 0 0 24.019 12.49V1.005A1.005 1.005 0 0 0 23.013 0z"/></svg><span>Jira</span></div>
        </div>
      </div>
    </section>

    <!-- SECTION 06 — CONTACT CTA -->
    <section class="contact-cta-section">
      <span class="eyebrow"><span class="dot"></span> Contact</span>
      <h2>Have something interesting in mind?</h2>
      <p>I'm always open to meaningful conversations, interesting ideas and opportunities to build something thoughtful.</p>
      <div class="cta-btns">
        <a href="mailto:sumitraiworks@gmail.com?subject=Hello%20Sumit" class="btn btn-primary">Get in Touch &rarr;</a>
        <a href="mailto:sumitraiworks@gmail.com" class="btn btn-secondary">Email Me</a>
      </div>
    </section>

  </div>
</main>
"""
    return get_head("Sumit Rai — Senior Product Designer | AI Builder", "index") + get_nav("index") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"

# -------------------------------------------------------------
# PAGE 2: PROJECTS.HTML (WORK ARCHIVE & INTERACTIVE CASE STUDIES)
# -------------------------------------------------------------
def build_projects():
    import json
    projects_json = json.dumps(PROJECTS)

    initial_projects_html = ""
    for p in PROJECTS:
        initial_projects_html += f"""
      <article class="proj-card" onclick="openCaseStudy('{p['id']}')" role="button" tabindex="0" aria-label="Open case study for {p['title']}">
        <div class="proj-image">
          <img src="{p['image']}" alt="{p['full_title']}" loading="lazy" />
        </div>
        <div class="proj-body">
          <div class="proj-meta">
            <span class="proj-category">{p['category']}</span>
            <span class="proj-year">{p['year']}</span>
          </div>
          <h3 class="proj-title">{p['title']}</h3>
          <p class="proj-desc">{p['tagline']}</p>
          <div class="proj-link-row">
            <span class="proj-view-link">View Case Study &rarr;</span>
            <div class="proj-tech-tags">
              <span class="proj-tag">{p['tags'][0]}</span>
              <span class="proj-tag">{p['tags'][1]}</span>
            </div>
          </div>
        </div>
      </article>
"""

    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <!-- LIST VIEW -->
    <div id="projectsListView">
      <div class="section-header-row" style="margin-top:24px; margin-bottom:32px;">
        <div class="section-title-wrap">
          <span class="eyebrow"><span class="dot"></span> Selected Works</span>
          <h1 style="font-size:clamp(2rem, 3.6vw, 2.8rem); margin-bottom:8px;">A glimpse into the products, systems, and experiences I've helped shape.</h1>
          <p>End-to-end design across SaaS, EdTech, mobile apps, and marketplace platforms.</p>
        </div>
      </div>

      <!-- Category Filter Tabs -->
      <div class="filter-tabs" id="projectFilterTabs" role="tablist">
        <button class="filter-btn active" data-filter="all">All Projects (4)</button>
        <button class="filter-btn" data-filter="saas">SaaS &amp; CMS</button>
        <button class="filter-btn" data-filter="mobile">Mobile App</button>
        <button class="filter-btn" data-filter="web">Web &amp; Marketplace</button>
        <button class="filter-btn" data-filter="edtech">EdTech</button>
      </div>

      <div class="proj-grid" id="projectsArchiveGrid">
        {initial_projects_html}
      </div>
    </div>

    <!-- SINGLE CASE STUDY VIEW -->
    <div id="caseStudyView" class="case-view" hidden>
      <div class="case-top-actions">
        <button class="case-pill-btn" id="backToProjectsBtn">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          <span>Back to All Projects</span>
        </button>
        <span class="tag-chip" id="caseCategoryChip">SaaS Product</span>
      </div>

      <div id="caseStudyContent">
        <!-- Rendered dynamically -->
      </div>
    </div>

  </div>
</main>
"""

    projects_page_js = f"""
  const allProjects = {projects_json};

  const archiveGrid = document.getElementById('projectsArchiveGrid');
  const filterTabs = document.getElementById('projectFilterTabs');
  const listView = document.getElementById('projectsListView');
  const caseView = document.getElementById('caseStudyView');
  const caseContent = document.getElementById('caseStudyContent');
  const backBtn = document.getElementById('backToProjectsBtn');
  const categoryChip = document.getElementById('caseCategoryChip');

  function renderProjects(filter = 'all') {{
    if (!archiveGrid) return;
    archiveGrid.innerHTML = '';
    const filtered = allProjects.filter(p => {{
      if (filter === 'all') return true;
      if (filter === 'saas') return p.tags.includes('SaaS') || p.tags.includes('CMS');
      if (filter === 'mobile') return p.tags.includes('Mobile App');
      if (filter === 'web') return p.tags.includes('Web Design') || p.tags.includes('Marketplace');
      if (filter === 'edtech') return p.tags.includes('EdTech');
      return true;
    }});

    filtered.forEach(p => {{
      const card = document.createElement('article');
      card.className = 'proj-card';
      card.setAttribute('role', 'button');
      card.setAttribute('tabindex', '0');
      card.setAttribute('aria-label', 'Open case study for ' + p.title);
      card.innerHTML = `
        <div class="proj-image">
          <img src="${{p.image}}" alt="${{p.full_title}}" loading="lazy" />
        </div>
        <div class="proj-body">
          <div class="proj-meta">
            <span class="proj-category">${{p.category}}</span>
            <span class="proj-year">${{p.year}}</span>
          </div>
          <h3 class="proj-title">${{p.title}}</h3>
          <p class="proj-desc">${{p.tagline}}</p>
          <div class="proj-link-row">
            <span class="proj-view-link">View Case Study &rarr;</span>
            <div class="proj-tech-tags">
              <span class="proj-tag">${{p.tags[0]}}</span>
              <span class="proj-tag">${{p.tags[1]}}</span>
            </div>
          </div>
        </div>
      `;
      card.addEventListener('click', () => openCaseStudy(p.id));
      card.addEventListener('keydown', (e) => {{ if (e.key === 'Enter') openCaseStudy(p.id); }});
      archiveGrid.appendChild(card);
    }});
  }}

  if (filterTabs) {{
    filterTabs.addEventListener('click', (e) => {{
      const btn = e.target.closest('.filter-btn');
      if (!btn) return;
      filterTabs.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderProjects(btn.dataset.filter);
    }});
  }}

  function openCaseStudy(projId) {{
    const project = allProjects.find(p => p.id === projId);
    if (!project) return;

    const idx = allProjects.findIndex(p => p.id === projId);
    const prev = allProjects[(idx - 1 + allProjects.length) % allProjects.length];
    const next = allProjects[(idx + 1) % allProjects.length];

    if (categoryChip) categoryChip.textContent = project.category;

    caseContent.innerHTML = `
      <!-- COMPACT INFO BLOCK -->
      <div class="case-meta-card">
        <div class="case-title-row">
          <span class="eyebrow"><span class="dot"></span> Case Study</span>
          <h1>${{project.full_title}}</h1>
        </div>
        <p class="case-tagline">${{project.tagline}}</p>
        
        <div class="case-meta-grid">
          <div class="case-meta-item">
            <div class="label">My Role</div>
            <div class="val">${{project.role}}</div>
          </div>
          <div class="case-meta-item">
            <div class="label">Focus Areas</div>
            <div class="val">${{project.focus_areas}}</div>
          </div>
          <div class="case-meta-item">
            <div class="label">Timeline</div>
            <div class="val">${{project.timeline}}</div>
          </div>
          <div class="case-meta-item">
            <div class="label">In Short</div>
            <div class="val">${{project.in_short}}</div>
          </div>
        </div>
      </div>

      <!-- HERO IMAGE PREVIEW -->
      <div class="case-hero-image">
        <img src="${{project.image}}" alt="${{project.full_title}} hero preview" />
      </div>

      <!-- STRUCTURED CASE STUDY SECTIONS -->
      <div class="case-body-flow">
        
        <div class="case-section-box">
          <h3><span class="sec-dot"></span> 01 &mdash; Project Overview</h3>
          <p>${{project.overview}}</p>
        </div>

        <div class="case-section-box">
          <h3><span class="sec-dot"></span> 02 &mdash; The Challenge</h3>
          <p>${{project.challenge}}</p>
        </div>

        <div class="case-section-box">
          <h3><span class="sec-dot"></span> 03 &mdash; My Role &amp; Responsibilities</h3>
          <p>${{project.my_role}}</p>
        </div>

        <div class="case-section-box">
          <h3><span class="sec-dot"></span> 04 &mdash; My Approach &amp; Process</h3>
          <p>${{project.approach}}</p>
        </div>

        <div class="case-section-box">
          <h3><span class="sec-dot"></span> 05 &mdash; The Solution</h3>
          <p>${{project.solution}}</p>
        </div>

        <div class="case-section-box">
          <h3><span class="sec-dot"></span> 06 &mdash; Outcome &amp; Impact</h3>
          <p>${{project.outcome}}</p>
        </div>

        <div class="case-section-box" style="background:var(--surface-subtle); border-color:rgba(224,99,30,0.25);">
          <h3><span class="sec-dot"></span> 07 &mdash; In Short</h3>
          <p style="font-weight:600; color:var(--ink);">${{project.in_short}}</p>
        </div>

      </div>

      <!-- PREV / NEXT NAVIGATION -->
      <div class="case-nav">
        <button class="case-nav-btn prev" id="prevCaseBtn">
          <span class="nav-eyebrow">&larr; Previous Case Study</span>
          <span class="nav-proj-name">${{prev.title}}</span>
        </button>
        <button class="case-nav-btn next" id="nextCaseBtn">
          <span class="nav-eyebrow">Next Case Study &rarr;</span>
          <span class="nav-proj-name">${{next.title}}</span>
        </button>
      </div>
    `;

    document.getElementById('prevCaseBtn').addEventListener('click', () => openCaseStudy(prev.id));
    document.getElementById('nextCaseBtn').addEventListener('click', () => openCaseStudy(next.id));

    listView.hidden = true;
    caseView.hidden = false;
    window.location.hash = project.id;
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }}

  function closeCaseStudy() {{
    caseView.hidden = true;
    listView.hidden = false;
    history.pushState("", document.title, window.location.pathname);
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }}

  if (backBtn) backBtn.addEventListener('click', closeCaseStudy);

  // Check URL hash on page load
  window.addEventListener('DOMContentLoaded', () => {{
    renderProjects('all');
    const hash = window.location.hash.replace('#', '');
    if (hash && allProjects.some(p => p.id === hash)) {{
      openCaseStudy(hash);
    }}
  }});
"""

    return get_head("Work & Case Studies — Sumit Rai", "projects") + get_nav("projects") + content + footer_html + f"<script>\n{global_js}\n{projects_page_js}\n</script>\n</body>\n</html>"

# -------------------------------------------------------------
# PAGE 3: ABOUT.HTML (EDITORIAL STORYTELLING)
# -------------------------------------------------------------
def build_about():
    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <!-- 01 — INTRODUCTION -->
    <section class="about-hero-grid">
      <div class="about-hero-copy">
        <span class="eyebrow"><span class="dot"></span> Senior Product Designer &middot; AI Builder</span>
        <h1>Hi, I'm Sumit Rai.</h1>
        <p class="lead">
          I'm a product designer, creative thinker and builder interested in how design and technology shape the things we experience every day.
        </p>
        <p>
          Over the past decade, I've journeyed from crafting brand identities and marketing collateral to architecting complex enterprise SaaS, EdTech ecosystems, and AI-native products. I believe the best products balance strategic clarity with rigorous visual craftsmanship.
        </p>
        <div style="display:flex; gap:12px; margin-top:28px; flex-wrap:wrap;">
          <a href="resume.html" class="btn btn-primary">Read My Resume &rarr;</a>
          <a href="mailto:sumitraiworks@gmail.com" class="btn btn-secondary">Email Me</a>
        </div>
      </div>

      <div class="about-avatar-card">
        <img src="./assets/avatar.jpg" alt="Sumit Rai portrait" />
      </div>
    </section>

    <!-- 02 — MY DESIGN JOURNEY -->
    <section class="about-editorial-block">
      <span class="eyebrow"><span class="dot"></span> Chapter 01</span>
      <h2>My Design Journey</h2>
      <p>
        My journey into design began in 2015 at Kitaro Trading, where I immersed myself in the fundamentals of visual hierarchy, brand consistency, and graphic design across diverse physical and digital consumer touchpoints. Working across real-world commercial constraints taught me that design is never purely aesthetic &mdash; it must communicate clearly and drive action.
      </p>
      <p>
        In 2019, my focus shifted decisively toward digital product design. At Design Matra, I took ownership of complex user journeys across FinTech, HealthTech, and E-Commerce products, tackling onboarding friction, checkout drop-offs, and multi-platform consistency.
      </p>
      <p>
        Later, as Senior Product Designer at Edfora Infotech, I led end-to-end design across web and mobile platforms for FIITJEE educational products, designing student learning hubs, institutional dashboards, and component design systems that unified multi-disciplinary engineering and academic teams.
      </p>
      <p>
        Today, at Raimage Design, I work as an independent founding designer partnering directly with founders and product teams. I frequently build high-fidelity interactive prototypes in code, exploring AI-native interfaces that make complex data actionable and effortless.
      </p>
    </section>

    <!-- 03 — EXPERIENCE CHRONOLOGY -->
    <section class="about-editorial-block">
      <span class="eyebrow"><span class="dot"></span> Chapter 02</span>
      <h2>Professional Experience</h2>
      <div class="timeline-list" style="margin-top:20px;">
        <div class="timeline-item">
          <div class="timeline-company">
            <span class="comp-name">Raimage Design</span>
            <span class="comp-role">Founding Designer</span>
          </div>
          <div class="timeline-details">
            <p>Directing zero-to-one product design, brand identity systems, and AI-native interface explorations for early-stage and growth tech ventures.</p>
          </div>
          <div class="timeline-period">2025 &mdash; Present</div>
        </div>

        <div class="timeline-item">
          <div class="timeline-company">
            <span class="comp-name">Edfora Infotech</span>
            <span class="comp-role">Senior Product Designer</span>
          </div>
          <div class="timeline-details">
            <p>Led end-to-end UX/UI design across student portals, administrator dashboards, and cross-platform design systems in the FIITJEE ecosystem.</p>
          </div>
          <div class="timeline-period">2023 &mdash; 2025</div>
        </div>

        <div class="timeline-item">
          <div class="timeline-company">
            <span class="comp-name">Design Matra</span>
            <span class="comp-role">Product Designer</span>
          </div>
          <div class="timeline-details">
            <p>Designed core flows for SaaS, FinTech, and consumer applications. Conducted user research sprints and established modular interface libraries.</p>
          </div>
          <div class="timeline-period">2021 &mdash; 2023</div>
        </div>

        <div class="timeline-item">
          <div class="timeline-company">
            <span class="comp-name">Kitaro Trading</span>
            <span class="comp-role">Graphic &amp; UI Designer</span>
          </div>
          <div class="timeline-details">
            <p>Crafted digital brand identities, marketing assets, and early web interfaces across consumer lifestyle products.</p>
          </div>
          <div class="timeline-period">2015 &mdash; 2021</div>
        </div>
      </div>
    </section>

    <!-- 04 — WHAT I EXPLORE -->
    <section class="about-editorial-block">
      <span class="eyebrow"><span class="dot"></span> Chapter 03</span>
      <h2>What I Explore</h2>
      <p>My current focus areas across the spectrum of product thinking and craft:</p>
      
      <div class="explore-grid">
        <div class="explore-pill">
          <h4>Product Design</h4>
          <p>Architecting user journeys, wireframing, and delivering pixel-perfect production screens.</p>
        </div>
        <div class="explore-pill">
          <h4>User Experience</h4>
          <p>Rooting decisions in user testing, cognitive ergonomics, and information hierarchy.</p>
        </div>
        <div class="explore-pill">
          <h4>Design Systems</h4>
          <p>Building reusable component libraries, design tokens, and scalable team guidelines.</p>
        </div>
        <div class="explore-pill">
          <h4>AI &amp; Emerging Tech</h4>
          <p>Exploring conversational interfaces, generative workflows, and AI-assisted creation.</p>
        </div>
        <div class="explore-pill">
          <h4>Product Strategy</h4>
          <p>Aligning customer desirability with business viability and technical feasibility.</p>
        </div>
        <div class="explore-pill">
          <h4>Creative Exploration</h4>
          <p>Pushing visual craft outside briefs through experiments, industrial design, and 3D shots.</p>
        </div>
      </div>
    </section>

    <!-- 05 — MY PERSPECTIVE -->
    <section class="about-editorial-block">
      <span class="eyebrow"><span class="dot"></span> Chapter 04</span>
      <h2>My Perspective</h2>
      <p>
        I believe that great product design is rarely about adding more &mdash; it is about deliberate subtraction until what remains feels obvious, natural, and indispensable.
      </p>
      <p>
        Curiosity is the fuel. Whether diving into frontend code, testing a new LLM model, or examining physical product packaging, staying curious ensures that every solution is informed by a broad perspective on how things work and why people care.
      </p>
    </section>

    <!-- 06 — READ MY RESUME CTA -->
    <section class="contact-cta-section" style="margin-top:40px; margin-bottom:56px;">
      <span class="eyebrow"><span class="dot"></span> Career History</span>
      <h2>Read My Resume</h2>
      <p>Explore my detailed professional timeline, credentials, key accomplishments, and download a printable PDF copy.</p>
      <div class="cta-btns">
        <a href="resume.html" class="btn btn-primary">Go to Resume Page &rarr;</a>
        <a href="assets/Sumit_Rai_Resume.pdf" download class="btn btn-secondary">Download Resume PDF &darr;</a>
      </div>
    </section>

    <!-- BEYOND THE PIXEL PHOTO GALLERY -->
    <section class="beyond-wrap">
      <div class="section-header-row" style="margin-bottom:16px;">
        <div class="section-title-wrap">
          <span class="eyebrow"><span class="dot"></span> Life Outside Pixels</span>
          <h3 style="font-size:1.3rem;">Beyond the Screen</h3>
        </div>
      </div>

      <div class="beyond-gallery" aria-label="Moments and photography by Sumit Rai">
        <div class="beyond-track">
          <figure class="photo-card"><img src="./assets/img_01.jpg" alt="Moment 01" loading="lazy" /></figure>
          <figure class="photo-card"><img src="./assets/img_03.jpg" alt="Moment 03" loading="lazy" /></figure>
          <figure class="photo-card"><img src="./assets/img_04.jpg" alt="Moment 04" loading="lazy" /></figure>
          <figure class="photo-card"><img src="./assets/img_06.jpg" alt="Moment 06" loading="lazy" /></figure>
          <figure class="photo-card"><img src="./assets/img_07.jpg" alt="Moment 07" loading="lazy" /></figure>
          <figure class="photo-card"><img src="./assets/img_08.jpg" alt="Moment 08" loading="lazy" /></figure>
          <!-- Loop Duplicates -->
          <figure class="photo-card" aria-hidden="true"><img src="./assets/img_01.jpg" alt="" loading="lazy" /></figure>
          <figure class="photo-card" aria-hidden="true"><img src="./assets/img_03.jpg" alt="" loading="lazy" /></figure>
          <figure class="photo-card" aria-hidden="true"><img src="./assets/img_04.jpg" alt="" loading="lazy" /></figure>
          <figure class="photo-card" aria-hidden="true"><img src="./assets/img_06.jpg" alt="" loading="lazy" /></figure>
          <figure class="photo-card" aria-hidden="true"><img src="./assets/img_07.jpg" alt="" loading="lazy" /></figure>
          <figure class="photo-card" aria-hidden="true"><img src="./assets/img_08.jpg" alt="" loading="lazy" /></figure>
        </div>
      </div>
    </section>

  </div>
</main>
"""
    return get_head("About — Sumit Rai", "about") + get_nav("about") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"

# -------------------------------------------------------------
# PAGE 4: RESUME.HTML (DEDICATED, STRUCTURED & PRINTABLE)
# -------------------------------------------------------------
def build_resume():
    content = f"""
<main class="page-body">
  <div class="wrap">
    
    <div class="resume-view-wrap">
      
      <!-- Top Actions Bar -->
      <div class="resume-top-bar">
        <a href="index.html" class="back-link">&larr; Back to Portfolio</a>
        <div class="resume-actions-group">
          <button class="btn btn-secondary btn-sm" onclick="window.print()" title="Print or save as PDF">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
            <span>Print Resume</span>
          </button>
          <a href="./assets/Sumit_Rai_Resume.pdf" download="Sumit_Rai_Resume.pdf" class="btn btn-primary btn-sm" id="downloadResumePdf">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            <span>Download Resume PDF &darr;</span>
          </a>
        </div>
      </div>

      <!-- Resume Paper Sheet -->
      <article class="resume-paper" id="resumePaper">
        
        <!-- Header -->
        <header class="resume-header">
          <h1 class="resume-name">Sumit Rai</h1>
          <div class="resume-title">Senior Product Designer &nbsp;|&nbsp; AI Builder</div>
          <div class="resume-contacts">
            <span>Delhi, India</span>
            <span>&bull;</span>
            <a href="mailto:sumitraiworks@gmail.com">sumitraiworks@gmail.com</a>
            <span>&bull;</span>
            <a href="https://www.linkedin.com/in/isumitrai/" target="_blank" rel="noopener">linkedin.com/in/isumitrai</a>
            <span>&bull;</span>
            <a href="https://isumitrai.github.io/" target="_blank" rel="noopener">isumitrai.github.io</a>
          </div>
        </header>

        <!-- 1. Professional Summary -->
        <section class="resume-section">
          <h3 class="section-heading">Professional Summary</h3>
          <p class="resume-summary-text">
            Product Designer with 7+ years of product design experience since 2019 and 10+ years of overall design experience. Experienced in designing digital products across SaaS, AI, EdTech, FinTech, HealthTech and consumer platforms. Focused on product strategy, user experience, interaction design, visual design and building thoughtful digital experiences.
          </p>
        </section>

        <!-- 2. Professional Experience -->
        <section class="resume-section">
          <h3 class="section-heading">Professional Experience</h3>
          
          <div class="resume-item">
            <div class="resume-item-head">
              <span class="resume-item-role">Founding Designer</span>
              <span class="resume-item-date">2025 &mdash; Present</span>
            </div>
            <div class="resume-item-org">Raimage Design &middot; Independent Design Studio &middot; New Delhi, India</div>
            <ul>
              <li>Directing end-to-end product design, brand architecture, and AI-native interface explorations for high-growth tech ventures.</li>
              <li>Spearheading product strategy, component libraries, and rapid interactive prototyping combining Figma and frontend code.</li>
              <li>Partnering closely with founders and engineering leaders to translate complex domain workflows into intuitive digital products.</li>
            </ul>
          </div>

          <div class="resume-item">
            <div class="resume-item-head">
              <span class="resume-item-role">Senior Product Designer</span>
              <span class="resume-item-date">2023 &mdash; 2025</span>
            </div>
            <div class="resume-item-org">Edfora Infotech &middot; EdTech / FIITJEE Ecosystem &middot; New Delhi, India</div>
            <ul>
              <li>Led product design across web and mobile platforms for FIITJEE educational products, multi-tenant administrative dashboards, and student collaboration hubs.</li>
              <li>Collaborated with cross-functional leadership on user research insights, data-informed roadmaps, and examination workflows.</li>
              <li>Architected a unified design system that accelerated design-to-development delivery velocity by 35%.</li>
            </ul>
          </div>

          <div class="resume-item">
            <div class="resume-item-head">
              <span class="resume-item-role">Product Designer</span>
              <span class="resume-item-date">2021 &mdash; 2023</span>
            </div>
            <div class="resume-item-org">Design Matra &middot; Digital Product Agency &middot; New Delhi, India</div>
            <ul>
              <li>Owned UX/UI design for high-traffic SaaS and mobile products across FinTech, HealthTech, and E-Commerce sectors.</li>
              <li>Redesigned core onboarding, search, and checkout funnels, driving measurable gains in user conversion and retention.</li>
              <li>Conducted generative usability research, rapid iterative prototyping, and comprehensive responsive design audits.</li>
            </ul>
          </div>

          <div class="resume-item">
            <div class="resume-item-head">
              <span class="resume-item-role">Graphic &amp; Interface Designer</span>
              <span class="resume-item-date">2015 &mdash; 2021</span>
            </div>
            <div class="resume-item-org">Kitaro Trading &middot; New Delhi, India</div>
            <ul>
              <li>Designed digital brand identities, marketing assets, and responsive web interfaces across diverse consumer product portfolios.</li>
              <li>Created foundational brand guidelines, design tokens, and multi-channel creative visual communication assets.</li>
            </ul>
          </div>

        </section>

        <!-- 3. Selected Projects & Achievements -->
        <section class="resume-section">
          <h3 class="section-heading">Selected Projects &amp; Achievements</h3>
          <div class="resume-item">
            <div class="resume-item-head">
              <span class="resume-item-role">EduManage</span>
              <span class="resume-item-date">SaaS Dashboard &middot; CMS</span>
            </div>
            <p style="font-size:13px; color:var(--ink-soft); margin-top:2px;">
              Smart educational management dashboard unifying academic operations, multi-tenant CMS, and staff workflows into a high-clarity workspace.
            </p>
          </div>
          <div class="resume-item">
            <div class="resume-item-head">
              <span class="resume-item-role">Quayo Basket</span>
              <span class="resume-item-date">Mobile App &middot; Brand Identity</span>
            </div>
            <p style="font-size:13px; color:var(--ink-soft); margin-top:2px;">
              Grocery shopping mobile application and complete retail brand identity system engineered for effortless product discovery and streamlined checkout.
            </p>
          </div>
          <div class="resume-item">
            <div class="resume-item-head">
              <span class="resume-item-role">Musafir</span>
              <span class="resume-item-date">Web Design &middot; Marketplace</span>
            </div>
            <p style="font-size:13px; color:var(--ink-soft); margin-top:2px;">
              Travel marketplace landing page redesigned for stronger conversion paths, destination framing, and confident trip planning.
            </p>
          </div>
          <div class="resume-item">
            <div class="resume-item-head">
              <span class="resume-item-role">Community</span>
              <span class="resume-item-date">EdTech Platform &middot; Learning Hub</span>
            </div>
            <p style="font-size:13px; color:var(--ink-soft); margin-top:2px;">
              Collaborative study hub connecting students through structured peer question channels, mentor discussions, and subject study repositories.
            </p>
          </div>
        </section>

        <!-- 4. Skills & Competencies -->
        <section class="resume-section">
          <h3 class="section-heading">Skills &amp; Competencies</h3>
          
          <div class="resume-skills-block">
            <span class="resume-skills-label">Product Design:</span>
            <span class="resume-skills-val">Product Strategy, UX Research, Interaction Design, Design Systems, Information Architecture, Wireframing, Rapid Prototyping</span>
          </div>

          <div class="resume-skills-block">
            <span class="resume-skills-label">Tools &amp; Stack:</span>
            <span class="resume-skills-val">Figma, Framer, Webflow, VS Code, Cursor, HTML/CSS/JavaScript, AI Workflows (Midjourney, LLMs), Adobe Illustrator, Photoshop, Jira</span>
          </div>

          <div class="resume-skills-block">
            <span class="resume-skills-label">Domain Breadth:</span>
            <span class="resume-skills-val">SaaS, Enterprise Dashboards, EdTech, FinTech, HealthTech, E-Commerce &amp; Consumer Platforms</span>
          </div>
        </section>

        <!-- 5. Education -->
        <section class="resume-section" style="margin-bottom:0;">
          <h3 class="section-heading">Education &amp; Credentials</h3>
          <div class="resume-item">
            <div class="resume-item-head">
              <span class="resume-item-role">Bachelor's Degree &middot; Foundations in Design &amp; Technology</span>
              <span class="resume-item-date">Graduated</span>
            </div>
            <div class="resume-item-org">India</div>
          </div>
        </section>

      </article>

      <div style="display:flex; justify-content:center; margin-top:32px;">
        <a href="./assets/Sumit_Rai_Resume.pdf" download="Sumit_Rai_Resume.pdf" class="btn btn-primary">
          Download Official Resume PDF &darr;
        </a>
      </div>

    </div>

  </div>
</main>
"""
    return get_head("Resume — Sumit Rai", "resume") + get_nav("resume") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"

# -------------------------------------------------------------
# PAGE 5: PLAYGROUND.HTML (EXPERIMENTS & UI SHOTS)
# -------------------------------------------------------------
def build_playground():
    items = [
        {"title": "Koolkidz Watches Design", "desc": "Playful children's product concept and watch face visual explorations.", "img": "./assets/pg_001.jpg"},
        {"title": "Stacklet AI Dev Projects", "desc": "Dark-mode AI developer environment and command dashboard concept.", "img": "./assets/pg_002.jpg"},
        {"title": "Chhota Bheem Branding", "desc": "Character packaging and identity exploration for merchandise.", "img": "./assets/pg_003.jpg"},
        {"title": "Radio Concept", "desc": "Retro-futuristic physical audio device interface and hardware study.", "img": "./assets/pg_004.jpg"},
    ]

    cards_html = ""
    for item in items:
        cards_html += f"""
      <article class="pg-card">
        <div class="pg-img">
          <img src="{item['img']}" alt="{item['title']}" loading="lazy" />
        </div>
        <div class="pg-info">
          <h3>{item['title']}</h3>
          <p>{item['desc']}</p>
        </div>
      </article>
"""

    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <div class="section-header-row" style="margin-top:24px; margin-bottom:32px;">
      <div class="section-title-wrap">
        <span class="eyebrow"><span class="dot"></span> Creative Explorations</span>
        <h1 style="font-size:clamp(2rem, 3.6vw, 2.8rem); margin-bottom:8px;">Experiments &amp; UI shots</h1>
        <p>Visual explorations, UI experiments, and creative side concepts built outside production briefs.</p>
      </div>
    </div>

    <div class="pg-grid">
      {cards_html}
    </div>

  </div>
</main>
"""
    return get_head("Playground — Sumit Rai", "playground") + get_nav("playground") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"


# -------------------------------------------------------------
# Generate All Pages
# -------------------------------------------------------------
def main():
    pages = {
        "index.html": build_index(),
        "projects.html": build_projects(),
        "about.html": build_about(),
        "resume.html": build_resume(),
        "playground.html": build_playground()
    }

    for filename, html in pages.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {filename} successfully ({len(html)} bytes)")

if __name__ == "__main__":
    main()
