#!/usr/bin/env python3
"""
Final Portfolio Generator for Sumit Rai
Addresses all user requests:
1. Nav is "Contact" [C] (NOT "Work with me").
2. "Design & Shop" is under Playground [P].
3. On inner pages, NO top navigation is shown — ONLY the clean Back button is shown (matching shahimim.com).
4. On Home page, Bento Box is placed at the bottom, matching the exact screenshot (media_1794226361464_3b0f65bc.jpg):
   - Card 1: Media card with pill "Bootstrapping a startup" and key "W"
   - Card 2: Digital garden with stacked index cards "Is the design we practice worth saving?" (0014, 26.05.26) and key "G"
   - Card 3: Writing card with confetti drawing "Stop adding confetti to your product" (12.10.25 · 8 min read) and key "B"
   - Card 4: Contact card with "Advisory & coaching", "Design mentorship", "Talks & panels" and key "C"
   - Card 5: Resources card with colourful book spines row and key "R"
5. Real works: EduManage, Quayo Basket, Musafir, Community.
6. Real experience in reverse chronological order:
   - Raimage Design (Founding Designer, 2025 — Present)
   - Edfora Infotech (Senior Product Designer, 2023 — 2025)
   - Design Matra (Product Designer, 2021 — 2023)
   - Kitaro Trading (Graphic Designer, 2012 — 2021)
7. Substack link to isumitrai.substack.com in 4-column minimal footer and writing areas.
"""

import json

PROJECTS = [
    {
        "id": "edumanage",
        "title": "EduManage",
        "full_title": "EduManage — Smart Educational Management Dashboard",
        "category": "SaaS Product · CMS",
        "year": "2026",
        "tagline": "A modern institution dashboard shaped around academic operations, content management, and day-to-day school workflows.",
        "image": "./assets/proj_edumanage.png",
        "tags": ["CMS", "Dashboard", "SaaS"],
        "client": "EduManage Inc.",
        "role": "Lead Product Designer",
        "impact": "Structured operational cards and modular data views that help modern institutions scan information quickly and act with confidence."
    },
    {
        "id": "quayo",
        "title": "Quayo Basket",
        "full_title": "Quayo Basket — Grocery App & Brand Identity System",
        "category": "Grocery App · Branding",
        "year": "2026",
        "tagline": "A grocery mobile app paired with a brand identity system for a clearer, friendlier shopping and rapid checkout experience.",
        "image": "./assets/proj_quayo.png",
        "tags": ["Mobile App", "UI/UX", "Branding"],
        "client": "Quayo Basket",
        "role": "Product & Brand Designer",
        "impact": "Recognizable retail feel across browsing, basket, and checkout moments supporting rapid product discovery and repeat ordering."
    },
    {
        "id": "musafir",
        "title": "Musafir",
        "full_title": "Musafir — Travel Marketplace Landing Page Redesign",
        "category": "Travel · Marketplace",
        "year": "2026",
        "tagline": "A travel marketplace landing page redesigned for stronger conversion paths, destination storytelling, and clearer decision-making.",
        "image": "./assets/proj_musafir.png",
        "tags": ["Travel", "Web Design", "Marketplace"],
        "client": "Musafir Travel",
        "role": "Lead UX / UI Designer",
        "impact": "Helps visitors understand travel packages faster, comparing flight/hotel offers with minimal friction and higher booking intent."
    },
    {
        "id": "community",
        "title": "Community",
        "full_title": "Community — Student Learning Hub & Engagement Platform",
        "category": "Community Platform · EdTech",
        "year": "2026",
        "tagline": "A student learning hub built around peer growth, shared course resources, and platform-led learner engagement.",
        "image": "./assets/proj_community.png",
        "tags": ["EdTech", "Platform", "Community"],
        "client": "Community EdTech",
        "role": "Senior Product Designer",
        "impact": "Balances content discovery, peer collaboration groups, and a simple platform architecture that supports active daily student participation."
    }
]

COMPANIES = [
    {
        "name": "Raimage Design",
        "role": "Founding Designer",
        "years": "2025 — Present",
        "desc": "Directing visual design systems, AI-native interface explorations, hardware studies, and digital craft at Raimage Studio.",
        "highlights": ["Studio Art Prints & Goods", "AI Developer HUD Prototypes", "Hardware Concepts"]
    },
    {
        "name": "Edfora Infotech",
        "role": "Senior Product Designer",
        "years": "2023 — 2025",
        "desc": "Led product design for scaled learning platforms, student assessment dashboards, and cross-platform design token architecture.",
        "highlights": ["Design Tokens 2.0", "Core Student Assessments", "35% Faster Dev Handoff"]
    },
    {
        "name": "Design Matra",
        "role": "Product Designer",
        "years": "2021 — 2023",
        "desc": "Shaped digital products, mobile applications, and B2B SaaS workflows from early discovery through production launch.",
        "highlights": ["Zero-to-One MVPs", "Interactive Prototypes", "Modular UI Kits"]
    },
    {
        "name": "Kitaro Trading",
        "role": "Graphic Designer",
        "years": "2012 — 2021",
        "desc": "Mastered visual communication, typography, retail packaging, and commercial brand identity systems over 9 foundational years.",
        "highlights": ["12+ Years Total Craft", "Brand Identity Systems", "Packaging Design"]
    }
]

GARDEN_NOTES = [
    {
        "id": "g-1",
        "title": "Is the design we practice worth saving?",
        "topic": "Design Philosophy",
        "date": "26.05.26",
        "read": "6 min read",
        "hook": "Every think piece about restructuring design teams for AI starts with a false premise.",
        "content": "<p>Every think piece about restructuring design teams for AI starts with a false premise: that the value of a designer was in generating production variants. In reality, the craft of product design has always been about reduction, taste, and resolving human friction before a line of code is written.</p><p>As generative models make code and UI assets infinitely cheap, the scarcity shifts to judgment: knowing what <em>not</em> to build. The design we practice is worth saving only if we elevate from component assemblers to systems architects with a moral compass for human attention.</p>"
    },
    {
        "id": "g-2",
        "title": "Stop adding confetti to your product",
        "topic": "Product Craft",
        "date": "12.10.25",
        "read": "8 min read",
        "hook": "We talk about 'delight' a lot in product meetings, but most of the time, it means adding confetti, sounds, or cosmetic polish over broken fundamentals.",
        "content": "<p>We talk about 'delight' a lot in product meetings, but most of the time, it means adding confetti animations, synthetic sounds, or celebratory illustrations over broken fundamentals.</p><p>Real delight in software is not a celebratory illustration after jumping through six confusing hurdles. Real delight is an application that loads instantaneously, remembers my context, anticipates my next move, and lets me finish my job in 15 seconds without making me think.</p><p><strong>Principle:</strong> Solve reliability, speed, and cognitive clarity first. Never use confetti to compensate for friction.</p>"
    },
    {
        "id": "g-3",
        "title": "The Illusion of Productivity",
        "topic": "Product Strategy",
        "date": "19.04.26",
        "read": "5 min read",
        "hook": "I've been thinking about the tech industry lately. And why all of a sudden everyone is building.",
        "content": "<p>In high-growth tech teams, busyness is routinely conflated with progress. Velocity charts tick upward, PRs merge daily, and design files fill up with dozens of polished flows. Yet, month after month, customer churn remains stagnant.</p><p>True product velocity is measured in the cycle time between an unvalidated assumption and a verified customer outcome. When teams optimize for output rather than outcome, they build complex software that solves imaginary problems at extraordinary speed.</p>"
    },
    {
        "id": "g-4",
        "title": "The Engagement Paradox",
        "topic": "UX Ethics",
        "date": "22.10.25",
        "read": "4 min read",
        "hook": "Separating efficiency from effectiveness in user interaction models.",
        "content": "<p>When a product team measures health exclusively through session duration and daily opens, the user experience invariably deteriorates. Notifications become urgent, red badges proliferate, and algorithmic feeds hijack attention.</p><p>Great software respects human attention. It enables users to accomplish their core intent in minimal steps, then gracefully gets out of the way so they can return to their real lives.</p>"
    },
    {
        "id": "g-5",
        "title": "Dogfooding: You Can't Outsource Empathy",
        "topic": "Design Craft",
        "date": "15.06.25",
        "read": "3 min read",
        "hook": "User research shows what users say; using your own software shows where it actually hurts.",
        "content": "<p>To understand software at an instinctual level, designers must live inside their own systems under genuine pressure. Experience the exact latency, broken edge states, and clunky form fields that real users endure every day.</p>"
    },
    {
        "id": "g-6",
        "title": "Interface Clarity Is Subtracted Decisions",
        "topic": "Systems",
        "date": "12.04.25",
        "read": "4 min read",
        "hook": "Great software is not made of features added, but cognitive friction removed before the user notices.",
        "content": "<p>Every redundant configuration dropdown and modal toggle is an outsourced decision. Make the interface feel intuitive by solving complexity internally rather than offloading it to the user.</p>"
    }
]

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
        "desc": "A masterclass on managing system complexity, modular interfaces, and why shallow modules ruin large systems.",
        "takeaway": "Modules should be deep: simple interfaces hiding profound internal power.",
        "link": "https://www.amazon.com/dp/1732102201"
    },
    {
        "id": "res-5",
        "title": "Universal Principles of Design",
        "author": "William Lidwell et al.",
        "category": "Design Craft",
        "format": "Visual Reference",
        "desc": "An authoritative encyclopedia of 125 cognitive, perceptual, and structural laws governing human interaction.",
        "takeaway": "Master Fitts' Law, Hick's Law, and progressive disclosure to reduce cognitive load.",
        "link": "https://www.amazon.com/dp/1592535879"
    },
    {
        "id": "res-6",
        "title": "Shape Up",
        "author": "Ryan Singer (Basecamp)",
        "category": "Product Strategy",
        "format": "Product Methodology",
        "desc": "A revolutionary framework for product teams: fixed time, variable scope, 6-week cycles, and building with shaped appetites.",
        "takeaway": "Never start building until problems are shaped with clear boundaries.",
        "link": "https://www.amazon.com/dp/B081N4R3G9"
    },
    {
        "id": "res-7",
        "title": "Inspired: How to Create Tech Products",
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

SETUP_ITEMS = [
    {
        "id": "setup-1",
        "name": "Aeron Chair",
        "brand": "Herman Miller",
        "category": "Ergonomics",
        "desc": "Classic graphite ergonomic task chair for 12+ hour design marathons.",
        "img": "https://images.unsplash.com/photo-1580481077148-52b34a66d035?auto=format&fit=crop&w=500&q=80",
        "link": "https://www.hermanmiller.com/products/seating/office-chairs/aeron-chairs/"
    },
    {
        "id": "setup-2",
        "name": "Studio Display 27″",
        "brand": "Apple",
        "category": "Display",
        "desc": "5K Retina display with True Tone, P3 wide color, and anti-reflective glass.",
        "img": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=500&q=80",
        "link": "https://www.apple.com/studio-display/"
    },
    {
        "id": "setup-3",
        "name": "AirPods Max",
        "brand": "Apple",
        "category": "Audio",
        "desc": "Active noise cancellation and acoustic spatial audio for deep focus design work.",
        "img": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=500&q=80",
        "link": "https://www.apple.com/airpods-max/"
    },
    {
        "id": "setup-4",
        "name": "MX Master 3S",
        "brand": "Logitech",
        "category": "Peripherals",
        "desc": "Quiet clicks, MagSpeed electromagnetic scrolling, and 8K DPI sensor.",
        "img": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&w=500&q=80",
        "link": "https://www.logitech.com/en-us/products/mice/mx-master-3s.html"
    },
    {
        "id": "setup-5",
        "name": "MacBook Pro 16″ M3 Max",
        "brand": "Apple",
        "category": "Workstation",
        "desc": "Liquid Retina XDR, 64GB unified memory for running local LLMs, Figma & Web Audio.",
        "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=500&q=80",
        "link": "https://www.apple.com/macbook-pro/"
    },
    {
        "id": "setup-6",
        "name": "OP-1 Field Synthesizer",
        "brand": "Teenage Engineering",
        "category": "Audio & Industrial Design",
        "desc": "Iconic portable synthesizer and tactile audio workstation inspiring UI micro-haptics.",
        "img": "https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?auto=format&fit=crop&w=500&q=80",
        "link": "https://teenage.engineering/products/op-1"
    }
]

TOOLS = [
    {
        "name": "Figma",
        "sub": "UI Design",
        "slug": "figma",
        "color": "#F24E1E",
        "bg": "#FFF1EE"
    },
    {
        "name": "Claude",
        "sub": "AI Coding",
        "slug": None,
        "color": "#CC785C",
        "bg": "#FDF3EF",
        "mono": "Cl"
    },
    {
        "name": "Gemini",
        "sub": "AI Research",
        "slug": None,
        "color": "#4285F4",
        "bg": "#EEF4FF",
        "mono": "G•"
    },
    {
        "name": "React",
        "sub": "Frontend",
        "slug": "react",
        "color": "#61DAFB",
        "bg": "#F0FAFE"
    },
    {
        "name": "TypeScript",
        "sub": "Language",
        "slug": "typescript",
        "color": "#3178C6",
        "bg": "#EEF4FB"
    },
    {
        "name": "VS Code",
        "sub": "Editor",
        "slug": "visualstudiocode",
        "color": "#007ACC",
        "bg": "#EEF7FF"
    },
    {
        "name": "Cursor",
        "sub": "AI Editor",
        "slug": None,
        "color": "#1A1A1A",
        "bg": "#F5F5F5",
        "mono": "Cu"
    },
    {
        "name": "Linear",
        "sub": "Planning",
        "slug": "linear",
        "color": "#5E6AD2",
        "bg": "#F0F1FB"
    },
    {
        "name": "Git & GitHub",
        "sub": "Version Control",
        "slug": "github",
        "color": "#181717",
        "bg": "#F5F5F5"
    },
    {
        "name": "Cinema 4D",
        "sub": "3D Design",
        "slug": "cinema4d",
        "color": "#011A6A",
        "bg": "#EEF0F9"
    },
    {
        "name": "Tailwind CSS",
        "sub": "Styling",
        "slug": "tailwindcss",
        "color": "#06B6D4",
        "bg": "#F0FBFC"
    },
    {
        "name": "Notion",
        "sub": "Docs & Notes",
        "slug": "notion",
        "color": "#000000",
        "bg": "#F5F5F5"
    }
]

def get_head(title="Sumit Rai — Senior Product Designer | AI Builder", active_page="index"):
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>{title}</title>
  <meta name="description" content="Sumit Rai — Senior Product Designer with 8+ years product design experience and 12+ years of overall design craft across SaaS, AI, EdTech, and consumer platforms." />
  <meta name="author" content="Sumit Rai" />
  <link rel="icon" type="image/svg+xml" href="./assets/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="./style.css" />
</head>
<body data-page="{active_page}">
"""

def get_nav(active_page):
    # ON INNER PAGES: NO top navigation tabs! ONLY Back button!
    if active_page != "index":
        return f"""
<header class="inner-page-header">
  <div class="wrap-wide inner-header-row">
    <a href="index.html" class="inner-back-btn" title="Back to Home [Esc]">
      <span class="back-arrow">&larr;</span>
      <span class="back-text">Back</span>
      <span class="nav-key">[Esc]</span>
    </a>

    <div class="inner-right-actions">
      <button class="nav-action-pill" id="soundToggleBtn" aria-label="Toggle haptic sounds" title="Toggle audio feedback">
        <span id="soundIcon">🔊</span>
      </button>
      <button class="nav-action-pill" id="cmdPaletteTrigger" aria-label="Quick navigation (Cmd+K)" title="Quick Command Palette (Cmd+K)">
        <kbd>⌘K</kbd>
      </button>
      <button class="theme-toggle-inline" id="themeToggle" aria-label="Toggle dark mode" title="Toggle Dark / Light Mode">
        <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
        <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      </button>
    </div>
  </div>
</header>
"""

    # ON HOMEPAGE: Clean top nav with exact tabs (Contact [C] & Playground [P])
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
      <a href="projects.html">Work <span class="nav-key">[W]</span></a>
      <a href="about.html">About <span class="nav-key">[A]</span></a>
      <a href="resume.html">Resume <span class="nav-key">[R]</span></a>
      <a href="contact.html">Contact <span class="nav-key">[C]</span></a>
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
      <a href="index.html" class="active">Home <span class="nav-key">[Esc]</span></a>
      <a href="projects.html">Selected Work <span class="nav-key">[W]</span></a>
      <a href="about.html">About Me <span class="nav-key">[A]</span></a>
      <a href="resources.html">Resources &amp; Gear <span class="nav-key">[B]</span></a>
      <a href="contact.html">Contact <span class="nav-key">[C]</span></a>
      <a href="resume.html">Resume <span class="nav-key">[R]</span></a>
      <a href="playground.html">Playground <span class="nav-key">[P]</span></a>
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
  <div class="wrap-wide">
    <div class="footer-four-cols">
      <div class="footer-col-item">
        <span class="f-col-header">LINKEDIN</span>
        <a href="https://www.linkedin.com/in/isumitrai/" target="_blank" rel="noopener" class="f-col-link">isumitrai <span class="shahi-arrow">&nearr;</span></a>
      </div>
      <div class="footer-col-item">
        <span class="f-col-header">SUBSTACK</span>
        <a href="https://isumitrai.substack.com/" target="_blank" rel="noopener" class="f-col-link">isumitrai.substack.com <span class="shahi-arrow">&nearr;</span></a>
      </div>
      <div class="footer-col-item">
        <span class="f-col-header">EMAIL</span>
        <a href="mailto:sumitraiworks@gmail.com" class="f-col-link">sumitraiworks@gmail.com <span class="shahi-arrow">&nearr;</span></a>
      </div>
      <div class="footer-col-item">
        <span class="f-col-header">X / TWITTER</span>
        <a href="https://x.com/isumitrai" target="_blank" rel="noopener" class="f-col-link">isumitrai <span class="shahi-arrow">&nearr;</span></a>
      </div>
    </div>

    <div class="footer-sub-meta">
      <div>
        <span>&copy; 2026 Sumit Rai &middot; Senior Product Designer &middot; 8+ yrs product, 12+ yrs craft</span>
      </div>
      <div>
        <span class="live-dot"></span>
        <span>New Delhi, India &middot; <strong id="liveClockText">--:-- -- IST</strong> &middot; Available for select roles</span>
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
        <span class="item-left"><span>Home</span></span>
        <span class="cmd-shortcut">H</span>
      </a>
      <a href="projects.html" class="cmd-item">
        <span class="item-left"><span>Selected Work</span></span>
        <span class="cmd-shortcut">W</span>
      </a>
      <a href="about.html" class="cmd-item">
        <span class="item-left"><span>About Sumit</span></span>
        <span class="cmd-shortcut">A</span>
      </a>
      <a href="resume.html" class="cmd-item">
        <span class="item-left"><span>Resume &amp; Credentials</span></span>
        <span class="cmd-shortcut">R</span>
      </a>
      <a href="resources.html" class="cmd-item">
        <span class="item-left"><span>Resources &amp; Gear</span></span>
        <span class="cmd-shortcut">B</span>
      </a>
      <a href="playground.html" class="cmd-item">
        <span class="item-left"><span>Playground (Design &amp; Shop)</span></span>
        <span class="cmd-shortcut">P</span>
      </a>
      <a href="contact.html" class="cmd-item">
        <span class="item-left"><span>Contact</span></span>
        <span class="cmd-shortcut">C</span>
      </a>
      <a href="https://isumitrai.substack.com/" target="_blank" rel="noopener" class="cmd-item">
        <span class="item-left"><span>Substack Newsletter</span></span>
        <span class="cmd-shortcut">SUB</span>
      </a>
      <a href="assets/Sumit_Rai_Resume.pdf" download class="cmd-item">
        <span class="item-left"><span>Download Resume PDF</span></span>
        <span class="cmd-shortcut">PDF</span>
      </a>
      <div class="cmd-item" id="cmdToggleTheme">
        <span class="item-left"><span>Toggle Dark / Light Mode</span></span>
        <span class="cmd-shortcut">T</span>
      </div>
    </div>
  </div>
</div>

<!-- Garden Note Reader Modal -->
<div class="garden-modal" id="gardenModal" role="dialog" aria-modal="true" aria-label="Digital Garden Note">
  <div class="garden-modal-box">
    <button class="garden-modal-close" onclick="closeGardenNote()" aria-label="Close note">&times;</button>
    <div id="gardenModalBody"></div>
  </div>
</div>
"""

global_js = """
(function(){
  /* ================================================================
     CUSTOM CURSOR — Red square, shahimim.com inspired
     Only active on devices with a fine pointer (mouse / trackpad)
     ================================================================ */
  const hasFineMouse = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  if (hasFineMouse) {
    const cursor = document.createElement('div');
    cursor.id = 'custom-cursor';
    cursor.className = 'custom-cursor';
    document.body.appendChild(cursor);

    let mouseX = 0, mouseY = 0;
    let cursorX = 0, cursorY = 0;
    let rafId = null;

    // Smooth spring-follow cursor
    function animateCursor() {
      // Spring coefficient: 0.10 = slow/smooth, 0.18 = snappier
      cursorX += (mouseX - cursorX) * 0.14;
      cursorY += (mouseY - cursorY) * 0.14;
      cursor.style.transform = 'translate(' + cursorX + 'px, ' + cursorY + 'px)';
      rafId = requestAnimationFrame(animateCursor);
    }
    animateCursor();

    document.addEventListener('mousemove', function(e) {
      mouseX = e.clientX;
      mouseY = e.clientY;
      cursor.style.opacity = '1';
    }, { passive: true });

    document.addEventListener('mouseleave', function() {
      cursor.style.opacity = '0';
    });

    // Hover: enlarge on interactive elements
    function addHover(selector) {
      document.querySelectorAll(selector).forEach(function(el) {
        el.addEventListener('mouseenter', function() {
          cursor.classList.add('cursor-hover');
          cursor.classList.remove('cursor-text', 'cursor-click');
        });
        el.addEventListener('mouseleave', function() {
          cursor.classList.remove('cursor-hover', 'cursor-text', 'cursor-click');
        });
      });
    }

    addHover('a, button, [role="button"], .shahi-card, .shahi-media-card, .proj-card, .editorial-proj-card, .editorial-exp-card, .garden-item, .setup-card, .resource-card, .pg-card-rich, label, select');

    // Text cursor on inputs
    document.querySelectorAll('input, textarea, [contenteditable]').forEach(function(el) {
      el.addEventListener('mouseenter', function() {
        cursor.classList.add('cursor-text');
        cursor.classList.remove('cursor-hover', 'cursor-click');
      });
      el.addEventListener('mouseleave', function() {
        cursor.classList.remove('cursor-text', 'cursor-hover', 'cursor-click');
      });
    });

    // Click flash
    document.addEventListener('mousedown', function() {
      cursor.classList.add('cursor-click');
    });
    document.addEventListener('mouseup', function() {
      cursor.classList.remove('cursor-click');
    });
  }

  /* ================================================================
     AUDIO ENGINE
     ================================================================ */
  const AudioEngine = {
    enabled: true,
    init() {
      if (!this.ctx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (AudioContext) this.ctx = new AudioContext();
      }
    },
    playTick(freq = 900, dur = 0.02) {
      if (!this.enabled) return;
      try {
        this.init();
        if (!this.ctx) return;
        if (this.ctx.state === 'suspended') this.ctx.resume();
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
        gain.gain.setValueAtTime(0.025, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + dur);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start();
        osc.stop(this.ctx.currentTime + dur);
      } catch(e){}
    }
  };

  const soundBtn = document.getElementById('soundToggleBtn');
  const soundIcon = document.getElementById('soundIcon');
  const soundLabel = document.getElementById('soundLabel');
  if (soundBtn) {
    soundBtn.addEventListener('click', function(){
      AudioEngine.enabled = !AudioEngine.enabled;
      if (soundIcon) soundIcon.textContent = AudioEngine.enabled ? '🔊' : '🔇';
      if (soundLabel) soundLabel.textContent = AudioEngine.enabled ? 'Sound' : 'Mute';
      if (AudioEngine.enabled) AudioEngine.playTick(1000, 0.03);
    });
  }

  const themeToggle = document.getElementById('themeToggle');
  const htmlEl = document.documentElement;
  const savedTheme = localStorage.getItem('folio_theme') || 'light';
  htmlEl.setAttribute('data-theme', savedTheme);

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      AudioEngine.playTick(1200, 0.03);
      const cur = htmlEl.getAttribute('data-theme') || 'light';
      const nxt = cur === 'dark' ? 'light' : 'dark';
      htmlEl.setAttribute('data-theme', nxt);
      localStorage.setItem('folio_theme', nxt);
    });
  }

  const menuToggle = document.getElementById('navMenuToggle');
  const drawer = document.getElementById('mobileNavDrawer');
  if (menuToggle && drawer) {
    menuToggle.addEventListener('click', () => {
      AudioEngine.playTick(750, 0.03);
      const open = menuToggle.getAttribute('aria-expanded') === 'true';
      menuToggle.setAttribute('aria-expanded', !open);
      drawer.setAttribute('aria-hidden', open);
      drawer.classList.toggle('active', !open);
    });
  }

  function updateDelhiClock() {
    const el = document.getElementById('liveClockText');
    if (!el) return;
    try {
      const now = new Date();
      const options = {
        timeZone: 'Asia/Kolkata',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
      };
      el.textContent = now.toLocaleTimeString('en-US', options) + ' IST';
    } catch(e) {
      el.textContent = '17:40 IST';
    }
  }
  setInterval(updateDelhiClock, 1000);
  updateDelhiClock();

  const cmdModal = document.getElementById('cmdModal');
  const cmdInput = document.getElementById('cmdInput');
  const cmdTrigger = document.getElementById('cmdPaletteTrigger');

  function openCmd() {
    AudioEngine.playTick(950, 0.03);
    if (cmdModal) {
      cmdModal.classList.add('active');
      if (cmdInput) {
        cmdInput.value = '';
        cmdInput.focus();
      }
      document.body.style.overflow = 'hidden';
    }
  }

  function closeCmd() {
    if (cmdModal) {
      cmdModal.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  if (cmdTrigger) cmdTrigger.addEventListener('click', openCmd);
  if (cmdModal) {
    cmdModal.addEventListener('click', (e) => {
      if (e.target === cmdModal) closeCmd();
    });
  }

  window.openGardenNote = function(noteId) {
    const note = (window.GARDEN_DATA || []).find(n => n.id === noteId);
    if (!note) return;
    const body = document.getElementById('gardenModalBody');
    const modal = document.getElementById('gardenModal');
    if (!body || !modal) return;
    body.innerHTML = `
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:16px;">
        <span class="garden-tag">${note.topic}</span>
        <span class="garden-date">${note.date} &middot; ${note.read}</span>
      </div>
      <h2 style="font-size:24px; font-weight:700; letter-spacing:-0.025em; margin-bottom:20px; line-height:1.25; color:var(--ink);">${note.title}</h2>
      <div style="font-size:15px; line-height:1.7; color:var(--ink-soft);">${note.content}</div>
      <div style="margin-top:32px; padding-top:20px; border-top:1px solid var(--line); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
        <span style="font-size:12px; color:var(--ink-muted); font-family:var(--font-mono);">From Sumit Rai's Digital Garden</span>
        <a href="https://isumitrai.substack.com/" target="_blank" rel="noopener" style="font-size:13px; font-weight:600; color:var(--accent); text-decoration:none;">Read on Substack <span class="shahi-arrow">&nearr;</span></a>
      </div>
    `;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    AudioEngine.playTick(880, 0.03);
  };

  window.closeGardenNote = function() {
    const modal = document.getElementById('gardenModal');
    if (modal) modal.classList.remove('active');
    document.body.style.overflow = '';
  };

  document.addEventListener('keydown', function(e){
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (cmdModal && cmdModal.classList.contains('active')) closeCmd();
      else openCmd();
      return;
    }

    if (e.key === 'Escape') {
      const gModal = document.getElementById('gardenModal');
      if (gModal && gModal.classList.contains('active')) {
        closeGardenNote();
        return;
      }
      if (cmdModal && cmdModal.classList.contains('active')) {
        closeCmd();
        return;
      }
      const curPage = document.body.dataset.page;
      if (curPage && curPage !== 'index') {
        AudioEngine.playTick(820, 0.03);
        window.location.href = 'index.html';
        return;
      }
    }

    const tag = (e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || tag === 'select' || e.target.isContentEditable) return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;

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
    } else if (key === 't') {
      AudioEngine.playTick(1200, 0.03);
      const cur = htmlEl.getAttribute('data-theme') || 'light';
      const nxt = cur === 'dark' ? 'light' : 'dark';
      htmlEl.setAttribute('data-theme', nxt);
      localStorage.setItem('folio_theme', nxt);
    }
  });
})();
"""

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

    exp_timeline_html = ""
    for c in COMPANIES:
        highlights_html = " ".join([f'<span class="metric-pill">{h}</span>' for h in c['highlights']])
        exp_timeline_html += f"""
        <div class="exp-flat-item">
          <div class="exp-top">
            <div>
              <span class="exp-company">{c['name']}</span>
              <div class="exp-role">{c['role']}</div>
            </div>
            <span class="exp-date">{c['years']}</span>
          </div>
          <p class="exp-desc">{c['desc']}</p>
          <div class="exp-metrics">
            {highlights_html}
          </div>
        </div>
"""

    tools_html = ""
    for t in TOOLS:
        if t.get("slug"):
            # Use Simple Icons CDN logo
            logo_html = f'<img src="https://cdn.simpleicons.org/{t["slug"]}" alt="{t["name"]} logo" loading="lazy" class="tool-logo-img" />'
        else:
            # Styled monogram for AI tools / tools without CDN entry
            mono = t.get("mono", t["name"][:2])
            logo_html = f'<span class="tool-mono" style="color:{t["color"]};">{mono}</span>'

        tools_html += f"""
        <div class="tool-tile-new" title="{t['name']}">
          <div class="tool-logo-wrap" style="background:{t['bg']};">
            {logo_html}
          </div>
          <span class="tool-name">{t['name']}</span>
          <span class="tool-sub">{t['sub']}</span>
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
        <a href="resources.html" class="btn btn-secondary">Resources &amp; Gear <span class="btn-key">[B]</span></a>
        <a href="playground.html" class="btn btn-secondary">Playground <span class="btn-key">[P]</span></a>
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
        <a href="projects.html" class="btn btn-secondary">See All Work <span class="btn-key">[W]</span> <span class="shahi-arrow">&nearr;</span></a>
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

    <!-- SECTION 04 — SELECTED EXPERIENCE (REVERSE CHRONOLOGICAL ORDER) -->
    <section class="experience-section">
      <div class="section-header-row">
        <div class="section-title-wrap">
          <span class="eyebrow"><span class="dot"></span> Career Path</span>
          <h2>Selected Experience</h2>
          <p>Proven track record of designing, shipping, and scaling products across key tech companies (latest first).</p>
        </div>
        <a href="resume.html" class="section-header-link">View Full Resume <span class="btn-key">[R]</span> <span class="shahi-arrow">&nearr;</span></a>
      </div>

      <div class="timeline-clean">
        {exp_timeline_html}
      </div>
    </section>

    <!-- SECTION 05 — SOFTWARE & DESIGN STACK -->
    <section class="tools-section">
      <div class="section-header-row">
        <div class="section-title-wrap">
          <span class="eyebrow"><span class="dot"></span> Systems &amp; Toolkit</span>
          <h2>Software &amp; Design Stack</h2>
          <p>My daily instruments for product strategy, UI design, generative prototyping, and code production.</p>
        </div>
      </div>
      <div class="tools-grid-new">
        {tools_html}
      </div>
    </section>

    <!-- SECTION 06 — BENTO BOX AT BOTTOM (Exact Match to User's Uploaded Screenshot) -->
    <section class="bento-section" id="bento" style="padding-top:40px; border-top:1px solid var(--line);">
      <div class="shahi-bento-grid">
        <!-- Card 1: Media Card with pill (Top Left) -->
        <a href="playground.html" class="shahi-media-card" aria-label="Bootstrapping Raimage Lab">
          <img src="./assets/pg_002.jpg" alt="Bootstrapping a startup" loading="lazy" />
          <span class="shahi-media-pill">Bootstrapping a startup</span>
          <span class="shahi-card-key" style="color:#FFF;">W</span>
        </a>

        <!-- Card 2: Digital Garden with stacked index cards (Top Right) -->
        <div class="shahi-card" onclick="window.location.href='resources.html#garden'" role="button" tabindex="0" style="cursor:pointer;" aria-label="Digital Garden">
          <span class="shahi-card-label">Digital garden</span>
          <div class="garden-card-stack">
            <div>
              <span class="stack-date">26.05.26</span>
              <span class="stack-num">0014</span>
            </div>
            <h4>Is the design we practice worth saving?</h4>
            <p>Every think piece about restructuring design teams for AI starts with a false premise.</p>
          </div>
          <span class="shahi-card-key">G</span>
        </div>

        <!-- Card 3: Writing card with confetti line drawing (Middle, Span Full) -->
        <a href="https://isumitrai.substack.com/" target="_blank" rel="noopener" class="shahi-card span-full" aria-label="Featured Essay on Substack">
          <span class="shahi-card-label">Writing</span>
          <div class="writing-card-flex">
            <svg width="56" height="56" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="color:var(--ink-soft); flex-shrink:0;">
              <path d="M14 50 L28 42 L22 36 Z" fill="var(--surface-subtle)" stroke="currentColor"/>
              <line x1="14" y1="50" x2="8" y2="56" stroke-dasharray="2 2"/>
              <path d="M28 38 C34 30, 40 32, 48 20"/>
              <path d="M24 34 C30 24, 38 22, 44 12"/>
              <path d="M30 42 C38 40, 44 44, 54 36"/>
              <circle cx="50" cy="16" r="1.5" fill="currentColor"/>
              <circle cx="56" cy="26" r="1.5" fill="currentColor"/>
              <circle cx="40" cy="10" r="1.5" fill="currentColor"/>
            </svg>
            <div class="writing-card-text">
              <h3>Stop adding confetti to your product</h3>
              <p>We talk about &ldquo;delight&rdquo; a lot in product meetings, but most of the time, it means adding confetti, sounds, or cosmetic polish over broken fundamentals.</p>
              <div class="writing-card-meta">12.10.25 &middot; 8 min read &middot; Read on Substack <span class="shahi-arrow">&nearr;</span></div>
            </div>
          </div>
          <span class="shahi-card-key">B</span>
        </a>

        <!-- Card 4: Studio / Services (Bottom Left) — NOT the contact page -->
        <a href="contact.html" class="shahi-card" aria-label="Work with Sumit Rai">
          <span class="shahi-card-label">Studio</span>
          <div class="contact-tier-preview">
            <div>Advisory &amp; coaching</div>
            <div class="highlight">Design mentorship</div>
            <div>Talks &amp; panels</div>
          </div>
          <span class="shahi-card-key">S</span>
        </a>

        <!-- Card 5: Resources with colourful book spines (Bottom Right) -->
        <a href="resources.html" class="shahi-card" aria-label="Resources &amp; Gear">
          <span class="shahi-card-label">Resources</span>
          <div>
            <p style="font-size:13px; color:var(--ink-soft); margin:0;">Books worth reading, tools worth keeping.</p>
            <div class="book-spines-row">
              <div class="book-spine" style="height:36px; background:#D9381E;"></div>
              <div class="book-spine" style="height:48px; background:#E5DFD3; border:1px solid #ccc;"></div>
              <div class="book-spine" style="height:42px; background:#4B5842;"></div>
              <div class="book-spine" style="height:52px; background:#1C352D;"></div>
              <div class="book-spine" style="height:38px; background:#D0B084;"></div>
              <div class="book-spine" style="height:46px; background:#E89635;"></div>
              <div class="book-spine" style="height:40px; background:#F4C430;"></div>
              <div class="book-spine" style="height:50px; background:#E5DFD3; border:1px solid #ccc;"></div>
              <div class="book-spine" style="height:44px; background:#C9372C;"></div>
              <div class="book-spine" style="height:38px; background:#BAC7A7;"></div>
              <div class="book-spine" style="height:48px; background:#889E73;"></div>
            </div>
          </div>
          <span class="shahi-card-key">R</span>
        </a>
      </div>
    </section>

  </div>
</main>
"""

    index_js = "window.GARDEN_DATA = " + json.dumps(GARDEN_NOTES) + ";"

    return get_head("Sumit Rai — Senior Product Designer | AI Builder", "index") + get_nav("index") + content + footer_html + f"<script>\n{global_js}\n{index_js}\n</script>\n</body>\n</html>"

def build_projects():
    # Build editorial numbered project cards (inspired by reference screenshot tier layout)
    num_labels = ["01", "02", "03", "04", "05", "06"]
    cards_html = ""
    for i, p in enumerate(PROJECTS):
        num = num_labels[i] if i < len(num_labels) else f"0{i+1}"
        tags_html = " ".join([f'<span class="proj-tag">{t}</span>' for t in p['tags']])
        cards_html += f"""
      <article class="editorial-proj-card" id="{p['id']}">
        <div class="editorial-proj-left">
          <span class="editorial-proj-label">{p['category']}</span>
          <span class="editorial-proj-num">{num}</span>
          <h2 class="editorial-proj-title">{p['title']}</h2>
          <div class="editorial-proj-lead">{p['tagline']}</div>
        </div>
        <div class="editorial-proj-right">
          <div class="editorial-proj-preview">
            <img src="{p['image']}" alt="{p['full_title']}" loading="lazy" />
          </div>
          <ul class="editorial-proj-bullets">
            <li>{p['role']}</li>
            <li>{p['client']}</li>
            <li>{p['impact'][:72]}{'…' if len(p['impact']) > 72 else ''}</li>
          </ul>
        </div>
        <div class="editorial-proj-meta-row">
          <div>
            <div class="meta-label">TAGS</div>
            <div class="meta-val">{tags_html}</div>
          </div>
          <div>
            <div class="meta-label">YEAR</div>
            <div class="meta-val">{p['year']}</div>
          </div>
        </div>
      </article>
"""

    content = f"""
<main class="page-body">
  <div class="wrap-wide">

    <div class="editorial-page-hero">
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
        <span style="font-family:var(--font-mono); font-size:12px; font-weight:600; color:var(--accent);">[W]</span>
        <h1 style="font-size:34px; font-weight:700; letter-spacing:-0.03em; margin:0; color:var(--ink);">Selected Work</h1>
      </div>
      <p style="font-size:15px; color:var(--ink-soft); max-width:580px; line-height:1.65; margin:0;">
        Digital products, design systems, and software shaped over 8+ years — from zero-to-one SaaS to scaled EdTech platforms.
      </p>
    </div>

    <div class="editorial-proj-list">
      {cards_html}
    </div>

    <section class="contact-cta-section" style="margin-top:64px;">
      <span class="eyebrow"><span class="dot"></span> Collaboration</span>
      <h2>Have a project in mind?</h2>
      <p>I partner with ambitious teams to turn complex ideas into refined, scalable digital products.</p>
      <div class="cta-btns">
        <a href="contact.html" class="btn btn-primary">Contact Sumit <span class="btn-key">[C]</span> <span class="shahi-arrow">&nearr;</span></a>
        <a href="mailto:sumitraiworks@gmail.com" class="btn btn-secondary">Email Sumit</a>
      </div>
    </section>

  </div>
</main>
"""
    return get_head("Selected Work — Sumit Rai", "projects") + get_nav("projects") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"

def build_about():
    # Build experience as numbered editorial cards (like reference screenshot)
    exp_nums = ["01", "02", "03", "04"]
    exp_cards_html = ""
    for i, c in enumerate(COMPANIES):
        num = exp_nums[i] if i < len(exp_nums) else f"0{i+1}"
        highlights_html = "".join([f'<li>{h}</li>' for h in c['highlights']])
        exp_cards_html += f"""
      <div class="editorial-exp-card">
        <div class="editorial-exp-left">
          <span class="editorial-exp-label">{c['years']}</span>
          <span class="editorial-exp-num">{num}</span>
          <h3 class="editorial-exp-title">{c['role']}</h3>
          <div class="editorial-exp-lead">{c['name']}</div>
          <p class="editorial-exp-sub">{c['desc']}</p>
        </div>
        <div class="editorial-exp-right">
          <ul class="editorial-exp-bullets">
            {highlights_html}
          </ul>
        </div>
      </div>
"""

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
          Over the past 12+ years, I've journeyed from mastering visual communication, typography, and packaging at Kitaro Trading to architecting digital products at Design Matra, Edfora Infotech, and founding Raimage Design. With 8+ years dedicated to digital product design, I balance strategic clarity with rigorous visual craftsmanship.
        </p>
        <div style="display:flex; gap:12px; margin-top:28px; flex-wrap:wrap;">
          <a href="resume.html" class="btn btn-primary">Read Resume <span class="btn-key">[R]</span></a>
          <a href="resources.html" class="btn btn-secondary">Curated Resources <span class="btn-key">[B]</span></a>
          <a href="https://isumitrai.substack.com/" target="_blank" rel="noopener" class="btn btn-secondary">Substack <span class="shahi-arrow">&nearr;</span></a>
        </div>
      </div>

      <div class="about-avatar-card">
        <img src="./assets/avatar.jpg" alt="Sumit Rai portrait" />
      </div>
    </section>

    <!-- 02 — EXPERIENCE (Editorial numbered cards) -->
    <section style="margin-top:72px; padding-top:48px; border-top:1px solid var(--line);">
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:40px;">
        <span style="font-family:var(--font-mono); font-size:12px; font-weight:600; color:var(--accent);">[A]</span>
        <h2 style="font-size:28px; font-weight:700; letter-spacing:-0.025em; margin:0; color:var(--ink);">Experience</h2>
      </div>
      <div class="editorial-exp-list">
        {exp_cards_html}
      </div>
    </section>

    <!-- 03 — DESIGN PHILOSOPHY -->
    <section class="about-editorial-block" style="margin-top:64px; padding-top:48px; border-top:1px solid var(--line);">
      <span class="eyebrow"><span class="dot"></span> Design Philosophy</span>
      <h2>How I Work</h2>
      <p>
        I believe that the best design starts with understanding. Before pushing pixels, I focus on identifying the core human tension, understanding the business model, and eliminating points of friction.
      </p>
      <div class="approach-grid" style="margin-top:24px;">
        <div class="approach-card">
          <span class="approach-num">01 / DISCOVER</span>
          <h3>Explore &amp; Understand</h3>
          <p>Understand the human context and business goals before jumping into Figma.</p>
        </div>
        <div class="approach-card">
          <span class="approach-num">02 / CONNECT</span>
          <h3>Validate with Code</h3>
          <p>Bridge the design-to-code gap using rapid prototypes in React, HTML Canvas, and AI APIs.</p>
        </div>
        <div class="approach-card">
          <span class="approach-num">03 / SHIP</span>
          <h3>Ship Scalable Systems</h3>
          <p>Build unified design tokens and scalable components that engineers love using.</p>
        </div>
      </div>
    </section>

    <section class="contact-cta-section" style="margin-top:64px;">
      <span class="eyebrow"><span class="dot"></span> Let's Connect</span>
      <h2>Interested in collaborating?</h2>
      <p>I'm always open to discussing senior product design roles, design systems advisory, or creative tech.</p>
      <div class="cta-btns">
        <a href="contact.html" class="btn btn-primary">Contact Sumit <span class="btn-key">[C]</span> <span class="shahi-arrow">&nearr;</span></a>
        <a href="mailto:sumitraiworks@gmail.com" class="btn btn-secondary">Send Email</a>
      </div>
    </section>

  </div>
</main>
"""
    return get_head("About — Sumit Rai", "about") + get_nav("about") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"

def build_resume():
    exp_entries_html = ""
    for c in COMPANIES:
        exp_entries_html += f"""
        <div class="resume-entry">
          <div class="entry-header">
            <div>
              <h3 class="entry-role">{c['role']}</h3>
              <div class="entry-org">{c['name']} &middot; Full-time</div>
            </div>
            <span class="entry-date">{c['years']}</span>
          </div>
          <p class="entry-desc">{c['desc']}</p>
        </div>
"""

    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <div class="resume-view-wrap">
      <div class="resume-top-bar">
        <div>
          <span class="eyebrow"><span class="dot"></span> Curriculum Vitae</span>
          <h1>Sumit Rai</h1>
          <p class="resume-subhead">Senior Product Designer &middot; 8+ years product design &middot; 12+ years design craft &middot; New Delhi, India</p>
        </div>
        <div class="resume-actions">
          <a href="assets/Sumit_Rai_Resume.pdf" download class="btn btn-primary">
            <span>Download PDF</span>
            <span class="shahi-arrow">&darr;</span>
          </a>
        </div>
      </div>

      <div class="resume-section-block">
        <h2 class="resume-sec-title">Professional Experience (Latest First)</h2>
        {exp_entries_html}
      </div>

      <div class="resume-section-block">
        <h2 class="resume-sec-title">Core Competencies</h2>
        <div class="skills-grid-clean">
          <div class="skill-group">
            <h4>Product Design</h4>
            <p>User Experience Strategy, Interaction Design, User Research, Journey Mapping, Information Architecture, Usability Testing</p>
          </div>
          <div class="skill-group">
            <h4>Design Systems</h4>
            <p>Design Tokens, Component Libraries, Multi-Brand Theming, WCAG AAA Accessibility, Figma Variants, Developer Handoff</p>
          </div>
          <div class="skill-group">
            <h4>Technical &amp; AI</h4>
            <p>React, TypeScript, HTML5/CSS3, Tailwind CSS, Claude / Gemini APIs, Web Audio, Rapid Prototyping, Git / GitHub</p>
          </div>
        </div>
      </div>

    </div>

  </div>
</main>
"""
    return get_head("Resume — Sumit Rai", "resume") + get_nav("resume") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"

def build_resources():
    book_cards_html = ""
    for r in RESOURCES:
        book_cards_html += f"""
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
          <a href="{r['link']}" target="_blank" rel="noopener" class="resource-amazon-btn" title="View {r['title']} on Amazon">
            <span>Get on Amazon</span>
            <span class="arrow shahi-arrow">&nearr;</span>
          </a>
          <span class="resource-format-tag">Curated Read</span>
        </div>
      </article>
"""

    setup_cards_html = ""
    for s in SETUP_ITEMS:
        setup_cards_html += f"""
      <a href="{s['link']}" target="_blank" rel="noopener" class="setup-card" title="View {s['name']}">
        <span class="setup-hover-pill">Visit <span class="shahi-arrow">&nearr;</span></span>
        <div class="setup-img-wrap">
          <img src="{s['img']}" alt="{s['name']}" loading="lazy" />
        </div>
        <div class="setup-card-name">{s['name']}</div>
        <div class="setup-card-brand">{s['brand']} &middot; {s['category']}</div>
      </a>
"""

    garden_list_html = ""
    for g in GARDEN_NOTES:
        garden_list_html += f"""
        <div class="garden-item" onclick="openGardenNote('{g['id']}')" role="button" tabindex="0" aria-label="Read {g['title']}">
          <div class="garden-left-meta">
            <span class="garden-tag">{g['topic']}</span>
            <span class="garden-date">{g['date']}</span>
          </div>
          <div class="garden-main-body">
            <h3 class="garden-title">{g['title']}</h3>
            <p class="garden-snippet">{g['hook']}</p>
          </div>
          <div class="garden-right-meta">
            <span class="garden-read-time">{g['read']}</span>
            <span class="shahi-arrow">&nearr;</span>
          </div>
        </div>
"""

    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <!-- HERO (Matching Image 4) -->
    <div style="margin-bottom:40px;">
      <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
        <span style="font-family:var(--font-mono); font-size:12px; font-weight:600; color:var(--accent);">[R]</span>
        <h1 style="font-size:32px; font-weight:700; letter-spacing:-0.03em; margin:0; color:var(--ink);">Resources &amp; Gear</h1>
      </div>
      <p style="font-size:15px; color:var(--ink-soft); max-width:650px; line-height:1.6; margin:0;">
        Well-designed things worth owning, books worth reading, tools worth keeping, links worth saving. Curated by Sumit Rai.
      </p>

      <!-- Substack callout -->
      <div style="margin-top:16px;">
        <a href="https://isumitrai.substack.com/" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size:13px;">
          <span>Read Writing on Substack</span>
          <span class="shahi-arrow">&nearr;</span>
        </a>
      </div>
    </div>

    <!-- Filter Buttons & Search -->
    <div class="resources-filter-row" id="resFilterRow" style="margin-bottom:32px;">
      <button class="filter-btn active" data-tab="setup">My Setup &amp; Gear (6)</button>
      <button class="filter-btn" data-tab="books">Curated Books (12)</button>
      <button class="filter-btn" data-tab="garden">Digital Garden (6 Notes)</button>
    </div>

    <!-- TAB 1: SETUP & GEAR (Matching Image 4) -->
    <div id="tabSetup" class="res-tab-pane">
      <div style="margin-bottom:16px;">
        <h3 style="font-size:18px; font-weight:600; color:var(--ink); margin:0;">My Setup</h3>
        <p style="font-size:13.5px; color:var(--ink-soft); margin:4px 0 0;">Hardware and daily instruments for industrial craft and software design.</p>
      </div>
      <div class="setup-grid">
        {setup_cards_html}
      </div>
    </div>

    <!-- TAB 2: CURATED BOOKS (Matching shahimim.com/#resources) -->
    <div id="tabBooks" class="res-tab-pane" style="display:none;">
      <div style="margin-bottom:16px;">
        <h3 style="font-size:18px; font-weight:600; color:var(--ink); margin:0;">Reading Shelf</h3>
        <p style="font-size:13.5px; color:var(--ink-soft); margin:4px 0 0;">12+ foundational texts on software architecture, design craft, and cognitive ergonomics.</p>
      </div>
      <div class="resources-grid" id="resGrid">
        {book_cards_html}
      </div>
    </div>

    <!-- TAB 3: DIGITAL GARDEN (Matching Image 5) -->
    <div id="tabGarden" class="res-tab-pane" style="display:none;">
      <div style="margin-bottom:16px;">
        <h3 style="font-size:18px; font-weight:600; color:var(--ink); margin:0;">Digital Garden &amp; Notes</h3>
        <p style="font-size:13.5px; color:var(--ink-soft); margin:4px 0 0;">Atomic essays on product thinking, design systems, and interface craft.</p>
      </div>
      <div class="garden-list">
        {garden_list_html}
      </div>
    </div>

  </div>
</main>
"""

    res_js = """
  window.GARDEN_DATA = """ + json.dumps(GARDEN_NOTES) + """;

  const tabBtns = document.querySelectorAll('#resFilterRow .filter-btn');
  const tabSetup = document.getElementById('tabSetup');
  const tabBooks = document.getElementById('tabBooks');
  const tabGarden = document.getElementById('tabGarden');

  function showTab(tabName) {
    tabBtns.forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === tabName);
    });
    if (tabSetup) tabSetup.style.display = tabName === 'setup' ? 'block' : 'none';
    if (tabBooks) tabBooks.style.display = tabName === 'books' ? 'block' : 'none';
    if (tabGarden) tabGarden.style.display = tabName === 'garden' ? 'block' : 'none';
  }

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      showTab(btn.dataset.tab);
    });
  });

  if (window.location.hash === '#garden') {
    showTab('garden');
  } else if (window.location.hash === '#books') {
    showTab('books');
  }
"""
    return get_head("Resources & Gear — Sumit Rai", "resources") + get_nav("resources") + content + footer_html + f"<script>\n{global_js}\n{res_js}\n</script>\n</body>\n</html>"

def build_playground():
    items = [
        {
            "id": "pg-1",
            "title": "Stacklet AI Dev Terminal HUD",
            "category": "UI & AI Concepts",
            "tag": "AI &middot; Dev Tool",
            "year": "2026",
            "desc": "AI-native developer terminal HUD, interactive command palettes, and dark-mode coding canvas.",
            "img": "./assets/pg_002.jpg",
            "edition": "Digital Asset",
            "is_shop": False
        },
        {
            "id": "pg-2",
            "title": "Koolkidz Watches Industrial Concept",
            "category": "Industrial & 3D",
            "tag": "Hardware &middot; Wearable",
            "year": "2025",
            "desc": "Playful children's digital timepiece, tactile silicone strap explorations, and graphic watch faces.",
            "img": "./assets/pg_001.jpg",
            "edition": "Hardware Study",
            "is_shop": False
        },
        {
            "id": "pg-3",
            "title": "Radio Concept Hardware Prototype",
            "category": "Industrial & 3D",
            "tag": "Hardware &middot; Audio",
            "year": "2025",
            "desc": "Tactile retro-futuristic audio device concept with mechanical switches and digital frequency display.",
            "img": "./assets/pg_004.jpg",
            "edition": "Industrial Study",
            "is_shop": False
        },
        {
            "id": "pg-4",
            "title": "Chhota Bheem Merchandise & Branding",
            "category": "Brand & Packaging",
            "tag": "Packaging &middot; Retail",
            "year": "2024",
            "desc": "Commercial merchandise branding, character packaging system, and retail promotional graphics.",
            "img": "./assets/pg_003.jpg",
            "edition": "Retail Production",
            "is_shop": False
        },
        {
            "id": "pg-5",
            "title": "A Walk to Remember — Art Print",
            "category": "Shop: Fine Art Prints",
            "tag": "Fine Art &middot; Print Edition",
            "year": "2025",
            "desc": "Limited digital print study exploring atmospheric lighting, warm monochrome tones, and visual silence. Featured on Raimage Design.",
            "img": "./assets/img_01.jpg",
            "edition": "Archival Giclée Print · Limited to 50",
            "is_shop": True
        },
        {
            "id": "pg-6",
            "title": "A Thousand Years — Typography Monograph",
            "category": "Shop: Fine Art Prints",
            "tag": "Editorial &middot; Archival Print",
            "year": "2024",
            "desc": "Architectural proportions applied to editorial typography and structural layout systems. Museum-grade cotton paper print.",
            "img": "./assets/img_03.jpg",
            "edition": "Archival Giclée Print · Limited to 50",
            "is_shop": True
        }
    ]

    cards_html = ""
    for it in items:
        shop_btn_html = ""
        if it['is_shop']:
            shop_btn_html = f"""
            <div style="margin-top:14px; padding-top:12px; border-top:1px solid var(--line); display:flex; justify-content:space-between; align-items:center;">
              <span class="shop-edition-badge">{it['edition']}</span>
              <a href="mailto:sumitraiworks@gmail.com?subject=Raimage%20Shop%20Inquiry%20-%20{it['title']}" class="pg-shop-btn">
                <span>Inquire Print</span>
                <span class="shahi-arrow">&nearr;</span>
              </a>
            </div>"""
        else:
            shop_btn_html = f"""
            <div class="pg-foot">
              <span>Raimage Studio Lab</span>
              <span class="shahi-arrow">&nearr;</span>
            </div>"""

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
          {shop_btn_html}
        </div>
      </article>
"""

    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <div class="pg-hero-block">
      <span class="eyebrow"><span class="dot"></span> Raimage Design Studio</span>
      <h1>Playground &mdash; Design &amp; Shop</h1>
      <p>
        Uncommissioned software experiments, industrial hardware concepts, and limited edition fine art prints from Raimage Design Studio.
      </p>
    </div>

    <!-- Filter Buttons -->
    <div class="pg-filter-row" id="pgFilterRow">
      <button class="filter-btn active" data-filter="all">All Creations (6)</button>
      <button class="filter-btn" data-filter="UI &amp; AI Concepts">UI &amp; AI Concepts</button>
      <button class="filter-btn" data-filter="Industrial &amp; 3D">Industrial &amp; 3D</button>
      <button class="filter-btn" data-filter="Shop: Fine Art Prints">Shop: Fine Art Prints</button>
      <button class="filter-btn" data-filter="Brand &amp; Packaging">Brand &amp; Packaging</button>
    </div>

    <div class="pg-grid-rich" id="pgGrid">
      {cards_html}
    </div>

    <!-- Raimage Studio Shop Banner -->
    <div class="studio-shop-banner">
      <div class="studio-shop-copy">
        <span class="shop-edition-badge">Raimage Studio Shop &amp; Editions</span>
        <h3>Acquire Prints &amp; Bespoke Design Assets</h3>
        <p>
          Museum-grade archival cotton prints, design token libraries, and bespoke hardware concept collaborations. Worldwide packaging &amp; signed editions.
        </p>
      </div>
      <div class="studio-shop-actions">
        <a href="mailto:sumitraiworks@gmail.com?subject=Raimage%20Shop%20Order%20Inquiry" class="btn btn-primary">
          <span>Inquire / Shop Editions</span>
          <span class="shahi-arrow">&nearr;</span>
        </a>
        <a href="contact.html" class="btn btn-secondary">Contact Sumit <span class="btn-key">[C]</span></a>
      </div>
    </div>

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
    return get_head("Playground (Design & Shop) — Sumit Rai", "playground") + get_nav("playground") + content + footer_html + f"<script>\n{global_js}\n{pg_js}\n</script>\n</body>\n</html>"

def build_contact():
    content = f"""
<main class="page-body">
  <div class="wrap-wide">
    
    <!-- HEADER -->
    <div style="margin-bottom:48px;">
      <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
        <span style="font-family:var(--font-mono); font-size:12px; font-weight:600; color:var(--accent);">[C]</span>
        <h1 style="font-size:32px; font-weight:700; letter-spacing:-0.03em; margin:0; color:var(--ink);">Contact</h1>
      </div>
      <p style="font-size:15px; color:var(--ink-soft); max-width:600px; line-height:1.6; margin:0;">
        Available for select product leadership, design advisory, and high-impact full-time roles worldwide.
      </p>
    </div>

    <!-- 3-TIER COLLABORATION TIERS -->
    <div class="work-tiers-list">
      <div class="work-tier-card">
        <div class="work-tier-grid">
          <div class="work-tier-left">
            <span style="font-family:var(--font-mono); font-size:11px; color:var(--ink-muted);">For Founders &amp; design leads</span>
            <span class="work-tier-num">01</span>
            <h3>Advisory &amp; coaching</h3>
            <div class="work-tier-lead">A thinking partner for the hard calls.</div>
            <p class="work-tier-sub">Product direction, design team structure, when to hire and when to automate with AI.</p>
          </div>
          <div class="work-tier-right">
            <ul>
              <li>Product direction and roadmap pressure-testing</li>
              <li>Design team structure and hiring strategy</li>
              <li>Design maturity and scalable token process coaching</li>
            </ul>
          </div>
        </div>
        <div class="work-tier-meta-row">
          <div>
            <div class="meta-label">FORMAT</div>
            <div class="meta-val">Monthly retainer or per session</div>
          </div>
          <div>
            <div class="meta-label">BEST FOR</div>
            <div class="meta-val">Founders without a design background, design leads at Series A/B</div>
          </div>
        </div>
      </div>

      <div class="work-tier-card">
        <div class="work-tier-grid">
          <div class="work-tier-left">
            <span style="font-family:var(--font-mono); font-size:11px; color:var(--ink-muted);">For Designers</span>
            <span class="work-tier-num">02</span>
            <h3>Design mentorship</h3>
            <div class="work-tier-lead">Focus on the right path for your career.</div>
            <p class="work-tier-sub">Honest feedback, portfolio critiques, and a clear path forward for your design craft.</p>
          </div>
          <div class="work-tier-right">
            <ul>
              <li>Portfolio and case study deep-dives</li>
              <li>Career positioning and narrative coaching</li>
              <li>Interview preparation and presentation coaching</li>
            </ul>
          </div>
        </div>
        <div class="work-tier-meta-row">
          <div>
            <div class="meta-label">FORMAT</div>
            <div class="meta-val">Bi-weekly or monthly 1:1 sessions</div>
          </div>
          <div>
            <div class="meta-label">BEST FOR</div>
            <div class="meta-val">Mid-level designers aiming for senior or staff, career pivoters</div>
          </div>
        </div>
      </div>

      <div class="work-tier-card">
        <div class="work-tier-grid">
          <div class="work-tier-left">
            <span style="font-family:var(--font-mono); font-size:11px; color:var(--ink-muted);">For Conferences &amp; teams</span>
            <span class="work-tier-num">03</span>
            <h3>Talks &amp; panels</h3>
            <div class="work-tier-lead">Stories from the work, not slides about it.</div>
            <p class="work-tier-sub">Product design, growth, and building with AI, told through real production casework.</p>
          </div>
          <div class="work-tier-right">
            <ul>
              <li>Conference talks and keynotes</li>
              <li>Panels and fireside conversations</li>
              <li>Internal team sessions and interactive workshops</li>
            </ul>
          </div>
        </div>
        <div class="work-tier-meta-row">
          <div>
            <div class="meta-label">FORMAT</div>
            <div class="meta-val">Keynote, panel or internal workshop</div>
          </div>
          <div>
            <div class="meta-label">BEST FOR</div>
            <div class="meta-val">Design and product conferences, meetups, team offsites</div>
          </div>
        </div>
      </div>
    </div>

    <!-- TICKET TEAR BANNER -->
    <div class="tear-banner">
      <div>
        <h3 style="font-size:17px; font-weight:600; margin:0 0 4px; color:var(--ink);">Book a mentorship session or discuss advisory</h3>
        <p style="font-size:13.5px; color:var(--ink-soft); margin:0;">Direct 1:1 sessions for design leads, founders and teams.</p>
      </div>
      <div style="display:flex; align-items:center; gap:16px;">
        <span class="tear-line">TEAR HERE &bull; &bull; &bull;</span>
        <a href="mailto:sumitraiworks@gmail.com?subject=Contact%20%26%20Collaboration%20Inquiry" class="btn btn-primary">
          <span>Get in Touch</span>
          <span class="shahi-arrow">&nearr;</span>
        </a>
      </div>
    </div>

    <!-- SUBSTACK PROMPT -->
    <div style="margin-top:40px; padding:24px; border:1px solid var(--line); border-radius:var(--radius-md); background:var(--surface); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
      <div>
        <h4 style="font-size:15px; font-weight:600; margin:0 0 4px; color:var(--ink);">Follow my writing on Substack</h4>
        <p style="font-size:13px; color:var(--ink-soft); margin:0;">Weekly reflections on product design, AI interfaces, and studio craft.</p>
      </div>
      <a href="https://isumitrai.substack.com/" target="_blank" rel="noopener" class="btn btn-secondary">
        <span>isumitrai.substack.com</span>
        <span class="shahi-arrow">&nearr;</span>
      </a>
    </div>

  </div>
</main>
"""
    return get_head("Contact — Sumit Rai", "contact") + get_nav("contact") + content + footer_html + f"<script>\n{global_js}\n</script>\n</body>\n</html>"

def main():
    pages = [
        ("index.html", build_index()),
        ("projects.html", build_projects()),
        ("about.html", build_about()),
        ("resume.html", build_resume()),
        ("resources.html", build_resources()),
        ("playground.html", build_playground()),
        ("contact.html", build_contact())
    ]
    for filename, html in pages:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {filename} successfully ({len(html)} bytes)")

if __name__ == "__main__":
    main()
