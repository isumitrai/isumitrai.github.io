/**
 * update_resume.js
 * Reads data/experience.json and data/resume.json to update resume.html
 * ensuring all sections requested by Sumit Rai are present:
 * - Professional Summary
 * - Career Timeline (Work Experience)
 * - Selected Projects
 * - Core Competencies & Skills
 * - Education
 * - Certifications
 * - View Resume & Download Resume buttons
 *
 * Run: node scripts/update_resume.js
 */

const fs   = require('fs');
const path = require('path');

const expPath    = path.join(__dirname, '..', 'data', 'experience.json');
const resumePath = path.join(__dirname, '..', 'data', 'resume.json');
const htmlPath   = path.join(__dirname, '..', 'resume.html');

const experiences = JSON.parse(fs.readFileSync(expPath, 'utf8'));
const resumeData  = JSON.parse(fs.readFileSync(resumePath, 'utf8'));

// Build experience entries
const expHtml = experiences.map(exp => `        <div class="resume-entry" data-id="${exp.id}">
          <div class="entry-header">
            <div>
              <h3 class="entry-role">${exp.role}</h3>
              <div class="entry-org">${exp.company} &middot; ${exp.type}</div>
            </div>
            <span class="entry-date">${exp.period}</span>
          </div>
          <p class="entry-desc">${exp.description}</p>
          ${exp.highlights && exp.highlights.length ? `
          <ul class="entry-highlights" style="margin: 8px 0 0 18px; padding: 0; font-size: 13.5px; color: var(--ink-soft); line-height: 1.6;">
            ${exp.highlights.map(h => `<li>${h}</li>`).join('\n            ')}
          </ul>` : ''}
        </div>`).join('\n\n');

// Build projects entries
const projectsHtml = resumeData.selectedProjects.map(p => `          <div class="resume-entry" style="padding: 16px 0; border-bottom: 1px solid var(--line);">
            <div class="entry-header">
              <div>
                <h3 class="entry-role" style="font-size: 16px;">${p.name}</h3>
                <div class="entry-org">${p.category}</div>
              </div>
              <a href="${p.url}" class="shahi-card-link" style="font-size: 12.5px; font-weight: 600; color: var(--accent);">View Case Study &rarr;</a>
            </div>
            <p class="entry-desc" style="margin-top: 6px;">${p.summary}</p>
          </div>`).join('\n');

// Build skills entries
const skillsHtml = resumeData.skills.map(s => `          <div class="skill-group">
            <h4>${s.group}</h4>
            <p>${s.items}</p>
          </div>`).join('\n');

// Build education entries
const eduHtml = resumeData.education.map(e => `          <div class="resume-entry" style="padding: 14px 0; border-bottom: 1px solid var(--line);">
            <div class="entry-header">
              <div>
                <h3 class="entry-role" style="font-size: 15px;">${e.degree}</h3>
                <div class="entry-org">${e.institution}</div>
              </div>
              <span class="entry-date">${e.period}</span>
            </div>
          </div>`).join('\n');

// Build certifications entries
const certHtml = resumeData.certifications.map(c => `          <div class="resume-entry" style="padding: 14px 0; border-bottom: 1px solid var(--line);">
            <div class="entry-header">
              <div>
                <h3 class="entry-role" style="font-size: 15px;">${c.title}</h3>
                <div class="entry-org">${c.issuer}</div>
              </div>
              <span class="entry-date">${c.year}</span>
            </div>
          </div>`).join('\n');

const mainBody = `    <div class="resume-view-wrap">
      <div class="resume-top-bar">
        <div>
          <span class="eyebrow"><span class="dot"></span> Curriculum Vitae</span>
          <h1>${resumeData.name}</h1>
          <p class="resume-subhead">${resumeData.subtitle}</p>
        </div>
        <div class="resume-actions" style="display:flex; gap:10px; align-items:center; flex-wrap:wrap;">
          <a href="${resumeData.pdfPath}" target="_blank" rel="noopener" class="btn btn-secondary">
            <span>View PDF</span>
            <span class="shahi-arrow">&nearr;</span>
          </a>
          <a href="${resumeData.pdfPath}" download class="btn btn-primary">
            <span>Download PDF</span>
            <span class="shahi-arrow">&darr;</span>
          </a>
        </div>
      </div>

      <div class="resume-section-block">
        <h2 class="resume-sec-title">Professional Summary</h2>
        <p style="font-size: 15px; line-height: 1.7; color: var(--ink-soft); max-width: 780px; margin: 0;">
          ${resumeData.summary}
        </p>
      </div>

      <div class="resume-section-block">
        <h2 class="resume-sec-title">Professional Experience (Career Timeline)</h2>
${expHtml}
      </div>

      <div class="resume-section-block">
        <h2 class="resume-sec-title">Selected Projects</h2>
        <div>
${projectsHtml}
        </div>
      </div>

      <div class="resume-section-block">
        <h2 class="resume-sec-title">Core Competencies &amp; Toolkit</h2>
        <div class="skills-grid-clean">
${skillsHtml}
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 28px; margin-top: 36px;">
        <div class="resume-section-block" style="margin-top: 0;">
          <h2 class="resume-sec-title">Education</h2>
          <div>
${eduHtml}
          </div>
        </div>

        <div class="resume-section-block" style="margin-top: 0;">
          <h2 class="resume-sec-title">Certifications &amp; Focus</h2>
          <div>
${certHtml}
          </div>
        </div>
      </div>

    </div>`;

let html = fs.readFileSync(htmlPath, 'utf8');

// Replace the inner wrapper of resume-view-wrap
const targetRegex = /<div class="resume-view-wrap">[\s\S]*?<\/div>\s*<\/div>\s*<\/main>/;
if (targetRegex.test(html)) {
  html = html.replace(targetRegex, `${mainBody}\n  </div>\n</main>`);
  fs.writeFileSync(htmlPath, html, 'utf8');
  console.log('✅  Updated entire resume.html with all structured sections.');
} else {
  console.warn('⚠️  Could not find resume-view-wrap in resume.html');
}
