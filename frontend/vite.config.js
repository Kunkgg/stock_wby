import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: true,
    port: 3000,
    proxy: {
      // 指定代理所有/api请求
      '/api': {
        // 代理请求之后的请求地址
        target: 'http://backend:8000/',
        // 跨域
        changeOrigin: true
      }
    }
  }

})
