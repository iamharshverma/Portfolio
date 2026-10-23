const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log('[Build] Starting Harsh Verma Portfolio build process...');

// 0. Verify speaker page integrity
try {
  console.log('[Build] Verifying speaker page integrity...');
  execSync('python3 scripts/check_speaker_page.py', { stdio: 'inherit' });
} catch (err) {
  console.error('[Build] Critical error: Speaker page validation failed!', err.message);
  process.exit(1);
}

// 1. Run site synchronization
try {
  console.log('[Build] Synchronizing site statistics and metrics...');
  execSync('python3 scripts/sync_site_stats.py', { stdio: 'inherit' });
} catch (err) {
  console.warn('[Build] Warning during sync_site_stats:', err.message);
}

// 1b. Generate Board Biography PDF
try {
  console.log('[Build] Generating Board Biography PDF...');
  execSync('python3 scripts/create_board_bio_pdf.py', { stdio: 'inherit' });
} catch (err) {
  console.warn('[Build] Warning during create_board_bio_pdf:', err.message);
}

// 2. Prepare output directories atomically to avoid serving partial dist states
const rootDir = path.resolve(__dirname, '..');
const distDir = path.join(rootDir, 'dist');
const buildDir = path.join(rootDir, 'build');
const distTmp = path.join(rootDir, '.dist_tmp');

console.log('[Build] Preparing staging directory: ' + distTmp);
if (fs.existsSync(distTmp)) {
  fs.rmSync(distTmp, { recursive: true, force: true });
}
fs.mkdirSync(distTmp, { recursive: true });

// Copy function supporting files and directories recursively
function copyRecursive(src, dest) {
  const stats = fs.statSync(src);
  if (stats.isDirectory()) {
    if (!fs.existsSync(dest)) {
      fs.mkdirSync(dest, { recursive: true });
    }
    const entries = fs.readdirSync(src);
    for (const entry of entries) {
      if (entry === 'node_modules' || entry === '.git' || entry === 'dist' || entry === 'build' || entry === '.dist_tmp') continue;
      copyRecursive(path.join(src, entry), path.join(dest, entry));
    }
  } else {
    fs.copyFileSync(src, dest);
  }
}

// 3. Populate staging directory with all website assets
const itemsToCopy = [
  'images',
  'css',
  'js',
  'data',
  'fonts',
  'assets',
  'files'
];

// Copy directories
for (const item of itemsToCopy) {
  const srcPath = path.join(rootDir, item);
  if (fs.existsSync(srcPath)) {
    console.log(`[Build] Staging directory: ${item}`);
    copyRecursive(srcPath, path.join(distTmp, item));
  }
}

// Copy all root HTML, JSON, JS, TS, XML, ICO, TXT, SVG files
const rootEntries = fs.readdirSync(rootDir);
let copiedFilesCount = 0;

for (const entry of rootEntries) {
  const ext = path.extname(entry).toLowerCase();
  const validExtensions = ['.html', '.json', '.js', '.ts', '.xml', '.ico', '.txt', '.svg', '.png', '.jpg', '.jpeg', '.webp'];
  const srcPath = path.join(rootDir, entry);

  if (fs.statSync(srcPath).isFile()) {
    if (validExtensions.includes(ext) || entry === 'CNAME') {
      fs.copyFileSync(srcPath, path.join(distTmp, entry));
      copiedFilesCount++;
    }
  }
}

console.log(`[Build] Staged ${copiedFilesCount} root files into staging directory`);

// 4. Atomically swap staging into dist and build
if (fs.existsSync(distDir)) {
  fs.rmSync(distDir, { recursive: true, force: true });
}
fs.renameSync(distTmp, distDir);

if (fs.existsSync(buildDir)) {
  fs.rmSync(buildDir, { recursive: true, force: true });
}
console.log('[Build] Mirroring dist/ to build/ for multi-target artifact uploaders...');
copyRecursive(distDir, buildDir);

// Verify index.html exists in dist
if (fs.existsSync(path.join(distDir, 'index.html'))) {
  const indexSize = fs.statSync(path.join(distDir, 'index.html')).size;
  console.log(`[Build] Success! Valid build artifacts generated in dist/ (index.html: ${indexSize} bytes).`);
} else {
  console.error('[Build] Error: dist/index.html was not created!');
  process.exit(1);
}
