/**
 * update_writing.js
 * Reads data/writing.json and injects article cards into writing.html
 * between <!-- WRITING_PLACEHOLDER_START --> and <!-- WRITING_PLACEHOLDER_END -->.
 *
 * Run: node scripts/update_writing.js
 */

const fs   = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, '..', 'data', 'writing.json');
const htmlPath = path.join(__dirname, '..', 'writing.html');

const articles = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

function formatDate(isoStr) {
  const d = new Date(isoStr);
  return d.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' });
}

// ── Build article cards ───────────────────────────────────────────────────────
const cards = articles.map(a => {
  const ctaHtml = a.externalUrl
    ? `<a href="${a.externalUrl}" target="_blank" rel="noopener" class="writing-article-cta">
            Read on Medium <span class="shahi-arrow">&nearr;</span>
          </a>`
    : `<span class="writing-article-cta">
            Read Article <span class="shahi-arrow">&rarr;</span>
          </span>`;

  const href = a.externalUrl ? a.externalUrl : '#';
  const target = a.externalUrl ? ' target="_blank" rel="noopener"' : '';

  return `      <a href="${href}"${target} class="writing-article-card" data-category="${a.category}" data-id="${a.id}">
        <div class="writing-article-top">
          <span class="writing-article-cat">${a.category}</span>
          <span class="writing-article-date">${formatDate(a.date)}</span>
          <span class="writing-article-read-time">${a.readTime}</span>
        </div>
        <h2 class="writing-article-title">${a.title}</h2>
        <p class="writing-article-intro">${a.intro}</p>
        ${ctaHtml}
      </a>`;
}).join('\n\n');

// ── Inject into HTML ──────────────────────────────────────────────────────────
let html = fs.readFileSync(htmlPath, 'utf8');

const markerRegex = /<!-- WRITING_PLACEHOLDER_START -->[\s\S]*?<!-- WRITING_PLACEHOLDER_END -->/;

if (markerRegex.test(html)) {
  html = html.replace(markerRegex, `<!-- WRITING_PLACEHOLDER_START -->\n${cards}\n      <!-- WRITING_PLACEHOLDER_END -->`);
  fs.writeFileSync(htmlPath, html, 'utf8');
  console.log(`✅  Injected ${articles.length} articles into writing.html`);
} else {
  console.error('❌  <!-- WRITING_PLACEHOLDER_START --> ... <!-- WRITING_PLACEHOLDER_END --> not found in writing.html');
  process.exit(1);
}
