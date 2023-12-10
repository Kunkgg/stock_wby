<template>
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
defineProps({settingStocks: Object})
</script>