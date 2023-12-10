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
    <vxe-table
        v-if="settingStocks.length > 0"
        show-overflow
        :data="settingStocks"
        :column-config="{resizable: true}"
        :edit-config="{trigger: 'click', mode: 'cell'}">
        <vxe-column type="seq" width="60"></vxe-column>
        <vxe-column field="代码" title="代码"></vxe-column>
        <vxe-column field="名称" title="名称"></vxe-column>
        <vxe-column field="最新价" title="最新价" :edit-render="{autofocus: '.vxe-input--inner'}">
            <template #edit="{ row }">
            <vxe-input v-model="row['最新价']" type="number"></vxe-input>
            </template>
        </vxe-column>
        <vxe-column field="总市值" title="总市值" :edit-render="{autofocus: '.vxe-input--inner'}">
            <template #edit="{ row }">
            <vxe-input v-model="row['总市值']" type="number"></vxe-input>
            </template>
        </vxe-column>
        <vxe-column field="年初至今涨跌幅" title="年内涨跌幅" :edit-render="{autofocus: '.vxe-input--inner'}">
            <template #edit="{ row }">
            <vxe-input v-model="row['年初至今涨跌幅']" type="number"></vxe-input>
            </template>
        </vxe-column>
        <vxe-column field="eval_3y" title="三年后合理估值" :edit-render="{autofocus: '.vxe-input--inner'}">
            <template #edit="{ row }">
            <vxe-input v-model="row['eval_3y']" type="number"></vxe-input>
            </template>
        </vxe-column>
        <vxe-column field="holding_ratio" title="持股比例" :edit-render="{autofocus: '.vxe-input--inner'}">
            <template #edit="{ row }">
            <vxe-input v-model="row['holding_ratio']" type="number"></vxe-input>
            </template>
        </vxe-column>
        <vxe-column field="holding_count" title="持股数" :edit-render="{autofocus: '.vxe-input--inner'}">
            <template #edit="{ row }">
            <vxe-input v-model="row['holding_count']" type="number"></vxe-input>
            </template>
        </vxe-column>
    </vxe-table>
</template>
<script setup>
import { ref, onMounted } from 'vue';

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