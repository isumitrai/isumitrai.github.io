/**
 * update_playground.js
 * Reads data/playground.json and injects pg-card-rich cards into playground.html
 * at the <!-- PLAYGROUND_PLACEHOLDER --> comment.
 *
 * Run: node scripts/update_playground.js
 */

const fs   = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, '..', 'data', 'playground.json');
const htmlPath = path.join(__dirname, '..', 'playground.html');

const items = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

// ── Build playground cards ────────────────────────────────────────────────────
const cards = items.map(item => {
  const footer = item.shopItem
    ? `<div style="margin-top:14px; padding-top:12px; border-top:1px solid var(--line); display:flex; justify-content:space-between; align-items:center;">
              <span class="shop-edition-badge">${item.shopEdition}</span>
              <a href="${item.inquiryLink}" class="pg-shop-btn">
                <span>Inquire Print</span>
                <span class="shahi-arrow">&nearr;</span>
              </a>
            </div>`
    : `<div class="pg-foot">
              <span>${item.studio}</span>
              <span class="shahi-arrow">&nearr;</span>
            </div>`;

  return `      <article class="pg-card-rich" data-category="${item.category}">
        <div class="pg-preview">
          <img src="${item.image}" alt="${item.title}" loading="lazy" />
        </div>
        <div class="pg-meta-body">
          <div class="pg-cat-row">
            <span class="pg-tag">${item.tags.join(' &middot; ')}</span>
            <span class="pg-year">${item.year}</span>
          </div>
          <h3>${item.title}</h3>
          <p>${item.description}</p>
          ${footer}
        </div>
      </article>`;
}).join('\n\n');

// ── Inject into HTML ──────────────────────────────────────────────────────────
let html = fs.readFileSync(htmlPath, 'utf8');

if (!html.includes('<!-- PLAYGROUND_PLACEHOLDER -->')) {
  console.error('❌  <!-- PLAYGROUND_PLACEHOLDER --> not found in playground.html');
  process.exit(1);
}

html = html.replace('<!-- PLAYGROUND_PLACEHOLDER -->', cards);
fs.writeFileSync(htmlPath, html, 'utf8');

console.log(`✅  Injected ${items.length} playground cards into playground.html`);
