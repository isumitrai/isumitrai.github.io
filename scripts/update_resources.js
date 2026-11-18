/**
 * update_resources.js
 * Reads data/resources.json and injects book cards into resources.html
 * between <!-- RESOURCES_PLACEHOLDER_START --> and <!-- RESOURCES_PLACEHOLDER_END -->.
 *
 * Run: node scripts/update_resources.js
 */

const fs   = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, '..', 'data', 'resources.json');
const htmlPath = path.join(__dirname, '..', 'resources.html');

const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

// ── Build book cards ──────────────────────────────────────────────────────────
const bookCards = data.books.map(b => `      <article class="resource-card" data-category="${b.category}">
        <div class="resource-card-header">
          <span class="resource-cat-tag">${b.category}</span>
          <span class="resource-format-tag">${b.format}</span>
        </div>
        <h3 class="resource-title">${b.title}</h3>
        <div class="resource-author">${b.author}</div>
        <p class="resource-desc">${b.description}</p>
        <div class="resource-takeaway">
          <strong>Key insight:</strong> ${b.insight}
        </div>
        <div class="resource-action-row">
          <a href="${b.link}" target="_blank" rel="noopener" class="resource-amazon-btn" title="View ${b.title} on Amazon">
            <span>Get on Amazon</span>
            <span class="arrow shahi-arrow">&nearr;</span>
          </a>
          <span class="resource-format-tag">Curated Read</span>
        </div>
      </article>`).join('\n\n');

// ── Inject into HTML ──────────────────────────────────────────────────────────
let html = fs.readFileSync(htmlPath, 'utf8');

const markerRegex = /<!-- RESOURCES_PLACEHOLDER_START -->[\s\S]*?<!-- RESOURCES_PLACEHOLDER_END -->/;

if (markerRegex.test(html)) {
  html = html.replace(markerRegex, `<!-- RESOURCES_PLACEHOLDER_START -->\n${bookCards}\n      <!-- RESOURCES_PLACEHOLDER_END -->`);
  fs.writeFileSync(htmlPath, html, 'utf8');
  console.log(`✅  Injected ${data.books.length} book cards into resources.html`);
} else {
  console.error('❌  <!-- RESOURCES_PLACEHOLDER_START --> ... <!-- RESOURCES_PLACEHOLDER_END --> not found in resources.html');
  process.exit(1);
}
