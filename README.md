# Sumit Rai — Portfolio Content System

This portfolio uses a **data-driven generation workflow**: all repeating sections
are stored as plain JSON files. A set of Node scripts read those files and
inject generated HTML into static pages.

---

## Quick Start

```bash
# Update every section at once
npm run update

# Or update individual sections
npm run update:home        # → index.html (projects)
npm run update:resources   # → resources.html (books)
npm run update:writing     # → writing.html (articles)
npm run update:playground  # → playground.html (pg cards)
npm run update:garden      # → resources.html (garden notes + window.GARDEN_DATA)
```

---

## Data Files

| File | Page | What it controls |
|------|------|-----------------|
| `data/projects.json` | `index.html` | Selected work cards |
| `data/resources.json` | `resources.html` | Curated books + gear setup |
| `data/writing.json` | `writing.html` | Articles / essays |
| `data/playground.json` | `playground.html` | Playground / shop items |
| `data/garden.json` | `resources.html` | Digital Garden notes |
| `data/experience.json` | *(resume page, future)* | Career timeline |
| `data/work_with_me.json` | *(work-with-me page, future)* | Service cards |

---

## How to Add Content

### Add a new project
Open `data/projects.json` and add an object to the `projects` array:

```json
{
  "id": "my-new-project",
  "title": "My New Project",
  "category": "Mobile App • Branding",
  "year": 2026,
  "image": "./assets/proj_new.png",
  "description": "Short description shown on the homepage card.",
  "tags": ["Mobile", "UI/UX"],
  "url": "projects.html#my-new-project",
  "featured": true
}
```

Then run `npm run update:home`.

---

### Add a new book
Open `data/resources.json` and add to the `books` array:

```json
{
  "id": "book-slug",
  "title": "Book Title",
  "author": "Author Name",
  "category": "Design Craft",
  "format": "Hardcover",
  "description": "One-line description.",
  "insight": "Key takeaway from the book.",
  "link": "https://www.amazon.com/dp/XXXXXXX"
}
```

Then run `npm run update:resources`.

---

### Add a new article
Open `data/writing.json`:

```json
{
  "id": "w-4",
  "title": "Article Title",
  "intro": "One sentence intro shown on the card.",
  "date": "2026-11-18",
  "readTime": "5 min read",
  "category": "Product Craft",
  "image": "",
  "externalUrl": "https://medium.com/your-article"
}
```

Leave `externalUrl` empty to link to an internal `writing-detail.html?id=w-4` page.  
Then run `npm run update:writing`.

---

### Add a new Garden note
Open `data/garden.json`:

```json
{
  "id": "g-7",
  "title": "Note Title",
  "topic": "Design Craft",
  "date": "18.11.26",
  "read": "3 min read",
  "hook": "One-line teaser shown in the list.",
  "content": "<p>Full HTML content of the note.</p>"
}
```

Then run `npm run update:garden`.

---

### Add a new Playground item
Open `data/playground.json`:

```json
{
  "id": "pg-7",
  "title": "New Creation",
  "category": "UI & AI Concepts",
  "tags": ["AI", "Concept"],
  "year": 2026,
  "image": "./assets/pg_005.jpg",
  "description": "Short description of the creation.",
  "studio": "Raimage Studio Lab",
  "shopItem": false,
  "shopPrice": "",
  "shopEdition": "",
  "inquiryLink": ""
}
```

For shop items set `shopItem: true`, fill `shopEdition` and `inquiryLink`.  
Then run `npm run update:playground`.

---

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/update_all.js` | Runs all scripts in sequence |
| `scripts/update_home.js` | Injects project cards → `index.html` |
| `scripts/update_resources.js` | Injects book cards → `resources.html` |
| `scripts/update_writing.js` | Injects article cards → `writing.html` |
| `scripts/update_playground.js` | Injects pg cards → `playground.html` |
| `scripts/update_garden.js` | Injects garden rows + `window.GARDEN_DATA` → `resources.html` |

---

## Placeholders

Each script looks for a specific HTML comment and replaces it with generated markup.

| Placeholder | File | Script |
|-------------|------|--------|
| `<!-- PROJECTS_PLACEHOLDER -->` | `index.html` | `update_home.js` |
| `<!-- RESOURCES_PLACEHOLDER -->` | `resources.html` | `update_resources.js` |
| `<!-- WRITING_PLACEHOLDER -->` | `writing.html` | `update_writing.js` |
| `<!-- PLAYGROUND_PLACEHOLDER -->` | `playground.html` | `update_playground.js` |
| `<!-- GARDEN_LIST_PLACEHOLDER -->` | `resources.html` | `update_garden.js` |

> **Important:** After running a script the placeholder is replaced with live HTML.
> To re-run a script, restore the placeholder comment first (or keep a backup of
> the original HTML). Future versions will use a restore step automatically.

---

## Resume

The PDF resume is stored at `assets/Sumit_Rai_Resume.pdf`.  
The Resume page links to it for both View and Download actions.  
To update: replace the file at that path and keep the same filename.

---

## Deployment

The site is a static GitHub Pages site deployed from this repository.  
Push changes to the `main` branch to publish.
