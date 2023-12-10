<template>
    <el-table v-if="records.length > 0" :data="records" style="width: 100%">
        <el-table-column type="index" label="#"/>
        <el-table-column prop="stock_code" label="股票代码" />
        <el-table-column prop="stock_name" label="股票名称" />
        <el-table-column prop="buy_point" label="理想买点" />
        <el-table-column prop="sell_point" label="理想卖点" />
        <el-table-column prop="price" label="股价" />
        <el-table-column prop="market_value" label="总市值" />
        <el-table-column prop="change_percent_1y" label="年内涨跌幅" />
        <el-table-column prop="eval_3y" label="三年后合理估值" />
        <el-table-column prop="holding_ratio" label="持股比例" />
        <el-table-column prop="holding_count" label="持股数" />
    </el-table>
</template>
<script setup>
defineProps({
    records: Array
})
</script>