const { chromium } = require('playwright');
const AxeBuilder = require('@axe-core/playwright').default;
const fs = require('fs');
const path = require('path');
const url = require('url');

async function getHtmlFiles(dir, fileList = []) {
  const files = await fs.promises.readdir(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = await fs.promises.stat(filePath);
    if (stat.isDirectory()) {
      await getHtmlFiles(filePath, fileList);
    } else if (file.endsWith('.html') && !file.endsWith('404.html')) {
      fileList.push(filePath);
    }
  }
  return fileList;
}

async function run() {
  const siteDir = path.join(process.cwd(), 'site');
  if (!fs.existsSync(siteDir)) {
    console.error(`Error: Site directory not found at ${siteDir}. Make sure to build the site first.`);
    process.exit(1);
  }

  const htmlFiles = await getHtmlFiles(siteDir);
  if (htmlFiles.length === 0) {
    console.log('No HTML files found to scan.');
    return;
  }

  console.log(`Starting scan of ${htmlFiles.length} HTML files...`);
  const browser = await chromium.launch();
  const context = await browser.newContext();
  let hasViolations = false;
  
  const CONCURRENCY = 8;
  const page = await context.newPage();
  for (let i = 0; i < htmlFiles.length; i++) {
    const file = htmlFiles[i];
    const fileUrl = url.pathToFileURL(file).href;
    console.log(`[${i+1}/${htmlFiles.length}] Scanning ${fileUrl}...`);
    try {
      await page.goto(fileUrl, { waitUntil: 'load' });
      const results = await new AxeBuilder({ page })
        .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
        .analyze();

      if (results.violations.length > 0) {
        hasViolations = true;
        console.error(`\nAccessibility violations found in ${fileUrl}:`);
        for (const violation of results.violations) {
          console.error(`\nRule: ${violation.id} (${violation.impact})`);
          console.error(`Description: ${violation.description}`);
          console.error(`Help URL: ${violation.helpUrl}`);
          for (const node of violation.nodes) {
            console.error(`  - Target: ${node.target.join(', ')}`);
            console.error(`    HTML: ${node.html}`);
            if (node.failureSummary) {
              console.error(`    Summary: ${node.failureSummary}`);
            }
          }
        }
      }
    } catch (err) {
      console.error(`Error scanning ${fileUrl}:`, err);
    }
  }
  await page.close();

  await browser.close();

  if (hasViolations) {
    console.error('\nAccessibility scan failed with WCAG 2.1 Level AA violations.');
    process.exit(1);
  } else {
    console.log('\nAccessibility scan passed! No WCAG violations found.');
  }
}

run().catch(err => {
  console.error('Unhandled error:', err);
  process.exit(1);
});
