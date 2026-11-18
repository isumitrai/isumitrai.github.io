/**
 * update_garden.js
 * Reads data/garden.json and injects:
 *   1. A compact preview card at <!-- GARDEN_PLACEHOLDER --> in index.html (bento section)
 *   2. Full garden-item rows at <!-- GARDEN_LIST_PLACEHOLDER --> in resources.html
 *   3. window.GARDEN_DATA script at <!-- GARDEN_DATA_PLACEHOLDER --> in resources.html
 *      (falls back to replacing the existing inline window.GARDEN_DATA = [...] block)
 *
 * Run: node scripts/update_garden.js
 */

const fs   = require('fs');
const path = require('path');

const dataPath      = path.join(__dirname, '..', 'data', 'garden.json');
const indexPath     = path.join(__dirname, '..', 'index.html');
const resourcesPath = path.join(__dirname, '..', 'resources.html');

const notes = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
const first = notes[0];

// ── 1. index.html: compact bento preview card ─────────────────────────────────
const bentoCard = `        <a href="resources.html#garden" class="shahi-card" aria-label="Digital Garden">
          <span class="shahi-card-label">Digital Garden</span>
          <div class="garden-preview-stack">
            <div class="garden-preview-item">
              <span class="garden-tag">${first.topic}</span>
              <span class="garden-date">${first.date}</span>
            </div>
            <h3 style="font-size:14px; font-weight:600; line-height:1.4; margin:8px 0 4px; color:var(--ink);">${first.title}</h3>
            <p style="font-size:12.5px; color:var(--ink-soft); line-height:1.5; margin:0;">${first.hook}</p>
            <div style="margin-top:12px; font-size:12px; color:var(--accent); font-weight:600;">${notes.length} notes &nearr;</div>
          </div>
          <span class="shahi-card-key">G</span>
        </a>`;

let indexHtml = fs.readFileSync(indexPath, 'utf8');
if (indexHtml.includes('<!-- GARDEN_PLACEHOLDER -->')) {
  indexHtml = indexHtml.replace('<!-- GARDEN_PLACEHOLDER -->', bentoCard);
  fs.writeFileSync(indexPath, indexHtml, 'utf8');
  console.log('✅  Injected garden bento card into index.html');
} else {
  console.warn('⚠️   <!-- GARDEN_PLACEHOLDER --> not found in index.html — skipping');
}

// ── 2. resources.html: full garden-item list ──────────────────────────────────
const rows = notes.map(n => `        <div class="garden-item" onclick="openGardenNote('${n.id}')" role="button" tabindex="0" aria-label="Read ${n.title}">
          <div class="garden-left-meta">
            <span class="garden-tag">${n.topic}</span>
            <span class="garden-date">${n.date}</span>
          </div>
          <div class="garden-main-body">
            <h3 class="garden-title">${n.title}</h3>
            <p class="garden-snippet">${n.hook}</p>
          </div>
          <div class="garden-right-meta">
            <span class="garden-read-time">${n.read}</span>
            <span class="shahi-arrow">&nearr;</span>
          </div>
        </div>`).join('\n\n');

let resHtml = fs.readFileSync(resourcesPath, 'utf8');

if (resHtml.includes('<!-- GARDEN_LIST_PLACEHOLDER -->')) {
  resHtml = resHtml.replace('<!-- GARDEN_LIST_PLACEHOLDER -->', rows);
  console.log(`✅  Injected ${notes.length} garden notes into resources.html`);
} else {
  console.warn('⚠️   <!-- GARDEN_LIST_PLACEHOLDER --> not found — skipping list injection');
}

// ── 3. resources.html: replace inline window.GARDEN_DATA ─────────────────────
const newDataBlock = `window.GARDEN_DATA = ${JSON.stringify(notes)};`;

// Replace existing window.GARDEN_DATA = [...]; block (single line)
if (resHtml.includes('window.GARDEN_DATA =')) {
  resHtml = resHtml.replace(/window\.GARDEN_DATA\s*=\s*\[[\s\S]*?\];/, newDataBlock);
  console.log('✅  Updated window.GARDEN_DATA in resources.html');
} else if (resHtml.includes('<!-- GARDEN_DATA_PLACEHOLDER -->')) {
  resHtml = resHtml.replace('<!-- GARDEN_DATA_PLACEHOLDER -->', `<script>\n  ${newDataBlock}\n  </script>`);
  console.log('✅  Injected window.GARDEN_DATA script block');
} else {
  console.warn('⚠️   No GARDEN_DATA target found — skipping data injection');
}

fs.writeFileSync(resourcesPath, resHtml, 'utf8');
