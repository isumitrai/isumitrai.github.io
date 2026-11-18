/**
 * update_all.js
 * Runs all section update scripts in sequence.
 * Run: node scripts/update_all.js  (or: npm run update)
 */

const { execSync } = require('child_process');
const path = require('path');

const scripts = [
  'update_home.js',
  'update_resources.js',
  'update_writing.js',
  'update_playground.js',
  'update_garden.js',
  'update_resume.js'
];

console.log('🚀  Rebuilding all data-driven sections...\n');

for (const script of scripts) {
  const scriptPath = path.join(__dirname, script);
  try {
    const out = execSync(`node "${scriptPath}"`, { encoding: 'utf8' });
    process.stdout.write(out);
  } catch (err) {
    console.error(`❌  Error running ${script}:`);
    console.error(err.stderr || err.message);
    process.exit(1);
  }
}

console.log('\n✨  All sections updated successfully.');
