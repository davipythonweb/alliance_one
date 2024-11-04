import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    assetsDir: 'static',  // Isso criará uma pasta 'static' dentro de 'dist'
  },
});

// Isso fará com que os arquivos estáticos sejam colocados dentro de uma subpasta chamada static na dist.