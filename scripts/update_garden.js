/**
 * update_garden.js
 * Reads data/garden.json and injects:
 *   1. A compact preview card between <!-- GARDEN_BENTO_START --> and <!-- GARDEN_BENTO_END --> in index.html
 *   2. Full garden-item rows between <!-- GARDEN_LIST_PLACEHOLDER_START --> and <!-- GARDEN_LIST_PLACEHOLDER_END --> in resources.html
 *   3. window.GARDEN_DATA script block in resources.html
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
const bentoRegex = /<!-- GARDEN_BENTO_START -->[\s\S]*?<!-- GARDEN_BENTO_END -->/;
if (bentoRegex.test(indexHtml)) {
  indexHtml = indexHtml.replace(bentoRegex, `<!-- GARDEN_BENTO_START -->\n${bentoCard}\n        <!-- GARDEN_BENTO_END -->`);
  fs.writeFileSync(indexPath, indexHtml, 'utf8');
  console.log('✅  Injected garden bento card into index.html');
} else {
  console.warn('⚠️   GARDEN_BENTO markers not found in index.html');
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

const listRegex = /<!-- GARDEN_LIST_PLACEHOLDER_START -->[\s\S]*?<!-- GARDEN_LIST_PLACEHOLDER_END -->/;
if (listRegex.test(resHtml)) {
  resHtml = resHtml.replace(listRegex, `<!-- GARDEN_LIST_PLACEHOLDER_START -->\n${rows}\n        <!-- GARDEN_LIST_PLACEHOLDER_END -->`);
  console.log(`✅  Injected ${notes.length} garden notes into resources.html`);
} else {
  console.warn('⚠️   GARDEN_LIST markers not found in resources.html');
}

// ── 3. resources.html: update window.GARDEN_DATA ─────────────────────────────
const newDataBlock = `window.GARDEN_DATA = ${JSON.stringify(notes)};`;
if (resHtml.includes('window.GARDEN_DATA =')) {
  resHtml = resHtml.replace(/window\.GARDEN_DATA\s*=\s*\[[\s\S]*?\];/, newDataBlock);
  console.log('✅  Updated window.GARDEN_DATA in resources.html');
}

fs.writeFileSync(resourcesPath, resHtml, 'utf8');
