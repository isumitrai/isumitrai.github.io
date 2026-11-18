/**
 * update_home.js
 * Reads data/projects.json and injects project cards into index.html
 * at the <!-- PROJECTS_PLACEHOLDER --> comment.
 *
 * Run: node scripts/update_home.js
 */

const fs   = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, '..', 'data', 'projects.json');
const htmlPath = path.join(__dirname, '..', 'index.html');

const { projects } = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

// ── Build project cards ───────────────────────────────────────────────────────
const cards = projects.map(p => `        <a href="${p.url}" class="proj-card" data-id="${p.id}">
          <div class="proj-img-wrap">
            <img src="${p.image}" alt="${p.title}" loading="lazy" />
          </div>
          <div class="proj-card-body">
            <div class="proj-card-meta">
              <span class="proj-cat">${p.category}</span>
              <span class="proj-year">${p.year}</span>
            </div>
            <h3 class="proj-title">${p.title}</h3>
            <p class="proj-desc">${p.description}</p>
            <div class="proj-tags">
              ${p.tags.map(t => `<span class="proj-tag">${t}</span>`).join('')}
            </div>
          </div>
        </a>`).join('\n\n');

const grid = `<div class="proj-grid">\n${cards}\n      </div>`;

// ── Inject into HTML ──────────────────────────────────────────────────────────
let html = fs.readFileSync(htmlPath, 'utf8');

if (!html.includes('<!-- PROJECTS_PLACEHOLDER -->')) {
  console.error('❌  <!-- PROJECTS_PLACEHOLDER --> not found in index.html');
  process.exit(1);
}

html = html.replace('<!-- PROJECTS_PLACEHOLDER -->', grid);
fs.writeFileSync(htmlPath, html, 'utf8');

console.log(`✅  Injected ${projects.length} project cards into index.html`);
