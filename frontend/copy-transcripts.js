#!/usr/bin/env node

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Create public/data/transcripts directory if it doesn't exist
const publicTranscriptsDir = path.join(__dirname, 'public', 'data', 'transcripts');
const srcTranscriptsDir = path.join(__dirname, 'src', 'data', 'transcripts');

if (!fs.existsSync(publicTranscriptsDir)) {
  fs.mkdirSync(publicTranscriptsDir, { recursive: true });
}

// Copy all JSON files from src/data/transcripts to public/data/transcripts
try {
  const files = fs.readdirSync(srcTranscriptsDir);
  const jsonFiles = files.filter(file => file.endsWith('.json'));
  
  jsonFiles.forEach(file => {
    const srcPath = path.join(srcTranscriptsDir, file);
    const destPath = path.join(publicTranscriptsDir, file);
    fs.copyFileSync(srcPath, destPath);
  });
  
  console.log(`✅ Copied ${jsonFiles.length} transcript files to public directory`);
} catch (error) {
  console.error('❌ Error copying transcript files:', error.message);
  process.exit(1);
}
