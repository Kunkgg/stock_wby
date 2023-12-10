<template>
    <CombinationRecordTable :records="records"></CombinationRecordTable>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import CombinationRecordTable from './CombinationRecordTable.vue';

const records = ref([]);
const generateRandomData = () => {
  return Array.from({ length: 7 }, (item, idx) => ({
    'stock_code': `00000${idx}`,
    'stock_name': `测试数据${idx}`,
    'buy_point': (Math.random() * 100).toFixed(2),
    'sell_point': (Math.random() * 10000).toFixed(2),
    'price': (Math.random() * 100).toFixed(2),
    'market_value': (Math.random() * 10000).toFixed(2),
    'change_percent_1y': (Math.random() * 1).toFixed(2),
    'eval_3y': (Math.random() * 1000).toFixed(2),
    'holding_ratio': (Math.random()).toFixed(2),
    'holding_count': Math.floor(Math.random() * 100),
  }))
}

onMounted(() => {
    records.value = generateRandomData();
})

</script>