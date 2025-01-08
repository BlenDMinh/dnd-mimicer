import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import './polyfills'
import path from 'path';

console.log('Vite configuration loaded');
console.log('Current directory:', __dirname);
console.log('Resolved dist directory:', path.resolve(__dirname, 'dist'));

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  preview: {
    port: 8080,
    strictPort: true,
  },
  server: {
    port: 8080,
    strictPort: true,
    host: true,
    origin: "http://0.0.0.0:8080",
  },
  build: {
    rollupOptions: {
      output: {
        dir: path.resolve(__dirname, 'dist'),
        entryFileNames: 'bundle.js',
        format: 'iife',
      }
    }
  }
})