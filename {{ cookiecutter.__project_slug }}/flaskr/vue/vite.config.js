import { defineConfig } from 'vite'
import { fileURLToPath, URL } from 'node:url'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig(({ command, mode, ssrBuild }) => {
  const config = {
    plugins: [vue()],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    },
    build: {
      outDir: '../static/',
      emptyOutDir: true,
      manifest: true,
      rollupOptions: {
        input: 'src/main.js',
        output: {
          entryFileNames: '[name].js',
          assetFileNames: 'assets/[name].[ext]'
        }
      }
    }
  }
  return config
})
