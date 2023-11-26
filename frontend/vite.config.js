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
    proxy: {
      // 指定代理所有/api请求
      '/api': {
        // 代理请求之后的请求地址
        target: 'http://127.0.0.1:8000/',
        // 跨域
        changeOrigin: true
      }
    }
  }

})
