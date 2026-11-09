#!/usr/bin/env python3
"""
Script to update generate_pages.py with:
1. RESOURCES dataset (curated books/reads with customizable Amazon links).
2. Updated get_head with 8+ and 12+ years experience.
3. Updated get_nav with Resources [B] and all shortcut badges.
4. Identical audited footer across all pages.
5. Global keyboard navigation supporting W, A, R, B, P, C, Esc.
6. Clean build_index with zero divider duplicity (separate brands and tools sections).
7. build_resources() function.
8. Updated build_about() and build_resume() with 8+ and 12+ years metrics.
"""

import sys

with open("generate_pages.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add RESOURCES right after TOOLS = [ ... ]
resources_code = '''
# -------------------------------------------------------------
# Curated Resources List (Books, Systems & Design Architecture)
# You can update the amazon link for each book with your own affiliate link anytime!
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
        "link": "https://www.amazon.com/dp/B08M3S6W8R"  # Update with your Amazon affiliate link
    },
    {
        "id": "res-2",
        "title": "The Design of Everyday Things",
        "author": "Don Norman",
        "category": "Product Strategy",
        "format": "Classic Hardcover",
        "desc": "The definitive bible on cognitive ergonomics, affordances, signifiers, and designing products that humans intuitively understand.",
        "takeaway": "When users fail, it is not user error — it is faulty interface design.",
        "link": "https://www.amazon.com/dp/0465050654"  # Update with your Amazon affiliate link
    },
    {
        "id": "res-3",
        "title": "The Elements of Typographic Style",
        "author": "Robert Bringhurst",
        "category": "Design Craft",
        "format": "Reference Book",
        "desc": "Widely revered as the definitive text on typographic craft, rhythm, proportional scales, and the architecture of the printed page.",
        "takeaway": "Typography exists to honor content and guide human comprehension.",
        "link": "https://www.amazon.com/dp/0881792128"  # Update with your Amazon affiliate link
    },
    {
        "id": "res-4",
        "title": "A Philosophy of Software Design",
        "author": "John Ousterhout",
        "category": "Systems & Tech",
        "format": "Technical Book",
        "desc": "A masterclass on managing system complexity, modular interfaces, and why shallow modules ruin large systems.",
        "takeaway": "Modules should be deep: simple interfaces hiding profound internal power.",
        "link": "https://www.amazon.com/dp/1732102201"  # Update with your Amazon affiliate link
    },
    {
        "id": "res-5",
        "title": "Universal Principles of Design",
        "author": "William Lidwell, Kritina Holden, Jill Butler",
        "category": "Design Craft",
        "format": "Visual Reference",
        "desc": "An authoritative encyclopedia of 125 cognitive, perceptual, and structural laws governing human interaction.",
        "takeaway": "Master Fitts\\' Law, Hick\\'s Law, and progressive disclosure to reduce cognitive load.",
        "link": "https://www.amazon.com/dp/1592535879"  # Update with your Amazon affiliate link
    },
    {
        "id": "res-6",
        "title": "Shape Up: Stop Running in Circles and Ship Work That Matters",
        "author": "Ryan Singer (Basecamp)",
        "category": "Product Strategy",
        "format": "Product Methodology",
        "desc": "A revolutionary framework for product teams: fixed time, variable scope, 6-week cycles, and building with shaped appetites.",
        "takeaway": "Never start building until problems are shaped with clear boundaries.",
        "link": "https://www.amazon.com/dp/B081N4R3G9"  # Update with your Amazon affiliate link
    },
    {
        "id": "res-7",
        "title": "Inspired: How to Create Tech Products Customers Love",
        "author": "Marty Cagan",
        "category": "Product Strategy",
        "format": "Management Guide",
        "desc": "The gold standard for product discovery, continuous customer validation, and building empowered product teams.",
        "takeaway": "Validate value, usability, feasibility, and viability before writing code.",
        "link": "https://www.amazon.com/dp/1119387507"  # Update with your Amazon affiliate link
    },
    {
        "id": "res-8",
        "title": "Designing Data-Intensive Applications",
        "author": "Martin Kleppmann",
        "category": "Systems & Tech",
        "format": "Engineering Architecture",
        "desc": "The definitive exploration of storage engines, distributed consensus, data models, and scalable systems reliability.",
        "takeaway": "A designer who understands backend latency and data models designs 10x better products.",
        "link": "https://www.amazon.com/dp/1449373321"  # Update with your Amazon affiliate link
    },
    {
        "id": "res-9",
        "title": "Grid Systems in Graphic Design",
        "author": "Josef Müller-Brockmann",
        "category": "Design Craft",
        "format": "Classic Monograph",
        "desc": "The Swiss design masterwork outlining mathematical grid systems for layout, typography, and architectural coherence.",
        "takeaway": "The grid is a structural aid, not a straightjacket — it creates rhythm and order.",
        "link": "https://www.amazon.com/dp/3721201450"  # Update with your Amazon affiliate link
    },
    {
        "id": "res-10",
        "title": "Show Your Work!",
        "author": "Austin Kleon",
        "category": "Mindset & Craft",
        "format": "Illustrated Essay",
        "desc": "A punchy guide to working in public, building a digital garden, and sharing your creative process openly.",
        "takeaway": "Become a documentarian of what you do every day; generosity builds lasting influence.",
        "link": "https://www.amazon.com/dp/076117897X"  # Update with your Amazon affiliate link
    },
    {
        "id": "res-11",
        "title": "A Pattern Language",
        "author": "Christopher Alexander",
        "category": "Systems & Tech",
        "format": "Architectural Classic",
        "desc": "The seminal architectural philosophy that directly inspired object-oriented programming, design systems, and modular components.",
        "takeaway": "Reusable patterns solve recurring spatial and informational tensions.",
        "link": "https://www.amazon.com/dp/0195019199"  # Update with your Amazon affiliate link
    },
    {
        "id": "res-12",
        "title": "Creativity, Inc.",
        "author": "Ed Catmull & Amy Wallace",
        "category": "Mindset & Craft",
        "format": "Hardcover Memoir",
        "desc": "The Pixar co-founder\\'s masterclass on creative culture, candid feedback (Braintrust), and protecting early fragile ideas.",
        "takeaway": "Early drafts are never great; psychological safety allows teams to turn raw ideas into masterpieces.",
        "link": "https://www.amazon.com/dp/0812993015"  # Update with your Amazon affiliate link
    }
]
'''

print("Ready to update generate_pages.py")
