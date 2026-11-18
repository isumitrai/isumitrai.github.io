/**
 * update_home.js
 * Reads data/projects.json and injects project cards into index.html
 * between <!-- PROJECTS_PLACEHOLDER_START --> and <!-- PROJECTS_PLACEHOLDER_END -->.
 *
 * Run: node scripts/update_home.js
 */

const fs   = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, '..', 'data', 'projects.json');
const htmlPath = path.join(__dirname, '..', 'index.html');

const { projects } = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

// ── Build project cards matching Sumit Rai's design language ──────────────────
const cards = projects.map(p => `      <article class="proj-card" onclick="window.location.href='${p.url}'" role="button" tabindex="0" aria-label="View case study for ${p.title}">
        <div class="proj-image">
          <img src="${p.image}" alt="${p.title}" loading="lazy" />
        </div>
        <div class="proj-body">
          <div class="proj-meta">
            <span class="proj-category">${p.category}</span>
            <span class="proj-year">${p.year}</span>
          </div>
          <h3 class="proj-title">${p.title}</h3>
          <p class="proj-desc">${p.description}</p>
          <div class="proj-link-row">
            <span class="proj-view-link">View Case Study <span class="shahi-arrow">&nearr;</span></span>
            <div class="proj-tech-tags">
              ${p.tags.map(t => `<span class="proj-tag">${t}</span>`).join('')}
            </div>
          </div>
        </div>
      </article>`).join('\n\n');

// ── Inject into HTML ──────────────────────────────────────────────────────────
let html = fs.readFileSync(htmlPath, 'utf8');

const markerRegex = /<!-- PROJECTS_PLACEHOLDER_START -->[\s\S]*?<!-- PROJECTS_PLACEHOLDER_END -->/;

if (markerRegex.test(html)) {
  html = html.replace(markerRegex, `<!-- PROJECTS_PLACEHOLDER_START -->\n${cards}\n      <!-- PROJECTS_PLACEHOLDER_END -->`);
  fs.writeFileSync(htmlPath, html, 'utf8');
  console.log(`✅  Injected ${projects.length} project cards into index.html`);
} else {
  console.error('❌  <!-- PROJECTS_PLACEHOLDER_START --> ... <!-- PROJECTS_PLACEHOLDER_END --> not found in index.html');
  process.exit(1);
}
