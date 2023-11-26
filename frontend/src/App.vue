<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <el-header>
    <h1 class="header-title">WBY Stock</h1>
  </el-header>
  <el-main class="width-80">
    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
      <el-tab-pane label="Custom" name="custom">
        <Custom></Custom>
      </el-tab-pane>
      <el-tab-pane label="Spot" name="Spot">
        <Spot></Spot>
      </el-tab-pane>
    </el-tabs>
  </el-main>
</template>

<script>
import Spot from './components/Spot.vue'
import Custom from './components/Custom.vue'

export default {
  components: {
    Spot,
    Custom
  },
  data() {
    return {
      activeName: 'Spot'
    }
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    }
  }
}
</script>

<style scoped>
.header-title {
  text-align: center;
  margin: 4rem;
}
.width-80 {
  width: 80%;
  margin: 2rem auto;
}
</style>
