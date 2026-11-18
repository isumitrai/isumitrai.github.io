import re

with open("generate_pages.py", "r") as f:
    content = f.read()

# We want to swap the order of TEXT TOP and IMAGE BOTTOM inside the JS projects.forEach
# The easiest way is to just replace the whole card.innerHTML string in generate_pages.py.

old_html = """      card.innerHTML = `
        <!-- TEXT TOP -->
        <div class="proj-body">
          <div class="proj-eyebrow">${p.tag}</div>
          <h3>${p.title}</h3>
          <p class="proj-desc">${p.summary}</p>
          <div class="proj-meta-row">
            <div class="tech-row">
              ${p.tech.map(t => `<span class="tech-chip">${t}</span>`).join('')}
            </div>
            <span class="proj-metric">${p.metric}</span>
          </div>
        </div>
        <!-- IMAGE BOTTOM -->
        <div class="proj-image">
          ${p.image
            ? `<img src="${p.image}" alt="${p.title}" loading="lazy" />`
            : `<div class="img-fallback">${caseIconSvg}</div>`
          }
          <span class="proj-cta">View case study →</span>
        </div>
      `;"""

new_html = """      card.innerHTML = `
        <!-- IMAGE TOP -->
        <div class="proj-image">
          ${p.image
            ? `<img src="${p.image}" alt="${p.title}" loading="lazy" />`
            : `<div class="img-fallback">${caseIconSvg}</div>`
          }
        </div>
        <!-- TEXT BOTTOM -->
        <div class="proj-body">
          <div class="proj-eyebrow">${p.tag}</div>
          <h3>${p.title}</h3>
          <p class="proj-desc">${p.summary}</p>
          <div class="proj-meta-row" style="margin-bottom:8px;">
            <div class="tech-row">
              ${p.tech.map(t => `<span class="tech-chip">${t}</span>`).join('')}
            </div>
            <span class="proj-metric">${p.metric}</span>
          </div>
          <span class="clay-btn primary proj-cta-full">View case study →</span>
        </div>
      `;"""

if old_html in content:
    content = content.replace(old_html, new_html)
    with open("generate_pages.py", "w") as f:
        f.write(content)
    print("Patched generate_pages.py successfully.")
else:
    print("Could not find the HTML to replace in generate_pages.py.")

