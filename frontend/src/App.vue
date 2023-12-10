<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <el-header style="height: 5rem;" class="width-80">
    <h1 class="header-title">WBY Stock</h1>
    <el-menu
      default-active="combination"
      :router="true"
      mode="horizontal"
    >
      <el-menu-item index="combination" :route="{name: 'combination'}">投资组合</el-menu-item>
      <el-menu-item index="net-asset-value" :route="{name: 'net-asset-value'}">净值跟踪</el-menu-item>
      <el-menu-item index="user" :route="{name: 'user'}">用户</el-menu-item>
      <el-menu-item index="about" :route="{name: 'about'}">关于</el-menu-item>
    </el-menu>
  </el-header>
  <el-main class="width-80">
    <router-view></router-view>
  </el-main>
</template>

<script>
import { Refresh } from '@element-plus/icons-vue'

export default {
  data() {
    return {
      activeName: 'Spot',
      updateTime: 'xxxx-xx-xx xx:xx:xx',
      total: 0,
      showingCount: 0,
      refreshLoading: false,
      spotKeyIndex: 0,
      customKeyIndex: 0,
    }
  },
  methods: {
  },
  mounted() {
  }
}
</script>

<style scoped>
.header-title {
  text-align: center;
  margin: 4rem auto 2rem auto;
}

.header-subtitle {
  justify-content: center;
  align-items: center;
}

.header-subtitle .el-text {
  margin: 0 1rem;
}
.width-80 {
  width: 80%;
  margin: 2rem auto;
}
</style>
