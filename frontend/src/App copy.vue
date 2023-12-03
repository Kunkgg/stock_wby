<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <el-header style="height: 5rem;">
    <h1 class="header-title">WBY Stock</h1>
    <el-row class="header-subtitle">
      <el-text type="info">Update Time: {{ updateTime }}</el-text>
      <el-text type="info">Total: {{ total }}</el-text>
      <el-button
        :icon="Refresh"
        :loading="refreshLoading"
        type="primary"
        circle
        size="small"
        @click="handleRefreshClick()"/>
    </el-row>
  </el-header>
  <el-main class="width-80">
    <el-tabs v-model="activeName" @tab-click="handleTabClick">
      <el-tab-pane label="Spot" name="Spot">
        <Spot :key="`spot-${spotKeyIndex}`" :total="total"></Spot>
      </el-tab-pane>
      <el-tab-pane label="Custom" name="custom">
        <Custom :key="`custom-${customKeyIndex}`" :keyIndex="customKeyIndex"></Custom>
      </el-tab-pane>
    </el-tabs>
  </el-main>
</template>

<script>
import Spot from './components/Spot.vue'
import Custom from './components/Custom.vue'
import { Refresh } from '@element-plus/icons-vue'
import { getStockStatus, refreshStockSpot } from "./service/stock";

export default {
  components: {
    Spot,
    Custom
  },
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
    handleTabClick(tab, event) {
      console.log(tab, event);
    },
    handleRefreshClick() {
      this.refreshLoading = true;
      this.updateTime = 'xxxx-xx-xx xx:xx:xx';
      this.total = 0;

      refreshStockSpot().then((res) => {
        this.updateTime = res.data.update_time;
        this.total = res.data.total;
        this.refreshLoading = false;
        this.spotKeyIndex += 1;
        this.customKeyIndex += 1;
      });
    },
  },
  mounted() {
    // getStockStatus().then((res) => {
    //   this.updateTime = res.data.update_time;
    //   this.total = res.data.total;
    // });
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
