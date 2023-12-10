<template>
    <el-descriptions :title="combination.name" :column="4">
        <el-descriptions-item label="创建时间" :span="4">{{ combination.createTime }}</el-descriptions-item>
        <el-descriptions-item label="股票数量" :span="2">{{ combination.stockCount }}</el-descriptions-item>
        <el-descriptions-item label="更新次数" :span="2">{{ combination.updateCount }}</el-descriptions-item>
        <el-descriptions-item label="更新方式" :span="2">{{ combination.updateMethod }}</el-descriptions-item>
        <el-descriptions-item label="最近更新时间" :span="2">{{ combination.updateTime }}</el-descriptions-item>
        <el-descriptions-item label="描述" :span="4">{{ combination.description }}</el-descriptions-item>
    </el-descriptions>
    <h4>组合配置</h4>
    <combinationSettingTable :setting-stocks="settingStocks"></combinationSettingTable>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import combinationSettingTable from './combinationSettingTable.vue';

// defineProps({
//     combination: Object
// })

const combination = ref({
    name: '组合名称',
    description: '组合描述',
    stockCount: 0,
    updateCount: 0,
    createTime: 'xxxx-xx-xx xx:xx:xx',
    updateTime: 'xxxx-xx-xx xx:xx:xx',
    updateMethod: '每周二上午 10:00',
})

const settingStocks = ref([]);

const generateRandomData = () => {
  return Array.from({ length: 7 }, (item, idx) => ({
    '代码': `00000${idx}`,
    '名称': `测试数据${idx}`,
    '最新价': (Math.random() * 100).toFixed(2),
    '总市值': (Math.random() * 10000).toFixed(2),
    '年初至今涨跌幅': (Math.random() * 100).toFixed(2),
    'eval_3y': (Math.random() * 1000).toFixed(2),
    'holding_ratio': (Math.random()).toFixed(2),
    'holding_count': Math.floor(Math.random() * 100)
  }))
}

onMounted(() => {
    const randomData = generateRandomData()
    settingStocks.value = randomData;
})

</script>

<style scoped>
</style>