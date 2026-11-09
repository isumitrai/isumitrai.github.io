#!/usr/bin/env python3
"""
Master Page Generator for Sumit Rai Portfolio V2 — Enhanced Edition
Fulfills all updated user requirements:
1. Typography from ref Debi portfolio: Plus Jakarta Sans (Headings) + Inter (Body/UI) + Space Mono (Micro-copy)
2. Debi-style nickname treatment on main page: "Hi, I'm Sumit Rai (most people call me Sumi or Sumo)"
3. Toolkit & Environment: Uses images tools01.jpg through tools18.jpg from assets/src/
4. Client & Brand Partners: Clean unbordered layout, equalized logo sizes, uniform grayscale, NO color inversion in dark mode!
5. Playground: Enhanced with Raimage Design studio lab styling (fine art prints, tools & UI concepts, industrial & 3D)
6. Dedicated Contact Page (contact.html) + Surprise features:
   - Live New Delhi, India local time clock widget (real-time updating)
   - Interactive intent pill selector with auto-drafting email
   - Pure Web Audio synthetic haptic sound engine (toggleable via header pill)
"""

import os
import json
import html

# Projects Database with structured case studies
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

# 18 Real Tool Images (assets/src/tools01.jpg to tools18.jpg)
TOOLS = [
    {"name": "Figma", "img": "./assets/src/tools01.jpg"},
    {"name": "Framer", "img": "./assets/src/tools02.jpg"},
    {"name": "Webflow", "img": "./assets/src/tools03.jpg"},
    {"name": "Arc", "img": "./assets/src/tools04.jpg"},
    {"name": "VS Code", "img": "./assets/src/tools05.jpg"},
    {"name": "Cursor", "img": "./assets/src/tools06.jpg"},
    {"name": "Spline 3D", "img": "./assets/src/tools07.jpg"},
    {"name": "Midjourney", "img": "./assets/src/tools08.jpg"},
    {"name": "Notion", "img": "./assets/src/tools09.jpg"},
    {"name": "ChatGPT", "img": "./assets/src/tools10.jpg"},
    {"name": "Bolt.new", "img": "./assets/src/tools11.jpg"},
    {"name": "GitHub", "img": "./assets/src/tools12.jpg"},
    {"name": "Illustrator", "img": "./assets/src/tools13.jpg"},
    {"name": "Photoshop", "img": "./assets/src/tools14.jpg"},
    {"name": "InDesign", "img": "./assets/src/tools15.jpg"},
    {"name": "Slack", "img": "./assets/src/tools16.jpg"},
    {"name": "Jira", "img": "./assets/src/tools17.jpg"},
    {"name": "Linear", "img": "./assets/src/tools18.jpg"}
]

def get_head(title="Sumit Rai — Senior Product Designer | AI Builder", active_page="index"):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="Sumit Rai (Sumi) — Senior Product Designer &amp; AI Builder with 7+ years of product design and 10+ years of overall design experience across SaaS, AI, EdTech, FinTech, and consumer platforms." />
  <meta name="author" content="Sumit Rai" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
"""

def get_nav(active_page):
    return f"""
<header class="nav-wrap" id="siteHeader">
  <div class="nav-pill">
    <div class="nav-logo-group">
      <a href="index.html" class="nav-logo" title="Sumit Rai">
        <span class="sr-mark">SR</span>
        <span>Sumit Rai</span>
      </a>
    </div>

    <nav class="nav-tabs" id="navTabs" aria-label="Main Navigation">
      <a href="projects.html" class="{'active' if active_page in ['projects'] else ''}">Work</a>
      <a href="about.html" class="{'active' if active_page == 'about' else ''}">About</a>
      <a href="resume.html" class="{'active' if active_page == 'resume' else ''}">Resume</a>
      <a href="playground.html" class="{'active' if active_page == 'playground' else ''}">Playground</a>
      <a href="contact.html" class="{'active' if active_page == 'contact' else ''}">Contact</a>
    </nav>

    <div class="nav-right-actions">
      <button class="nav-action-pill" id="soundToggleBtn" aria-label="Toggle haptic sounds">
        <span id="soundIcon">🔊</span>
        <span id="soundLabel" class="sound-label-text">Sound</span>
      </button>
      <button class="nav-action-pill" id="cmdPaletteTrigger" aria-label="Quick navigation (Cmd+K)">
        <kbd>⌘K</kbd>
      </button>
      <button class="nav-menu-toggle" id="navMenuToggle" aria-label="Toggle navigation menu" aria-expanded="false">
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
      </button>
    </div>
  </div>

  <!-- Mobile nav drawer -->
  <div class="mobile-nav-drawer" id="mobileNavDrawer" aria-hidden="true">
    <nav class="mobile-nav-links">
      <a href="index.html" class="{'active' if active_page == 'index' else ''}">Home</a>
      <a href="projects.html" class="{'active' if active_page in ['projects'] else ''}">Work</a>
      <a href="about.html" class="{'active' if active_page == 'about' else ''}">About</a>
      <a href="resume.html" class="{'active' if active_page == 'resume' else ''}">Resume</a>
      <a href="playground.html" class="{'active' if active_page == 'playground' else ''}">Playground</a>
      <a href="contact.html" class="{'active' if active_page == 'contact' else ''}">Contact</a>
    </nav>
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
      <div class="footer-clock-box" id="delhiClockWrap">
        <span class="live-dot"></span>
        <span>New Delhi, India &middot; <strong id="liveClockText">--:-- -- IST</strong></span>
      </div>
      <div class="flinks">
        <a href="https://www.linkedin.com/in/isumitrai/" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://x.com/isumitrai" target="_blank" rel="noopener">X</a>
        <a href="https://www.instagram.com/isumitrai/" target="_blank" rel="noopener">Instagram</a>
        <a href="contact.html">Contact</a>
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
          <span>Resume &amp; Credentials</span>
        </span>
        <span class="cmd-shortcut">R</span>
      </a>
      <a href="playground.html" class="cmd-item">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m10 15 5-3-5-3v6Z"/></svg>
          <span>Playground (Raimage Lab)</span>
        </span>
        <span class="cmd-shortcut">P</span>
      </a>
      <a href="contact.html" class="cmd-item">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span>Get in Touch (Contact Page)</span>
        </span>
        <span class="cmd-shortcut">C</span>
      </a>
      <a href="assets/Sumit_Rai_Resume.pdf" download class="cmd-item">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <span>Download Resume PDF</span>
        </span>
        <span class="cmd-shortcut">PDF</span>
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
// ---- Global Audio, Clock, Theme & Command Palette Management ----
(function(){
  // 1. Web Audio Synthesizer Haptic Engine
  const AudioEngine = (function(){
    let ctx = null;
    let enabled = localStorage.getItem('sr_sound') === 'true';

    function init(){
      if (!ctx && (window.AudioContext || window.webkitAudioContext)) {
        ctx = new (window.AudioContext || window.webkitAudioContext)();
      }
    }

    function playTick(freq = 820, dur = 0.035, type = 'sine'){
      if (!enabled) return;
      try {
        init();
        if (ctx.state === 'suspended') ctx.resume();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, ctx.currentTime);
        gain.gain.setValueAtTime(0.06, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + dur);
      } catch(e) {}
    }

    function toggle(){
      enabled = !enabled;
      localStorage.setItem('sr_sound', enabled);
      if (enabled) playTick(960, 0.05);
      return enabled;
    }

    function isEnabled(){ return enabled; }

    return { playTick, toggle, isEnabled };
  })();

  // Update Sound Button State
  const soundBtn = document.getElementById('soundToggleBtn');
  const soundIcon = document.getElementById('soundIcon');
  const soundLabel = document.getElementById('soundLabel');
  function updateSoundUI(){
    const on = AudioEngine.isEnabled();
    if (soundIcon) soundIcon.textContent = on ? '🔊' : '🔇';
    if (soundLabel) soundLabel.textContent = on ? 'Sound' : 'Muted';
    if (soundBtn) soundBtn.classList.toggle('active', on);
  }
  updateSoundUI();
  if (soundBtn) {
    soundBtn.addEventListener('click', function(){
      AudioEngine.toggle();
      updateSoundUI();
    });
  }

  // Play micro click on link / button clicks
  document.addEventListener('click', function(e){
    if (e.target.closest('a, button, .proj-card, .tool-tile, .pg-card-rich')) {
      AudioEngine.playTick(780, 0.028);
    }
  });

  // 2. Real-time New Delhi (IST) Clock
  function updateDelhiClock(){
    const textEl = document.getElementById('liveClockText');
    const pageVal = document.getElementById('delhiLiveClockVal');
    const now = new Date();
    // New Delhi is UTC +5:30
    const istOffset = 5.5 * 60 * 60 * 1000;
    const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
    const delhiDate = new Date(utc + istOffset);

    let h = delhiDate.getHours();
    const m = String(delhiDate.getMinutes()).padStart(2, '0');
    const s = String(delhiDate.getSeconds()).padStart(2, '0');
    const ampm = h >= 12 ? 'PM' : 'AM';
    h = h % 12 || 12;

    const formatted = `${h}:${m}:${s} ${ampm} IST`;
    if (textEl) textEl.textContent = formatted;
    if (pageVal) pageVal.textContent = formatted;
  }
  setInterval(updateDelhiClock, 1000);
  updateDelhiClock();

  // 3. Dark/Light Mode
  const root = document.documentElement;
  const themeToggle = document.getElementById('themeToggle');
  const storedTheme = localStorage.getItem('sr_theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  if (storedTheme === 'dark') root.setAttribute('data-theme', 'dark');

  function toggleTheme(){
    const isDark = root.getAttribute('data-theme') === 'dark';
    const next = isDark ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    localStorage.setItem('sr_theme', next);
    AudioEngine.playTick(isDark ? 650 : 880, 0.04);
  }
  if (themeToggle) themeToggle.addEventListener('click', toggleTheme);

  // 4. Scroll Header — add scrolled class for backdrop effect (always visible)
  const header = document.getElementById('siteHeader');
  window.addEventListener('scroll', function(){
    if (header) {
      header.classList.toggle('nav-scrolled', window.scrollY > 40);
    }
  }, { passive: true });

  // 4b. Mobile Nav Toggle (hamburger)
  const navMenuToggle = document.getElementById('navMenuToggle');
  const mobileNavDrawer = document.getElementById('mobileNavDrawer');
  if (navMenuToggle && mobileNavDrawer) {
    navMenuToggle.addEventListener('click', function(){
      const isOpen = mobileNavDrawer.classList.toggle('open');
      navMenuToggle.setAttribute('aria-expanded', isOpen);
      mobileNavDrawer.setAttribute('aria-hidden', !isOpen);
      navMenuToggle.classList.toggle('open', isOpen);
    });
    // Close drawer on nav link click
    mobileNavDrawer.querySelectorAll('a').forEach(function(link){
      link.addEventListener('click', function(){
        mobileNavDrawer.classList.remove('open');
        navMenuToggle.setAttribute('aria-expanded', 'false');
        navMenuToggle.classList.remove('open');
      });
    });
  }

  // 5. Copy Email
  const copyBtn = document.getElementById('copyEmailBtn');
  if (copyBtn) {
    copyBtn.addEventListener('click', function(e){
      e.preventDefault();
      navigator.clipboard.writeText('sumitraiworks@gmail.com').then(function(){
        copyBtn.classList.add('copied');
        AudioEngine.playTick(1020, 0.06);
        setTimeout(function(){ copyBtn.classList.remove('copied'); }, 2000);
      });
    });
  }

  // 6. Interactive Nickname Cycle (Debi Style)
  const nickBtn = document.getElementById('nicknameToggle');
  if (nickBtn) {
    const nicks = ['Sumi', 'Sumo'];
    let idx = 0;
    nickBtn.addEventListener('click', function(e){
      e.preventDefault();
      idx = (idx + 1) % nicks.length;
      nickBtn.textContent = nicks[idx];
      AudioEngine.playTick(880 + (idx * 120), 0.04);
    });
  }

  // 7. Command + K Palette
  const cmdModal = document.getElementById('cmdModal');
  const cmdTrigger = document.getElementById('cmdPaletteTrigger');
  const cmdInput = document.getElementById('cmdInput');
  const cmdList = document.getElementById('cmdList');
  const cmdThemeBtn = document.getElementById('cmdToggleTheme');

  function openCmd(){
    if (!cmdModal) return;
    cmdModal.classList.add('active');
    AudioEngine.playTick(720, 0.03);
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
            <span class="proj-view-link">Case Study</span>
            <div class="proj-tech-tags">
              <span class="proj-tag">{p['tags'][0]}</span>
              <span class="proj-tag">{p['tags'][1]}</span>
            </div>
          </div>
        </div>
      </article>
"""

    # Requirement 4: Clean, unbordered, equalized grayscale logos (NO COLOR INVERT IN DARK MODE)
    brands_html = ""
    for b in BRANDS:
        brands_html += f"""
        <div class="brand-item-clean" title="{b['name']}">
          <img src="{b['img']}" alt="{b['name']}" loading="lazy" />
        </div>
"""

    # Requirement 3: 18 tool images from assets/src/tools01.jpg to tools18.jpg
    tools_html = ""
    for t in TOOLS:
        tools_html += f"""
        <div class="tool-tile" title="{t['name']}">
          <img src="{t['img']}" alt="{t['name']}" loading="lazy" />
          <span class="tool-name">{t['name']}</span>
        </div>
"""

    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <!-- SECTION 01 — HERO -->
    <section class="hero">
      <div class="status-pill">
        <span class="dot"></span>
        <span>Senior Product Designer &middot; AI Builder</span>
      </div>

      <h1 class="hero-greeting">
        Hi, I'm Sumit Rai.
      </h1>

      <p class="hero-statement">I design products, build experiences<br>and explore what's next.</p>
      
      <p class="hero-description">
        Senior Product Designer and AI Builder — exploring the intersection of design, technology and thoughtful product experiences.
      </p>

      <div class="cta-row">
        <a href="#work" class="btn btn-primary">View My Work</a>
        <a href="about.html" class="btn btn-secondary">About Me</a>
        <a href="contact.html" class="btn btn-ghost">Get in Touch</a>
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
        <a href="projects.html" class="section-header-link">All Work</a>
      </div>

      <div class="proj-grid">
        {projects_cards_html}
      </div>

      <div class="see-all-wrap">
        <a href="projects.html" class="btn btn-secondary">All Work</a>
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
            <a href="about.html" class="btn btn-secondary">About Me</a>
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
        <a href="resume.html" class="section-header-link">Full Resume</a>
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

      <!-- REQUIREMENT 4: CLIENT BRANDS (CLEAN, EQUAL SIZE, MONOCHROME, NO INVERT IN DARK) -->
      <div class="brands-wrap">
        <div class="section-header-row" style="margin-bottom:16px;">
          <div class="section-title-wrap">
            <span class="eyebrow"><span class="dot"></span> Client &amp; Brand Partners</span>
            <h3 style="font-size:1.35rem;">Brands I've Helped Shape</h3>
          </div>
        </div>
        <div class="brands-grid-clean">
          {brands_html}
        </div>
      </div>

      <!-- REQUIREMENT 3: TOOLKIT & ENVIRONMENT WITH IMAGES (tools01 to tools18) -->
      <div class="tools-wrap">
        <div class="section-header-row" style="margin-bottom:16px;">
          <div class="section-title-wrap">
            <span class="eyebrow"><span class="dot"></span> Toolkit &amp; Environment</span>
            <h3 style="font-size:1.35rem;">Tools I Use to Think, Design &amp; Build</h3>
          </div>
        </div>
        <div class="tools-grid-img">
          {tools_html}
        </div>
      </div>
    </section>

    <!-- SECTION 06 — CONTACT CTA -->
    <section class="contact-cta-section">
      <span class="eyebrow"><span class="dot"></span> Contact</span>
      <h2>Have something interesting in mind?</h2>
      <p>I'm always open to meaningful conversations, interesting ideas and opportunities to build something thoughtful.</p>
      <div class="cta-btns">
        <a href="contact.html" class="btn btn-primary">Get in Touch</a>
        <a href="mailto:sumitraiworks@gmail.com" class="btn btn-secondary">Email Me</a>
      </div>
    </section>

  </div>
</main>
"""
    return get_head("Sumit Rai (Sumi) — Senior Product Designer | AI Builder", "index") + get_nav("index") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"

# -------------------------------------------------------------
# PAGE 2: PROJECTS.HTML (WORK ARCHIVE & INTERACTIVE CASE STUDIES)
# -------------------------------------------------------------
def build_projects():
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
            <span class="proj-view-link">Case Study</span>
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
            <span class="proj-view-link">Case Study</span>
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
          <span class="nav-eyebrow">Previous</span>
          <span class="nav-proj-name">${{prev.title}}</span>
        </button>
        <button class="case-nav-btn next" id="nextCaseBtn">
          <span class="nav-eyebrow">Next</span>
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

  window.addEventListener('DOMContentLoaded', () => {{
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
          <a href="resume.html" class="btn btn-primary">Read Resume</a>
          <a href="contact.html" class="btn btn-secondary">Get in Touch</a>
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
        <a href="resume.html" class="btn btn-primary">Resume Page</a>
        <a href="assets/Sumit_Rai_Resume.pdf" download class="btn btn-secondary">Download PDF</a>
      </div>
    </section>

    <!-- BEYOND THE PIXEL PHOTO GALLERY -->
    <section class="beyond-wrap">
      <div class="section-header-row" style="margin-bottom:16px;">
        <div class="section-title-wrap">
          <span class="eyebrow"><span class="dot"></span> Life Outside Pixels</span>
          <h3 style="font-size:1.35rem;">Beyond the Screen</h3>
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
          <!-- Duplicates for seamless looping -->
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
        <a href="index.html" class="back-link">Back to Portfolio</a>
        <div class="resume-actions-group">
          <button class="btn btn-secondary btn-sm" onclick="window.print()" title="Print or save as PDF">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
            <span>Print Resume</span>
          </button>
          <a href="./assets/Sumit_Rai_Resume.pdf" download="Sumit_Rai_Resume.pdf" class="btn btn-primary btn-sm" id="downloadResumePdf">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            <span>Download PDF</span>
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
          Download Resume PDF
        </a>
      </div>

    </div>

  </div>
</main>
"""
    return get_head("Resume — Sumit Rai", "resume") + get_nav("resume") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"

# -------------------------------------------------------------
# PAGE 5: PLAYGROUND.HTML (RAIMAGE STUDIO LAB REFERENCE STYLE)
# -------------------------------------------------------------
def build_playground():
    items = [
        {
            "id": "pg-1",
            "title": "Stacklet AI Dev Projects",
            "category": "Tools & UI Concepts",
            "tag": "AI · Developer Tool",
            "year": "2026",
            "desc": "AI-native developer terminal HUD, interactive command palettes, and dark-mode coding canvas.",
            "img": "./assets/pg_002.jpg"
        },
        {
            "id": "pg-2",
            "title": "Koolkidz Watches Design",
            "category": "Industrial & 3D",
            "tag": "Product · Hardware",
            "year": "2025",
            "desc": "Playful children's digital timepiece, tactile silicone strap explorations, and graphic watch faces.",
            "img": "./assets/pg_001.jpg"
        },
        {
            "id": "pg-3",
            "title": "Radio Concept Hardware",
            "category": "Industrial & 3D",
            "tag": "Hardware · Audio",
            "year": "2025",
            "desc": "Tactile retro-futuristic audio device concept with mechanical switches and digital frequency display.",
            "img": "./assets/pg_004.jpg"
        },
        {
            "id": "pg-4",
            "title": "Chhota Bheem Branding",
            "category": "Brand & Packaging",
            "tag": "Packaging · Character",
            "year": "2024",
            "desc": "Commercial merchandise branding, character packaging system, and retail promotional graphics.",
            "img": "./assets/pg_003.jpg"
        },
        {
            "id": "pg-5",
            "title": "A Walk to Remember — Art Print",
            "category": "Fine Art & Prints",
            "tag": "Fine Art · Digital Print",
            "year": "2025",
            "desc": "Limited digital print study exploring atmospheric lighting, warm monochrome tones, and visual silence. Featured on Raimage Design.",
            "img": "./assets/img_01.jpg"
        },
        {
            "id": "pg-6",
            "title": "A Thousand Years — Typography Study",
            "category": "Fine Art & Prints",
            "tag": "Editorial · Architecture",
            "year": "2024",
            "desc": "Monochromatic architectural photography coupled with brutalist typographic hierarchy. Available on Raimage Studio Lab.",
            "img": "./assets/img_03.jpg"
        },
        {
            "id": "pg-7",
            "title": "Tactile Color Calibration",
            "category": "Tools & UI Concepts",
            "tag": "Design Tokens · Palette",
            "year": "2025",
            "desc": "Experimental design token generator and CMYK print calibration grid designed for studio pipelines.",
            "img": "./assets/img_04.jpg"
        },
        {
            "id": "pg-8",
            "title": "Generative Waveform Study",
            "category": "Tools & UI Concepts",
            "tag": "Generative · Visual",
            "year": "2025",
            "desc": "Procedural noise patterns and audio wave visualizers explored for emerging AI sound interfaces.",
            "img": "./assets/img_07.jpg"
        }
    ]

    cards_html = ""
    for item in items:
        safe_title = html.escape(item['title'], quote=True)
        safe_desc = html.escape(item['desc'], quote=True)
        safe_tag = html.escape(item['tag'], quote=True)
        cards_html += f"""
      <article class="pg-card-rich" data-category="{item['category'].lower()}" data-title="{safe_title}" data-desc="{safe_desc}" data-img="{item['img']}" data-tag="{safe_tag}" role="button" tabindex="0">
        <div class="pg-preview">
          <img src="{item['img']}" alt="{safe_title}" loading="lazy" />
        </div>
        <div class="pg-meta-body">
          <div class="pg-cat-row">
            <span class="pg-tag">{safe_tag}</span>
            <span class="pg-year">{item['year']}</span>
          </div>
          <h3>{safe_title}</h3>
          <p>{safe_desc}</p>
          <div class="pg-foot">
            <span>Inspect</span>
            <span style="font-size:11px; opacity:0.7;">Raimage Lab</span>
          </div>
        </div>
      </article>
"""

    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <div class="pg-hero-block">
      <span class="eyebrow"><span class="dot"></span> Raimage Design Studio Lab</span>
      <h1>Playground &amp; Creative Lab</h1>
      <p>
        Visual explorations, experimental tools, fine art prints, and creative side concepts shaped outside client briefs. Inspired by the active studio pipelines at <a href="https://www.raimagedesign.com" target="_blank" rel="noopener" style="text-decoration:underline; font-weight:600;">Raimage Design</a>.
      </p>
    </div>

    <!-- Filter Tabs -->
    <div class="pg-filter-row" id="pgFilterRow">
      <button class="filter-btn active" data-filter="all">All Experiments (8)</button>
      <button class="filter-btn" data-filter="tools & ui concepts">Tools &amp; UI Concepts</button>
      <button class="filter-btn" data-filter="fine art & prints">Fine Art &amp; Prints</button>
      <button class="filter-btn" data-filter="industrial & 3d">Industrial &amp; 3D</button>
      <button class="filter-btn" data-filter="brand & packaging">Brand &amp; Packaging</button>
    </div>

    <div class="pg-grid-rich" id="pgGrid">
      {cards_html}
    </div>

  </div>
</main>

<!-- Lightbox Modal for Playground Artifacts -->
<div class="cmd-modal" id="pgModal" role="dialog" aria-modal="true" aria-label="Exploration Preview">
  <div class="cmd-box" style="max-width:720px; padding:0; overflow:hidden;">
    <div style="aspect-ratio:16/10; width:100%; background:var(--surface-subtle); overflow:hidden;">
      <img id="pgModalImg" src="" alt="" style="width:100%; height:100%; object-fit:cover;" />
    </div>
    <div style="padding:24px 28px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <span class="tag-chip" id="pgModalTag" style="color:var(--accent);">Tag</span>
        <button onclick="document.getElementById('pgModal').classList.remove('active')" style="font-size:12px; font-weight:600; color:var(--ink-soft);">&times; Close</button>
      </div>
      <h2 id="pgModalTitle" style="font-size:1.45rem; margin-bottom:8px;">Title</h2>
      <p id="pgModalDesc" style="font-size:14px; line-height:1.6; color:var(--ink-soft);">Description</p>
    </div>
  </div>
</div>
"""

    pg_js = """
  // Filter Playground Items
  const filterBtns = document.querySelectorAll('#pgFilterRow .filter-btn');
  const cards = document.querySelectorAll('.pg-card-rich');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const target = btn.dataset.filter.toLowerCase();
      cards.forEach(card => {
        const cat = card.dataset.category;
        card.style.display = (target === 'all' || cat.includes(target)) ? 'flex' : 'none';
      });
    });
  });

  // Modal inspection
  window.openPgModal = function(title, desc, img, tag){
    const modal = document.getElementById('pgModal');
    if (!modal) return;
    document.getElementById('pgModalTitle').textContent = title;
    document.getElementById('pgModalDesc').textContent = desc;
    document.getElementById('pgModalImg').src = img;
    document.getElementById('pgModalTag').textContent = tag;
    modal.classList.add('active');
  };

  cards.forEach(card => {
    function triggerOpen(){
      openPgModal(card.dataset.title, card.dataset.desc, card.dataset.img, card.dataset.tag);
    }
    card.addEventListener('click', triggerOpen);
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        triggerOpen();
      }
    });
  });

  const modal = document.getElementById('pgModal');
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) modal.classList.remove('active');
    });
  }
"""

    return get_head("Playground & Studio Lab — Sumit Rai", "playground") + get_nav("playground") + content + footer_html + f"<script>\n{global_js}\n{pg_js}\n</script>\n</body>\n</html>"

# -------------------------------------------------------------
# PAGE 6: CONTACT.HTML (DEDICATED CONTACT PAGE + SURPRISE FEATURES)
# -------------------------------------------------------------
def build_contact():
    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <!-- Hero -->
    <div class="contact-hero-wrap">
      <div class="status-pill">
        <span class="dot"></span>
        <span>Available for Q1/Q2 2026 Collaborations</span>
      </div>
      <h1>Let's start a conversation.</h1>
      <p class="lead">
        Have an early-stage product in mind, a founding design role, or want to explore AI-native workflows? I'm always open to discussing new opportunities.
      </p>
    </div>

    <!-- Layout: Left Interactive Form, Right Live Delhi Clock & Direct Channels -->
    <div class="contact-grid-layout">
      
      <!-- Interactive Form Card -->
      <div class="contact-form-card">
        <span class="eyebrow"><span class="dot"></span> Quick Inquiries</span>
        <h2 style="font-size:1.45rem; margin-bottom:12px;">What are you looking to build?</h2>
        <p style="font-size:13.5px; color:var(--ink-soft); margin-bottom:18px;">
          Select a project focus below to auto-tailor the message starter:
        </p>

        <!-- Topic Selector Pills -->
        <div class="contact-intent-pills" id="intentPills">
          <button class="intent-pill active" data-topic="0-to-1 Product Design" data-lead="Hi Sumit, I'm working on a zero-to-one product and would love your product design expertise on...">🚀 0-to-1 Product</button>
          <button class="intent-pill" data-topic="Founding / Senior Role" data-lead="Hi Sumit, we have an exciting founding/senior product design role on our team and would love to chat...">💼 Founding / Senior Role</button>
          <button class="intent-pill" data-topic="Design System Audit" data-lead="Hi Sumit, we are looking to overhaul or scale our design system across web and mobile...">📐 Design System</button>
          <button class="intent-pill" data-topic="AI Interface Exploration" data-lead="Hi Sumit, we're building an AI-native product and want to explore modern user interaction patterns...">🤖 AI Interface</button>
          <button class="intent-pill" data-topic="Just Saying Hi" data-lead="Hi Sumit, love your portfolio! Just reaching out to connect and say hello...">👋 Just Saying Hi</button>
        </div>

        <form id="contactForm">
          <div class="contact-form-group">
            <label for="contactName">Your Name</label>
            <input type="text" id="contactName" class="contact-input" placeholder="e.g. Elena Rostova" required />
          </div>

          <div class="contact-form-group">
            <label for="contactEmail">Your Email</label>
            <input type="email" id="contactEmail" class="contact-input" placeholder="name@company.com" required />
          </div>

          <div class="contact-form-group">
            <label for="contactMsg">Message</label>
            <textarea id="contactMsg" class="contact-textarea" placeholder="Tell me a bit about your product, timeline, or idea...">Hi Sumit, I'm working on a zero-to-one product and would love your product design expertise on...</textarea>
          </div>

          <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:24px;">
            <button type="submit" class="btn btn-primary" id="sendBtn">
              <span>Send Message</span>
            </button>
            <a href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=sumitraiworks@gmail.com&amp;su=Product%20Collaboration%20with%20Sumit" target="_blank" rel="noopener" class="btn btn-secondary" title="Open Gmail in web browser">
              <span>Open in Gmail ↗</span>
            </a>
          </div>
        </form>
      </div>

      <!-- Sidebar: Live Delhi Time, Turnaround, Direct Info -->
      <div class="contact-sidebar-card">
        
        <!-- Live Time Box -->
        <div class="sidebar-box">
          <div class="eyebrow" style="margin-bottom:4px;"><span class="dot"></span> Local Time Widget</div>
          <h3>📍 New Delhi, India</h3>
          <p style="font-size:13px; color:var(--ink-soft);">
            Standard Time (IST &middot; UTC +5:30). Synchronized with active studio hours:
          </p>
          <div class="live-time-display">
            <span class="live-time-val" id="delhiLiveClockVal">--:-- -- IST</span>
          </div>
          <p style="font-size:12px; color:var(--ink-faint); margin-top:4px;">
            Average response time: <strong>&lt; 24 hours</strong> on weekdays.
          </p>
        </div>

        <!-- Direct Email Card -->
        <div class="sidebar-box">
          <div class="eyebrow" style="margin-bottom:4px;"><span class="dot"></span> Direct Contact</div>
          <h3>Direct Email</h3>
          <p style="font-size:14px; font-weight:700; color:var(--ink); margin-bottom:8px;">
            sumitraiworks@gmail.com
          </p>
          <button class="btn btn-secondary btn-sm" id="sidebarCopyEmail" style="width:100%; justify-content:center;">
            <span>📋 Copy Email Address</span>
          </button>
        </div>

        <!-- Professional Profiles -->
        <div class="sidebar-box">
          <div class="eyebrow" style="margin-bottom:4px;"><span class="dot"></span> Digital Presence</div>
          <h3>Connect &amp; Follow</h3>
          <div style="display:flex; flex-direction:column; gap:10px; margin-top:12px; font-size:13.5px; font-weight:600;">
            <a href="https://www.linkedin.com/in/isumitrai/" target="_blank" rel="noopener" style="display:flex; align-items:center; justify-content:space-between; color:var(--ink);">
              <span>LinkedIn</span>
              <span style="color:var(--accent);">&nearr;</span>
            </a>
            <a href="https://x.com/isumitrai" target="_blank" rel="noopener" style="display:flex; align-items:center; justify-content:space-between; color:var(--ink);">
              <span>X (formerly Twitter)</span>
              <span style="color:var(--accent);">&nearr;</span>
            </a>
            <a href="https://www.instagram.com/isumitrai/" target="_blank" rel="noopener" style="display:flex; align-items:center; justify-content:space-between; color:var(--ink);">
              <span>Instagram</span>
              <span style="color:var(--accent);">&nearr;</span>
            </a>
            <a href="https://www.raimagedesign.com" target="_blank" rel="noopener" style="display:flex; align-items:center; justify-content:space-between; color:var(--ink);">
              <span>Raimage Design Studio</span>
              <span style="color:var(--accent);">&nearr;</span>
            </a>
          </div>
        </div>

      </div>

    </div>

  </div>
</main>
"""

    contact_js = """
  // Intent Pills Dynamic Tailoring
  const pills = document.querySelectorAll('#intentPills .intent-pill');
  const msgField = document.getElementById('contactMsg');
  let currentTopic = "0-to-1 Product Design";

  pills.forEach(pill => {
    pill.addEventListener('click', (e) => {
      e.preventDefault();
      pills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      currentTopic = pill.dataset.topic;
      if (msgField) msgField.value = pill.dataset.lead;
    });
  });

  // Handle Form Submission -> mailto link
  const form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('contactName').value.trim();
      const email = document.getElementById('contactEmail').value.trim();
      const msg = document.getElementById('contactMsg').value.trim();

      const subject = encodeURIComponent(`[${currentTopic}] From ${name}`);
      const body = encodeURIComponent(`Name: ${name}\nEmail: ${email}\nTopic: ${currentTopic}\n\nMessage:\n${msg}`);
      window.location.href = `mailto:sumitraiworks@gmail.com?subject=${subject}&body=${body}`;
    });
  }

  // Sidebar Copy Email
  const sbCopy = document.getElementById('sidebarCopyEmail');
  if (sbCopy) {
    sbCopy.addEventListener('click', (e) => {
      e.preventDefault();
      navigator.clipboard.writeText('sumitraiworks@gmail.com').then(() => {
        sbCopy.innerHTML = '<span>&check; Copied to Clipboard!</span>';
        setTimeout(() => {
          sbCopy.innerHTML = '<span>📋 Copy Email Address</span>';
        }, 2200);
      });
    });
  }
"""

    return get_head("Contact — Sumit Rai", "contact") + get_nav("contact") + content + footer_html + f"<script>\n{global_js}\n{contact_js}\n</script>\n</body>\n</html>"


# -------------------------------------------------------------
# Generate All Pages
# -------------------------------------------------------------
def main():
    pages = {
        "index.html": build_index(),
        "projects.html": build_projects(),
        "about.html": build_about(),
        "resume.html": build_resume(),
        "playground.html": build_playground(),
        "contact.html": build_contact()
    }

    for filename, html in pages.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {filename} successfully ({len(html)} bytes)")

if __name__ == "__main__":
    main()
