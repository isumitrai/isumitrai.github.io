#!/usr/bin/env python3
"""
Master Page Generator for Sumit Rai Portfolio — Enhanced Edition
Fulfills all requirements:
1. Ultra-clean typography, generous whitespace, inspired by shahimim.com + modern product design.
2. Experience: 8+ years in product design and 12+ years total design craft.
3. Signature pop color: Electric International Orange (#FF5500 / #FF661A).
4. Uniform Navigation: Logo, Work [W], About [A], Resume [R], Resources [B], Playground [P], Contact [C].
5. Uniform Audited Footer: Live status dot, New Delhi IST clock, direct email with copy toast, quick links, credits.
6. New Dedicated Curated Resources Page (resources.html) with customizable Amazon links.
7. Clean Homepage: Zero divider duplicity, independent Brands and Tools sections.
8. Global Keyboard Navigation: W, A, R, B, P, C, Esc.
"""

import os
import json
import html

# -------------------------------------------------------------
# Projects Database with structured case studies
# -------------------------------------------------------------
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

# -------------------------------------------------------------
# Client Brands List
# -------------------------------------------------------------
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
# 18 Real Tool Images (assets/src/tools01.jpg to tools18.jpg)
# -------------------------------------------------------------
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

# -------------------------------------------------------------
# Curated Resources List (Books, Systems & Design Architecture)
# Update with your own Amazon referral/affiliate links anytime!
# -------------------------------------------------------------
RESOURCES = [
    {
        "id": "res-1",
        "title": "Refactoring UI",
        "author": "Adam Wathan & Steve Schoger",
        "category": "Design Craft",
        "format": "Digital & Hardcover",
        "desc": "The most pragmatic guide to designing clean, high-conversion interfaces from a developer and designer perspective.",
        "takeaway": "Design with visual hierarchy and intentional spacing before decorative chrome.",
        "link": "https://www.amazon.com/dp/B08M3S6W8R"
    },
    {
        "id": "res-2",
        "title": "The Design of Everyday Things",
        "author": "Don Norman",
        "category": "Product Strategy",
        "format": "Classic Hardcover",
        "desc": "The definitive bible on cognitive ergonomics, affordances, signifiers, and designing products that humans intuitively understand.",
        "takeaway": "When users fail, it is not user error — it is faulty interface design.",
        "link": "https://www.amazon.com/dp/0465050654"
    },
    {
        "id": "res-3",
        "title": "The Elements of Typographic Style",
        "author": "Robert Bringhurst",
        "category": "Design Craft",
        "format": "Reference Book",
        "desc": "Widely revered as the definitive text on typographic craft, rhythm, proportional scales, and the architecture of the printed page.",
        "takeaway": "Typography exists to honor content and guide human comprehension.",
        "link": "https://www.amazon.com/dp/0881792128"
    },
    {
        "id": "res-4",
        "title": "A Philosophy of Software Design",
        "author": "John Ousterhout",
        "category": "Systems & Tech",
        "format": "Technical Book",
        "desc": "A masterclass on managing system complexity, modular interfaces, and why shallow modules ruin systems.",
        "takeaway": "Modules should be deep: simple interfaces hiding profound internal power.",
        "link": "https://www.amazon.com/dp/1732102201"
    },
    {
        "id": "res-5",
        "title": "Universal Principles of Design",
        "author": "William Lidwell, Kritina Holden, Jill Butler",
        "category": "Design Craft",
        "format": "Visual Reference",
        "desc": "An authoritative encyclopedia of 125 cognitive, perceptual, and structural laws governing human interaction.",
        "takeaway": "Master Fitts' Law, Hick's Law, and progressive disclosure to reduce cognitive load.",
        "link": "https://www.amazon.com/dp/1592535879"
    },
    {
        "id": "res-6",
        "title": "Shape Up: Stop Running in Circles and Ship Work That Matters",
        "author": "Ryan Singer (Basecamp)",
        "category": "Product Strategy",
        "format": "Product Methodology",
        "desc": "A revolutionary framework for product teams: fixed time, variable scope, 6-week cycles, and building with shaped appetites.",
        "takeaway": "Never start building until problems are shaped with clear boundaries.",
        "link": "https://www.amazon.com/dp/B081N4R3G9"
    },
    {
        "id": "res-7",
        "title": "Inspired: How to Create Tech Products Customers Love",
        "author": "Marty Cagan",
        "category": "Product Strategy",
        "format": "Management Guide",
        "desc": "The gold standard for product discovery, continuous customer validation, and building empowered product teams.",
        "takeaway": "Validate value, usability, feasibility, and viability before writing code.",
        "link": "https://www.amazon.com/dp/1119387507"
    },
    {
        "id": "res-8",
        "title": "Designing Data-Intensive Applications",
        "author": "Martin Kleppmann",
        "category": "Systems & Tech",
        "format": "Engineering Architecture",
        "desc": "The definitive exploration of storage engines, distributed consensus, data models, and scalable systems reliability.",
        "takeaway": "A designer who understands backend latency and data models designs 10x better products.",
        "link": "https://www.amazon.com/dp/1449373321"
    },
    {
        "id": "res-9",
        "title": "Grid Systems in Graphic Design",
        "author": "Josef Müller-Brockmann",
        "category": "Design Craft",
        "format": "Classic Monograph",
        "desc": "The Swiss design masterwork outlining mathematical grid systems for layout, typography, and architectural coherence.",
        "takeaway": "The grid is a structural aid, not a straightjacket — it creates rhythm and order.",
        "link": "https://www.amazon.com/dp/3721201450"
    },
    {
        "id": "res-10",
        "title": "Show Your Work!",
        "author": "Austin Kleon",
        "category": "Mindset & Craft",
        "format": "Illustrated Essay",
        "desc": "A punchy guide to working in public, building a digital garden, and sharing your creative process openly.",
        "takeaway": "Become a documentarian of what you do every day; generosity builds lasting influence.",
        "link": "https://www.amazon.com/dp/076117897X"
    },
    {
        "id": "res-11",
        "title": "A Pattern Language",
        "author": "Christopher Alexander",
        "category": "Systems & Tech",
        "format": "Architectural Classic",
        "desc": "The seminal architectural philosophy that directly inspired object-oriented programming, design systems, and modular components.",
        "takeaway": "Reusable patterns solve recurring spatial and informational tensions.",
        "link": "https://www.amazon.com/dp/0195019199"
    },
    {
        "id": "res-12",
        "title": "Creativity, Inc.",
        "author": "Ed Catmull & Amy Wallace",
        "category": "Mindset & Craft",
        "format": "Hardcover Memoir",
        "desc": "The Pixar co-founder's masterclass on creative culture, candid feedback (Braintrust), and protecting early fragile ideas.",
        "takeaway": "Early drafts are never great; psychological safety allows teams to turn raw ideas into masterpieces.",
        "link": "https://www.amazon.com/dp/0812993015"
    }
]

# -------------------------------------------------------------
# Common Head, Nav, Footer, and Global JS
# -------------------------------------------------------------
def get_head(title="Sumit Rai — Senior Product Designer | AI Builder", active_page="index"):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="Sumit Rai — Senior Product Designer &amp; AI Builder with 8+ years of product design and 12+ years of overall design craft across SaaS, AI, EdTech, FinTech, and consumer platforms." />
  <meta name="author" content="Sumit Rai" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
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

    <nav class="nav-tabs" id="navTabs" aria-label="Main Navigation">
      <a href="projects.html" class="{'active' if active_page == 'projects' else ''}">Work <span class="nav-key">[W]</span></a>
      <a href="about.html" class="{'active' if active_page == 'about' else ''}">About <span class="nav-key">[A]</span></a>
      <a href="resume.html" class="{'active' if active_page == 'resume' else ''}">Resume <span class="nav-key">[R]</span></a>
      <a href="resources.html" class="{'active' if active_page == 'resources' else ''}">Resources <span class="nav-key">[B]</span></a>
      <a href="playground.html" class="{'active' if active_page == 'playground' else ''}">Playground <span class="nav-key">[P]</span></a>
      <a href="contact.html" class="{'active' if active_page == 'contact' else ''}">Contact <span class="nav-key">[C]</span></a>
    </nav>

    <div class="nav-right-actions">
      <button class="nav-action-pill" id="soundToggleBtn" aria-label="Toggle haptic sounds" title="Toggle audio feedback">
        <span id="soundIcon">🔊</span>
        <span id="soundLabel" class="sound-label-text">Sound</span>
      </button>
      <button class="nav-action-pill" id="cmdPaletteTrigger" aria-label="Quick navigation (Cmd+K)" title="Quick Command Palette (Cmd+K)">
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
      <a href="index.html" class="{'active' if active_page == 'index' else ''}">Home <span class="nav-key">[Esc]</span></a>
      <a href="projects.html" class="{'active' if active_page == 'projects' else ''}">Work <span class="nav-key">[W]</span></a>
      <a href="about.html" class="{'active' if active_page == 'about' else ''}">About <span class="nav-key">[A]</span></a>
      <a href="resume.html" class="{'active' if active_page == 'resume' else ''}">Resume <span class="nav-key">[R]</span></a>
      <a href="resources.html" class="{'active' if active_page == 'resources' else ''}">Resources <span class="nav-key">[B]</span></a>
      <a href="playground.html" class="{'active' if active_page == 'playground' else ''}">Playground <span class="nav-key">[P]</span></a>
      <a href="contact.html" class="{'active' if active_page == 'contact' else ''}">Contact <span class="nav-key">[C]</span></a>
    </nav>
  </div>
</header>

<button class="theme-toggle-floating" id="themeToggle" aria-label="Toggle dark mode" title="Toggle Dark / Light Mode">
  <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
  <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
</button>
"""

footer_html = """
<footer class="site-footer" id="siteFooter">
  <div class="footer-inner">
    
    <!-- Top status bar -->
    <div class="footer-top-row">
      <div class="footer-status-tag">
        <span class="live-dot"></span>
        <span>Available for select product leadership &amp; design advisory</span>
      </div>
      <div class="footer-clock-box" id="delhiClockWrap">
        <span class="live-dot"></span>
        <span>New Delhi, India &middot; <strong id="liveClockText">--:-- -- IST</strong></span>
      </div>
    </div>

    <!-- Main hero call to action -->
    <div class="footer-hero-cta">
      <h2 class="footer-tagline">Let's build something thoughtful together.</h2>
      <p class="footer-sublead">Always open to high-impact products, early-stage ventures, and ambitious design challenges.</p>
      
      <div class="footer-email-box">
        <div class="footer-email-pill">
          <a class="pill-left" href="mailto:sumitraiworks@gmail.com" title="Send email to Sumit Rai">
            <span class="email-text">sumitraiworks@gmail.com</span>
            <span class="email-arrow">&nearr;</span>
          </a>
          <button class="copy-btn" id="copyEmailBtn" aria-label="Copy email address" title="Copy email address">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span class="copy-toast">Copied!</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Bottom navigation and meta -->
    <div class="footer-bottom-nav">
      <div class="footer-brand-side">
        <span class="footer-mark">SR</span>
        <span class="footer-name">Sumit Rai</span>
        <span class="footer-sep">&middot;</span>
        <span class="footer-exp-text">8+ years product design &middot; 12+ years design craft</span>
      </div>

      <div class="footer-links-group">
        <div class="flinks-nav">
          <a href="projects.html">Work <span class="nav-key">[W]</span></a>
          <a href="about.html">About <span class="nav-key">[A]</span></a>
          <a href="resume.html">Resume <span class="nav-key">[R]</span></a>
          <a href="resources.html">Resources <span class="nav-key">[B]</span></a>
          <a href="playground.html">Playground <span class="nav-key">[P]</span></a>
          <a href="contact.html">Contact <span class="nav-key">[C]</span></a>
        </div>

        <div class="flinks-social">
          <a href="https://www.linkedin.com/in/isumitrai/" target="_blank" rel="noopener">LinkedIn <span class="shahi-arrow">&nearr;</span></a>
          <a href="https://x.com/isumitrai" target="_blank" rel="noopener">X <span class="shahi-arrow">&nearr;</span></a>
          <a href="https://www.instagram.com/isumitrai/" target="_blank" rel="noopener">Instagram <span class="shahi-arrow">&nearr;</span></a>
          <a href="assets/Sumit_Rai_Resume.pdf" download>Resume PDF <span class="shahi-arrow">&darr;</span></a>
        </div>
      </div>
    </div>

    <div class="footer-credit-row">
      <span>&copy; 2026 Sumit Rai. All rights reserved.</span>
      <span>Designed with restraint &middot; Built for craft</span>
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
      <a href="resources.html" class="cmd-item">
        <span class="item-left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"/><path d="M6 6h10"/><path d="M6 10h10"/></svg>
          <span>Curated Resources (Books &amp; Tools)</span>
        </span>
        <span class="cmd-shortcut">B</span>
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
    if (e.target.closest('a, button, .proj-card, .tool-tile, .resource-card, .pg-card-rich')) {
      AudioEngine.playTick(780, 0.028);
    }
  });

  // 2. Real-time New Delhi (IST) Clock
  function updateDelhiClock(){
    const textEl = document.getElementById('liveClockText');
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

  // 4. Scroll Header — add scrolled class for backdrop effect
  const header = document.getElementById('siteHeader');
  window.addEventListener('scroll', function(){
    if (header) {
      header.classList.toggle('nav-scrolled', window.scrollY > 40);
    }
  }, { passive: true });

  // 5. Mobile Nav Toggle (hamburger)
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

  // 6. Copy Email with Toast & Audio
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

  // 8. Global Keyboard Shortcuts Navigation (inspired by shahimim.com)
  document.addEventListener('keydown', function(e){
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (cmdModal && cmdModal.classList.contains('active')) {
        closeCmd();
      } else {
        openCmd();
      }
      return;
    }

    if (cmdModal && cmdModal.classList.contains('active')) {
      if (e.key === 'Escape') {
        e.preventDefault();
        closeCmd();
      }
      return;
    }

    // Do not trigger navigation when typing in inputs or holding modifier keys
    const tag = (e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || tag === 'select' || e.target.isContentEditable) {
      return;
    }
    if (e.metaKey || e.ctrlKey || e.altKey) {
      return;
    }

    const key = e.key.toLowerCase();
    if (key === 'w') {
      AudioEngine.playTick(820, 0.03);
      window.location.href = 'projects.html';
    } else if (key === 'a') {
      AudioEngine.playTick(820, 0.03);
      window.location.href = 'about.html';
    } else if (key === 'r') {
      AudioEngine.playTick(820, 0.03);
      window.location.href = 'resume.html';
    } else if (key === 'b') {
      AudioEngine.playTick(820, 0.03);
      window.location.href = 'resources.html';
    } else if (key === 'p') {
      AudioEngine.playTick(820, 0.03);
      window.location.href = 'playground.html';
    } else if (key === 'c') {
      AudioEngine.playTick(820, 0.03);
      window.location.href = 'contact.html';
    } else if (e.key === 'Escape') {
      AudioEngine.playTick(820, 0.03);
      window.location.href = 'index.html';
    }
  });
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
            <span class="proj-view-link">View Case Study <span class="shahi-arrow">&nearr;</span></span>
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
        <div class="brand-item-clean" title="{b['name']}">
          <img src="{b['img']}" alt="{b['name']}" loading="lazy" />
        </div>
"""

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
        Sumit Rai
      </h1>

      <p class="hero-statement">Product Designer &amp; AI Builder</p>
      
      <p class="hero-description">
        I design products, build experiences and explore what's next. Senior Product Designer with 8+ years crafting digital products across SaaS, AI, EdTech, and consumer platforms.
      </p>

      <div class="cta-row">
        <a href="#work" class="btn btn-primary">Selected Work <span class="btn-key">[W]</span></a>
        <a href="about.html" class="btn btn-secondary">About Me <span class="btn-key">[A]</span></a>
        <a href="resources.html" class="btn btn-secondary">Curated Resources <span class="btn-key">[B]</span></a>
        <a href="contact.html" class="btn btn-secondary">Get in Touch <span class="btn-key">[C]</span></a>
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
        <a href="projects.html" class="section-header-link">All Work <span class="shahi-arrow">&nearr;</span></a>
      </div>

      <div class="proj-grid">
        {projects_cards_html}
      </div>

      <div class="see-all-wrap">
        <a href="projects.html" class="btn btn-secondary">See All Work <span class="btn-key">[W]</span> &rarr;</a>
      </div>
    </section>

    <!-- SECTION 03 — MY APPROACH -->
    <section class="approach-section">
      <div class="approach-quote-box">
        <span class="eyebrow"><span class="dot"></span> Design Philosophy</span>
        <h2>&ldquo;Good design starts with understanding.&rdquo;</h2>
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
          <span class="approach-num">03 / SHIP</span>
          <h3>Ship with Purpose</h3>
          <p>Build scalable design systems, partner tightly with engineering, and iterate toward measurable business clarity.</p>
        </div>
      </div>
    </section>

    <!-- SECTION 04 — BENTO BOX SHOWCASE (Inspired by shahimim.com) -->
    <section class="bento-section" id="bento">
      <div class="section-header-row">
        <div class="section-title-wrap">
          <span class="eyebrow"><span class="dot"></span> Craft &amp; Systems</span>
          <h2>At a Glance &mdash; Craft, Stack &amp; Explorations</h2>
          <p>A multi-disciplinary blend of 8+ years product design leadership, 12+ years total design craft, code prototypes, and curated knowledge.</p>
        </div>
        <a href="about.html" class="section-header-link">About My Journey <span class="shahi-arrow">&nearr;</span></a>
      </div>

      <div class="bento-grid">
        <!-- Bento 1: Primary Spotlight (Span 2) -->
        <a href="about.html" class="bento-card span-2" aria-label="Learn more about Sumit Rai's background and experience">
          <div>
            <div class="bento-top-row">
              <span class="bento-badge accent-badge"><span class="live-dot"></span> Senior Product Designer</span>
              <span class="bento-arrow-btn"><span class="shahi-arrow">&nearr;</span></span>
            </div>
            <div class="bento-body">
              <h3 class="bento-title">Designing Intuitive Systems &amp; High-Impact Products Since 2014</h3>
              <p class="bento-desc">
                8+ years leading end-to-end UX/UI product strategy and 12+ years of design craft across visual systems, interactive prototypes, and scalable token architectures. Balancing business revenue with human delight.
              </p>
            </div>
            <div class="bento-stats-row">
              <div>
                <span class="bento-stat-num">8+</span>
                <span class="bento-stat-label">Years in Product</span>
              </div>
              <div style="border-left:1px solid var(--line); padding-left:18px;">
                <span class="bento-stat-num">12+</span>
                <span class="bento-stat-label">Years Total Craft</span>
              </div>
              <div style="border-left:1px solid var(--line); padding-left:18px;">
                <span class="bento-stat-num">6+</span>
                <span class="bento-stat-label">Industries Shipped</span>
              </div>
            </div>
          </div>
          <div class="bento-footer">
            <span class="bento-link-text">Read background &amp; design journey <span class="shahi-arrow">&rarr;</span></span>
            <span class="bento-tag pop">[A] About</span>
          </div>
        </a>

        <!-- Bento 2: Raimage Studio Lab (Span 1) -->
        <a href="playground.html" class="bento-card" aria-label="Explore Raimage Studio Lab experiments">
          <div>
            <div class="bento-top-row">
              <span class="bento-badge">Raimage Lab</span>
              <span class="bento-arrow-btn"><span class="shahi-arrow">&nearr;</span></span>
            </div>
            <div class="bento-body">
              <h3 class="bento-title">AI-Native &amp; Code Prototypes</h3>
              <p class="bento-desc">
                Bridging Figma and production with Claude, Gemini APIs, HTML5 Canvas, Web Audio, and generative UI micro-tools.
              </p>
            </div>
            <div class="bento-tags">
              <span class="bento-tag pop">GenAI</span>
              <span class="bento-tag">Canvas</span>
              <span class="bento-tag">Web Audio</span>
              <span class="bento-tag">Micro-tools</span>
            </div>
          </div>
          <div class="bento-footer">
            <span class="bento-link-text">Explore interactive lab <span class="shahi-arrow">&rarr;</span></span>
            <span class="bento-tag">[P] Lab</span>
          </div>
        </a>

        <!-- Bento 3: Curated Resources / Books (Span 1) -->
        <a href="resources.html" class="bento-card" aria-label="View curated books and resources">
          <div>
            <div class="bento-top-row">
              <span class="bento-badge">Reading Shelf</span>
              <span class="bento-arrow-btn"><span class="shahi-arrow">&nearr;</span></span>
            </div>
            <div class="bento-body">
              <h3 class="bento-title">12+ Curated Books</h3>
              <p class="bento-desc">
                Handpicked texts on systems design, typography, cognitive psychology, and software architecture with personal takeaways.
              </p>
            </div>
            <div class="bento-tags">
              <span class="bento-tag pop">12 Books</span>
              <span class="bento-tag">Takeaways</span>
              <span class="bento-tag">Amazon Links</span>
            </div>
          </div>
          <div class="bento-footer">
            <span class="bento-link-text">Browse recommended reads <span class="shahi-arrow">&rarr;</span></span>
            <span class="bento-tag">[B] Books</span>
          </div>
        </a>

        <!-- Bento 4: Philosophy & Architecture (Span 1) -->
        <a href="projects.html" class="bento-card" aria-label="View projects and architecture">
          <div>
            <div class="bento-top-row">
              <span class="bento-badge">Philosophy</span>
              <span class="bento-arrow-btn"><span class="shahi-arrow">&nearr;</span></span>
            </div>
            <div class="bento-body">
              <h3 class="bento-title">Understand &middot; Connect &middot; Ship</h3>
              <p class="bento-desc">
                Deep understanding of business goals and user workflows. Scalable design token architectures that engineers love shipping.
              </p>
            </div>
            <div class="bento-tags">
              <span class="bento-tag pop">Tokens</span>
              <span class="bento-tag">Figma</span>
              <span class="bento-tag">WCAG AAA</span>
            </div>
          </div>
          <div class="bento-footer">
            <span class="bento-link-text">View project case studies <span class="shahi-arrow">&rarr;</span></span>
            <span class="bento-tag">[W] Work</span>
          </div>
        </a>

        <!-- Bento 5: Location & Availability (Span 1) -->
        <a href="contact.html" class="bento-card" aria-label="Contact Sumit Rai">
          <div>
            <div class="bento-top-row">
              <span class="bento-badge accent-badge"><span class="live-dot"></span> Available</span>
              <span class="bento-arrow-btn"><span class="shahi-arrow">&nearr;</span></span>
            </div>
            <div class="bento-body">
              <h3 class="bento-title">New Delhi, India</h3>
              <p class="bento-desc">
                Available for select senior product design consulting, design systems advisory, and high-impact full-time roles worldwide.
              </p>
            </div>
            <div class="bento-tags">
              <span class="bento-tag pop">IST (UTC +5:30)</span>
              <span class="bento-tag">Remote</span>
              <span class="bento-tag">Hybrid</span>
            </div>
          </div>
          <div class="bento-footer">
            <span class="bento-link-text">Start a conversation <span class="shahi-arrow">&rarr;</span></span>
            <span class="bento-tag">[C] Contact</span>
          </div>
        </a>
      </div>
    </section>

    <!-- SECTION 05 — SELECTED EXPERIENCE -->
    <section class="experience-section">
      <div class="section-header-row">
        <div class="section-title-wrap">
          <span class="eyebrow"><span class="dot"></span> Professional Journey</span>
          <h2>Selected Experience</h2>
          <p>Roles and founding product work across high-impact design studios and tech teams.</p>
        </div>
        <a href="resume.html" class="section-header-link">View Full Resume <span class="btn-key">[R]</span> <span class="shahi-arrow">&nearr;</span></a>
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
    </section>

    <!-- SECTION 06 — BRANDS SECTION (CLEAN INDEPENDENT CONTAINER, ZERO DUPLICATE BORDERS) -->
    <section class="brands-section">
      <div class="section-header-row">
        <div class="section-title-wrap">
          <span class="eyebrow"><span class="dot"></span> Client &amp; Brand Partners</span>
          <h2>Brands I've Helped Shape</h2>
          <p>Selected ventures, institutions, and brand ecosystems shaped across product and visual design.</p>
        </div>
      </div>
      <div class="brands-wrap">
        <div class="brands-grid-clean">
          {brands_html}
        </div>
      </div>
    </section>

    <!-- SECTION 07 — TOOLKIT & ENVIRONMENT -->
    <section class="tools-section">
      <div class="section-header-row">
        <div class="section-title-wrap">
          <span class="eyebrow"><span class="dot"></span> Toolkit &amp; Environment</span>
          <h2>Tools I Use to Think, Design &amp; Build</h2>
          <p>Everyday software, platforms, and AI workflows powering high-velocity product delivery.</p>
        </div>
      </div>
      <div class="tools-wrap">
        <div class="tools-grid-img">
          {tools_html}
        </div>
      </div>
    </section>

    <!-- SECTION 08 — CONTACT CTA -->
    <section class="contact-cta-section">
      <span class="eyebrow"><span class="dot"></span> Let's Connect</span>
      <h2>Have something interesting in mind?</h2>
      <p>I'm always open to meaningful conversations, interesting ideas and opportunities to build something thoughtful.</p>
      <div class="cta-btns">
        <a href="contact.html" class="btn btn-primary">Get in Touch <span class="btn-key">[C]</span> &rarr;</a>
        <a href="mailto:sumitraiworks@gmail.com" class="btn btn-secondary">Email Sumit</a>
      </div>
    </section>

  </div>
</main>
"""
    return get_head("Sumit Rai — Senior Product Designer | AI Builder", "index") + get_nav("index") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"

# -------------------------------------------------------------
# PAGE 2: PROJECTS.HTML (CASE STUDIES ARCHIVE & DETAILS)
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
            <span class="proj-view-link">Case Study <span class="shahi-arrow">&nearr;</span></span>
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

      <!-- Meta Card -->
      <article class="case-meta-card">
        <div class="case-title-row">
          <h1 id="caseTitle">EduManage</h1>
          <p class="case-tagline" id="caseTagline">A modern institution dashboard shaped around academic operations.</p>
        </div>
        <div class="case-meta-grid">
          <div class="case-meta-item">
            <span class="label">Role</span>
            <span class="val" id="caseRole">Senior Product Designer</span>
          </div>
          <div class="case-meta-item">
            <span class="label">Timeline</span>
            <span class="val" id="caseTimeline">2024 — 2026</span>
          </div>
          <div class="case-meta-item">
            <span class="label">Focus</span>
            <span class="val" id="caseFocus">SaaS Dashboard · CMS</span>
          </div>
          <div class="case-meta-item">
            <span class="label">Impact</span>
            <span class="val" id="caseImpact">High-clarity workflows</span>
          </div>
        </div>
      </article>

      <!-- Hero Visual -->
      <div class="case-hero-image">
        <img id="caseHeroImg" src="./assets/proj_edumanage.png" alt="Case Study hero" />
      </div>

      <!-- Editorial Narrative Flow -->
      <div class="case-body-flow">
        <div class="case-section-box">
          <h3><span class="sec-dot"></span> The Overview</h3>
          <p id="caseOverviewText">Enterprise-grade institution management dashboard engineered for operational clarity.</p>
        </div>

        <div class="case-section-box">
          <h3><span class="sec-dot"></span> The Challenge</h3>
          <p id="caseChallengeText">Educational institutions traditionally rely on disconnected legacy tools and disparate spreadsheets.</p>
        </div>

        <div class="case-section-box">
          <h3><span class="sec-dot"></span> My Role &amp; Responsibilities</h3>
          <p id="caseRoleText">I directed end-to-end user research, information architecture, design systems, and clickable prototypes.</p>
        </div>

        <div class="case-section-box">
          <h3><span class="sec-dot"></span> Approach &amp; Process</h3>
          <p id="caseApproachText">I mapped administrative user journeys to uncover recurring bottlenecks and structured role-based modular layouts.</p>
        </div>

        <div class="case-section-box">
          <h3><span class="sec-dot"></span> The Solution</h3>
          <p id="caseSolutionText">Delivered an actionable multi-tenant dashboard with automated telemetry and multi-tiered permission management.</p>
        </div>

        <div class="case-section-box">
          <h3><span class="sec-dot"></span> Outcomes &amp; Impact</h3>
          <p id="caseOutcomeText">Significantly reduced task completion times and established a unified design system adopted across portals.</p>
        </div>
      </div>

      <!-- Bottom Prev / Next Nav -->
      <nav class="case-nav" aria-label="Case Study Navigation">
        <button class="case-nav-btn prev" id="prevCaseBtn">
          <span class="nav-eyebrow">&larr; Previous Project</span>
          <span class="nav-proj-name" id="prevCaseTitle">Community</span>
        </button>
        <button class="case-nav-btn next" id="nextCaseBtn">
          <span class="nav-eyebrow">Next Project &rarr;</span>
          <span class="nav-proj-name" id="nextCaseTitle">Quayo Basket</span>
        </button>
      </nav>
    </div>

  </div>
</main>
"""

    projects_page_js = f"""
  const allProjects = {projects_json};
  const listView = document.getElementById('projectsListView');
  const caseView = document.getElementById('caseStudyView');
  const backBtn = document.getElementById('backToProjectsBtn');
  const filterTabs = document.querySelectorAll('#projectFilterTabs .filter-btn');

  // Filter functionality
  filterTabs.forEach(btn => {{
    btn.addEventListener('click', () => {{
      filterTabs.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.dataset.filter;
      const cards = document.querySelectorAll('#projectsArchiveGrid .proj-card');
      
      cards.forEach((card, idx) => {{
        const p = allProjects[idx];
        if (cat === 'all') {{
          card.style.display = 'flex';
        }} else if (cat === 'saas' && p.category.toLowerCase().includes('saas')) {{
          card.style.display = 'flex';
        }} else if (cat === 'mobile' && p.category.toLowerCase().includes('grocery')) {{
          card.style.display = 'flex';
        }} else if (cat === 'web' && p.category.toLowerCase().includes('web')) {{
          card.style.display = 'flex';
        }} else if (cat === 'edtech' && p.category.toLowerCase().includes('edtech')) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }});
  }});

  // Open Case Study Details
  function openCaseStudy(projId) {{
    const pIndex = allProjects.findIndex(item => item.id === projId);
    if (pIndex === -1) return;
    const p = allProjects[pIndex];

    document.getElementById('caseTitle').textContent = p.title;
    document.getElementById('caseTagline').textContent = p.tagline;
    document.getElementById('caseCategoryChip').textContent = p.category;
    document.getElementById('caseRole').textContent = p.role;
    document.getElementById('caseTimeline').textContent = p.timeline;
    document.getElementById('caseFocus').textContent = p.focus_areas;
    document.getElementById('caseImpact').textContent = p.in_short;
    document.getElementById('caseHeroImg').src = p.image;
    document.getElementById('caseHeroImg').alt = p.full_title;

    document.getElementById('caseOverviewText').textContent = p.overview;
    document.getElementById('caseChallengeText').textContent = p.challenge;
    document.getElementById('caseRoleText').textContent = p.my_role;
    document.getElementById('caseApproachText').textContent = p.approach;
    document.getElementById('caseSolutionText').textContent = p.solution;
    document.getElementById('caseOutcomeText').textContent = p.outcome;

    // Prev / Next setup
    const prevIndex = (pIndex - 1 + allProjects.length) % allProjects.length;
    const nextIndex = (pIndex + 1) % allProjects.length;

    const prevP = allProjects[prevIndex];
    const nextP = allProjects[nextIndex];

    const prevBtn = document.getElementById('prevCaseBtn');
    const nextBtn = document.getElementById('nextCaseBtn');

    document.getElementById('prevCaseTitle').textContent = prevP.title;
    document.getElementById('nextCaseTitle').textContent = nextP.title;

    prevBtn.onclick = () => openCaseStudy(prevP.id);
    nextBtn.onclick = () => openCaseStudy(nextP.id);

    listView.hidden = true;
    caseView.hidden = false;
    window.location.hash = projId;
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
          Over the past 12+ years, I've journeyed from crafting brand identities and marketing collateral to architecting complex enterprise SaaS, EdTech ecosystems, and AI-native products with 8+ years dedicated to digital product design. I believe the best products balance strategic clarity with rigorous visual craftsmanship.
        </p>
        <div style="display:flex; gap:12px; margin-top:28px; flex-wrap:wrap;">
          <a href="resume.html" class="btn btn-primary">Read Resume <span class="btn-key">[R]</span></a>
          <a href="resources.html" class="btn btn-secondary">Curated Resources <span class="btn-key">[B]</span></a>
          <a href="contact.html" class="btn btn-secondary">Get in Touch <span class="btn-key">[C]</span></a>
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
        My journey into design began in 2014, immersing myself in visual hierarchy, brand consistency, and graphic design across diverse physical and digital consumer touchpoints. Working across real-world commercial constraints taught me that design is never purely aesthetic &mdash; it must communicate clearly and drive action.
      </p>
      <p>
        In 2018–2019, my focus shifted decisively toward digital product design. At Design Matra, I took ownership of complex user journeys across FinTech, HealthTech, and E-Commerce products, tackling onboarding friction, checkout drop-offs, and multi-platform consistency.
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
            <p>Crafted digital brand identities, marketing assets, and consumer interfaces across multi-channel digital touchpoints.</p>
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
        <a href="resume.html" class="btn btn-primary">Resume Page <span class="btn-key">[R]</span></a>
        <a href="assets/Sumit_Rai_Resume.pdf" download class="btn btn-secondary">Download PDF &darr;</a>
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
# PAGE 4: RESUME.HTML (STRUCTURED & PRINTABLE)
# -------------------------------------------------------------
def build_resume():
    content = f"""
<main class="page-body">
  <div class="wrap">
    
    <div class="resume-view-wrap">
      
      <!-- Top Actions Bar -->
      <div class="resume-top-bar">
        <a href="index.html" class="back-link">&larr; Back to Portfolio <span class="nav-key">[Esc]</span></a>
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
            Product Designer with 8+ years of product design experience and 12+ years of overall design craft. Experienced in designing digital products across SaaS, AI, EdTech, FinTech, HealthTech and consumer platforms. Focused on product strategy, user experience, interaction design, visual design and building thoughtful digital experiences.
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
              <span class="resume-item-role">Graphic &amp; UI Designer</span>
              <span class="resume-item-date">2015 &mdash; 2021</span>
            </div>
            <div class="resume-item-org">Kitaro Trading &middot; Consumer Goods &middot; New Delhi, India</div>
            <ul>
              <li>Designed multi-channel brand identities, packaging, and digital interfaces for consumer product lines.</li>
              <li>Produced marketing collateral, retail packaging systems, and digital promotional touchpoints.</li>
              <li>Standardized visual brand guidelines and cross-medium design asset libraries.</li>
            </ul>
          </div>
        </section>

        <!-- 3. Core Competencies -->
        <section class="resume-section">
          <h3 class="section-heading">Core Competencies</h3>
          <div class="resume-skills-block">
            <span class="resume-skills-label">Product Design:</span>
            <span class="resume-skills-val">UI/UX Design, Wireframing, Rapid Prototyping, Design Systems, Mobile Apps (iOS/Android), Web Applications, SaaS Dashboards</span>
          </div>
          <div class="resume-skills-block">
            <span class="resume-skills-label">User Experience:</span>
            <span class="resume-skills-val">User Research, Usability Testing, Information Architecture, User Flow Mapping, Interaction Design, Heuristic Evaluation</span>
          </div>
          <div class="resume-skills-block">
            <span class="resume-skills-label">Product Strategy:</span>
            <span class="resume-skills-val">Discovery &amp; Framing, Cross-Functional Collaboration, Roadmapping, Agile Workflows, Conversion Rate Optimization (CRO)</span>
          </div>
          <div class="resume-skills-block">
            <span class="resume-skills-label">Brand &amp; Visual:</span>
            <span class="resume-skills-val">Brand Identity Systems, Visual Hierarchy, Design Tokens, Typography, Graphic Design, Iconography</span>
          </div>
          <div class="resume-skills-block">
            <span class="resume-skills-label">AI &amp; Emerging Tech:</span>
            <span class="resume-skills-val">AI-Native Workflows, Interactive Code Prototyping (HTML/CSS/JS), Prompt Engineering, Generative Interface Explorations</span>
          </div>
        </section>

        <!-- 4. Tools & Technologies -->
        <section class="resume-section">
          <h3 class="section-heading">Tools &amp; Technologies</h3>
          <div class="resume-skills-block">
            <span class="resume-skills-label">Design &amp; Prototyping:</span>
            <span class="resume-skills-val">Figma, Framer, FigJam, Adobe Creative Suite (Illustrator, Photoshop, InDesign), Spline 3D</span>
          </div>
          <div class="resume-skills-block">
            <span class="resume-skills-label">Dev &amp; AI Tools:</span>
            <span class="resume-skills-val">VS Code, Cursor, GitHub, Webflow, Bolt.new, ChatGPT, Midjourney, Claude, HTML5, CSS3, JavaScript</span>
          </div>
          <div class="resume-skills-block">
            <span class="resume-skills-label">Management:</span>
            <span class="resume-skills-val">Jira, Linear, Notion, Slack, Google Workspace</span>
          </div>
        </section>

        <!-- 5. Education -->
        <section class="resume-section">
          <h3 class="section-heading">Education &amp; Credentials</h3>
          <div class="resume-item">
            <div class="resume-item-head">
              <span class="resume-item-role">Bachelor of Science (B.Sc.)</span>
              <span class="resume-item-date">2012 &mdash; 2015</span>
            </div>
            <div class="resume-item-org">University of Delhi &middot; Delhi, India</div>
          </div>
          <div class="resume-item">
            <div class="resume-item-head">
              <span class="resume-item-role">Diploma in Web &amp; Graphic Design</span>
              <span class="resume-item-date">2014 &mdash; 2015</span>
            </div>
            <div class="resume-item-org">Arena Animation &middot; Delhi, India</div>
          </div>
        </section>

      </article>

    </div>

  </div>
</main>
"""
    return get_head("Resume — Sumit Rai", "resume") + get_nav("resume") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"

# -------------------------------------------------------------
# PAGE 5: RESOURCES.HTML (CURATED BOOKS & SYSTEMS REFERENCES)
# -------------------------------------------------------------
def build_resources():
    cards_html = ""
    for r in RESOURCES:
        cards_html += f"""
      <article class="resource-card" data-category="{r['category']}">
        <div class="resource-card-header">
          <span class="resource-cat-tag">{r['category']}</span>
          <span class="resource-format-tag">{r['format']}</span>
        </div>
        <h3 class="resource-title">{r['title']}</h3>
        <div class="resource-author">{r['author']}</div>
        <p class="resource-desc">{r['desc']}</p>
        <div class="resource-takeaway">
          <strong>Key insight:</strong> {r['takeaway']}
        </div>
        <div class="resource-action-row">
          <!-- Update with your Amazon affiliate link anytime -->
          <a href="{r['link']}" target="_blank" rel="noopener" class="resource-amazon-btn" title="View {r['title']} on Amazon">
            <span>Get on Amazon</span>
            <span class="arrow shahi-arrow">&nearr;</span>
          </a>
          <span class="resource-format-tag">Curated Read</span>
        </div>
      </article>
"""

    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <!-- HERO -->
    <section class="resources-hero-block">
      <span class="eyebrow"><span class="dot"></span> Knowledge &amp; Reference</span>
      <h1>Curated Resources</h1>
      <p class="lead">
        A personal selection of foundational books, architectural frameworks, and design readings that continuously inform how I think, structure products, and build systems.
      </p>
      <div class="resources-note-pill">
        <span class="dot"></span>
        <span>Tap any book to view on Amazon &middot; Updated quarterly</span>
      </div>
    </section>

    <!-- CATEGORY FILTER TABS -->
    <div class="resources-filter-row" id="resFilterRow">
      <button class="res-filter-btn active" data-filter="all">All Reads (12)</button>
      <button class="res-filter-btn" data-filter="Design Craft">Design Craft</button>
      <button class="res-filter-btn" data-filter="Product Strategy">Product Strategy</button>
      <button class="res-filter-btn" data-filter="Systems &amp; Tech">Systems &amp; Tech</button>
      <button class="res-filter-btn" data-filter="Mindset &amp; Craft">Mindset &amp; Craft</button>
    </div>

    <!-- CARDS GRID -->
    <div class="resources-grid" id="resGrid">
      {cards_html}
    </div>

    <!-- RECOMMENDATION CTA -->
    <section class="contact-cta-section" style="margin-top:20px;">
      <span class="eyebrow"><span class="dot"></span> Have a Recommendation?</span>
      <h2>Read something exceptional recently?</h2>
      <p>I'm always expanding my reading list across AI, systems architecture, cognitive ergonomics, and design history.</p>
      <div class="cta-btns">
        <a href="contact.html" class="btn btn-primary">Share a Recommendation <span class="btn-key">[C]</span> &rarr;</a>
        <a href="mailto:sumitraiworks@gmail.com" class="btn btn-secondary">Email Sumit</a>
      </div>
    </section>

  </div>
</main>
"""

    res_js = """
  // Filter Tabs logic for Resources Page
  const filterBtns = document.querySelectorAll('#resFilterRow .res-filter-btn');
  const cards = document.querySelectorAll('#resGrid .resource-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.dataset.filter;

      cards.forEach(card => {
        if (cat === 'all' || card.dataset.category === cat) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
"""

    return get_head("Curated Resources — Sumit Rai", "resources") + get_nav("resources") + content + footer_html + f"<script>\n{global_js}\n{res_js}\n</script>\n</body>\n</html>"

# -------------------------------------------------------------
# PAGE 6: PLAYGROUND.HTML (RAIMAGE DESIGN LAB)
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
            "desc": "Architectural proportions applied to editorial typography and structural layout systems.",
            "img": "./assets/img_03.jpg"
        }
    ]

    cards_html = ""
    for it in items:
        cards_html += f"""
      <article class="pg-card-rich" data-category="{it['category']}">
        <div class="pg-preview">
          <img src="{it['img']}" alt="{it['title']}" loading="lazy" />
        </div>
        <div class="pg-meta-body">
          <div class="pg-cat-row">
            <span class="pg-tag">{it['tag']}</span>
            <span class="pg-year">{it['year']}</span>
          </div>
          <h3>{it['title']}</h3>
          <p>{it['desc']}</p>
          <div class="pg-foot">
            <span>Raimage Studio Lab</span>
            <span>&nearr;</span>
          </div>
        </div>
      </article>
"""

    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <div class="pg-hero-block">
      <span class="eyebrow"><span class="dot"></span> Raimage Design Lab</span>
      <h1>Playground &amp; Explorations</h1>
      <p>
        Uncommissioned ideas, industrial design concepts, fine art prints, and AI interface experiments from Raimage Design Studio.
      </p>
    </div>

    <!-- Filter Buttons -->
    <div class="pg-filter-row" id="pgFilterRow">
      <button class="filter-btn active" data-filter="all">All Experiments (6)</button>
      <button class="filter-btn" data-filter="Tools &amp; UI Concepts">Tools &amp; UI Concepts</button>
      <button class="filter-btn" data-filter="Industrial &amp; 3D">Industrial &amp; 3D</button>
      <button class="filter-btn" data-filter="Brand &amp; Packaging">Brand &amp; Packaging</button>
      <button class="filter-btn" data-filter="Fine Art &amp; Prints">Fine Art &amp; Prints</button>
    </div>

    <div class="pg-grid-rich" id="pgGrid">
      {cards_html}
    </div>

    <section class="contact-cta-section" style="margin-top:64px;">
      <span class="eyebrow"><span class="dot"></span> Custom Collaborations</span>
      <h2>Interested in bespoke visual or product explorations?</h2>
      <p>Let's collaborate on creative technology, experimental prototypes, or industrial product design.</p>
      <div class="cta-btns">
        <a href="contact.html" class="btn btn-primary">Start a Collaboration <span class="btn-key">[C]</span> &rarr;</a>
        <a href="mailto:sumitraiworks@gmail.com" class="btn btn-secondary">Email Sumit</a>
      </div>
    </section>

  </div>
</main>
"""

    pg_js = """
  const pgFilterBtns = document.querySelectorAll('#pgFilterRow .filter-btn');
  const pgCards = document.querySelectorAll('#pgGrid .pg-card-rich');

  pgFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      pgFilterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.dataset.filter;

      pgCards.forEach(card => {
        if (cat === 'all' || card.dataset.category === cat) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
"""

    return get_head("Playground (Lab) — Sumit Rai", "playground") + get_nav("playground") + content + footer_html + f"<script>\n{global_js}\n{pg_js}\n</script>\n</body>\n</html>"

# -------------------------------------------------------------
# PAGE 7: CONTACT.HTML (INTERACTIVE TAILORED FORM & SIDEBAR)
# -------------------------------------------------------------
def build_contact():
    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <div class="contact-hero-wrap">
      <span class="eyebrow"><span class="dot"></span> Start a Conversation</span>
      <h1>Get in Touch</h1>
      <p class="lead">
        Whether you have an upcoming product launch, early-stage design advisory, or want to discuss emerging AI workflows, I'd love to hear from you.
      </p>
    </div>

    <div class="contact-grid-layout">
      
      <!-- Left Column: Interactive Form -->
      <div class="contact-form-card">
        <label style="font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; display:block; margin-bottom:10px; color:var(--ink);">
          What would you like to discuss?
        </label>
        
        <div class="contact-intent-pills" id="intentPills">
          <button type="button" class="intent-pill active" data-topic="0-to-1 Product Design" data-lead="Hi Sumit, we are planning a zero-to-one product and need senior design leadership...">0-to-1 Product Design</button>
          <button type="button" class="intent-pill" data-topic="Design System Architecture" data-lead="Hi Sumit, we want to scale our UI component system and need your architecture expertise...">Design System</button>
          <button type="button" class="intent-pill" data-topic="AI Interface Exploration" data-lead="Hi Sumit, we are building an AI-native workflow and would love your guidance on the interface...">AI Interface / Prototype</button>
          <button type="button" class="intent-pill" data-topic="Advisory &amp; Mentorship" data-lead="Hi Sumit, I\\'d love to explore design advisory or mentorship for our team...">Design Advisory</button>
          <button type="button" class="intent-pill" data-topic="General Inquiry" data-lead="Hi Sumit, I came across your portfolio and wanted to reach out...">General Hello</button>
        </div>

        <form id="contactForm">
          <div class="contact-form-group">
            <label for="contactName">Your Name</label>
            <input type="text" id="contactName" class="contact-input" placeholder="e.g. Alex Chen" required />
          </div>

          <div class="contact-form-group">
            <label for="contactEmail">Your Email</label>
            <input type="email" id="contactEmail" class="contact-input" placeholder="e.g. alex@company.com" required />
          </div>

          <div class="contact-form-group">
            <label for="contactMsg">Message</label>
            <textarea id="contactMsg" class="contact-textarea" rows="4" required>Hi Sumit, we are planning a zero-to-one product and need senior design leadership...</textarea>
          </div>

          <button type="submit" class="btn btn-primary" style="width:100%; padding:14px; margin-top:8px;">
            <span>Send Message &rarr;</span>
          </button>
        </form>
      </div>

      <!-- Right Column: Direct Info & Delhi Time -->
      <div class="contact-sidebar-card">
        
        <div class="sidebar-box">
          <h3>Direct Contact</h3>
          <p style="margin-bottom:12px; color:var(--ink-soft);">Prefer direct email over forms? Reach out anytime:</p>
          <a href="mailto:sumitraiworks@gmail.com" style="font-family:var(--font-heading); font-size:1.15rem; font-weight:700; color:var(--accent); text-decoration:underline; text-underline-offset:3px;">
            sumitraiworks@gmail.com
          </a>
          <div style="margin-top:14px;">
            <button class="btn btn-secondary btn-sm" id="sidebarCopyEmail">
              <span>📋 Copy Email Address</span>
            </button>
          </div>
        </div>

        <div class="sidebar-box">
          <h3>Current Location &amp; Time</h3>
          <p style="color:var(--ink-soft); margin-bottom:6px;">Based in New Delhi, India &middot; Available worldwide across overlapping timezones.</p>
          <div class="live-time-display">
            <span class="live-time-val" id="delhiLiveClockVal">--:-- --</span>
            <span class="live-time-zone">IST (UTC +5:30)</span>
          </div>
          <span style="font-size:11.5px; color:var(--ink-faint);">Standard response time: within 24 hours.</span>
        </div>

        <div class="sidebar-box">
          <h3>Connect Online</h3>
          <div style="display:flex; flex-direction:column; gap:10px; margin-top:10px; font-size:13.5px;">
            <a href="https://www.linkedin.com/in/isumitrai/" target="_blank" rel="noopener" style="display:flex; align-items:center; justify-content:space-between; color:var(--ink);">
              <span>LinkedIn</span>
              <span style="color:var(--accent);">&nearr;</span>
            </a>
            <a href="https://x.com/isumitrai" target="_blank" rel="noopener" style="display:flex; align-items:center; justify-content:space-between; color:var(--ink);">
              <span>X (Twitter)</span>
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
      const body = encodeURIComponent(`Name: ${name}\\nEmail: ${email}\\nTopic: ${currentTopic}\\n\\nMessage:\\n${msg}`);
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
# Generate All Pages (7 Pages with 100% Shared Nav & Footer)
# -------------------------------------------------------------
def main():
    pages = {
        "index.html": build_index(),
        "projects.html": build_projects(),
        "about.html": build_about(),
        "resume.html": build_resume(),
        "resources.html": build_resources(),
        "playground.html": build_playground(),
        "contact.html": build_contact()
    }

    for filename, html_code in pages.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_code)
        print(f"Generated {filename} successfully ({len(html_code)} bytes)")

if __name__ == "__main__":
    main()
