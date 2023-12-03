<template>
  <el-steps :active="active" align-center>
    <el-step title="Step 1" description="设置组合名称" />
    <el-step title="Step 2" description="选股" />
    <el-step title="Step 3" description="配置估值、持股比例、持股数" />
  </el-steps>
  <el-main>
    <template v-if="isFirstStep">
        <el-form label-position="top">
        <el-form-item label="组合名称">
            <el-input v-model="combinationName" placeholder="请输入组合名称"></el-input>
        </el-form-item>
        <el-form-item label="组合描述">
            <el-input
                v-model="combinationDescription"
                :autosize="{ minRows: 2, maxRows: 4 }"
                type="textarea"
                placeholder="请输入组合描述"
            />
        </el-form-item>
        </el-form>
    </template>
    <template v-else-if="active === 2">
        <el-row>
            <el-col :span="20">
                <el-input
                v-model="searchStocks"
                placeholder="输入股票名称, 多个股票以逗号分隔"
                class="search-input"
                :clearable="searchStocks.length > 0"
                />
            </el-col>
            <el-col :span="4">
                <el-button :icon="Search" class="btn" @click="handlerSearchBtn">添加</el-button>
                <el-button :icon="Delete" class="btn" @click="handlerClearBtn" type="danger">清空</el-button>
            </el-col>
        </el-row>
        <el-table v-if="selectedStocks.length > 0" :data="selectedStocks" style="width: 100%">
            <el-table-column type="index" label="#"/>
            <el-table-column prop="stockCode" label="股票代码" />
            <el-table-column prop="stockName" label="股票名称" />
            <el-table-column fixed="right" label="操作">
            <template #default="scope">
                <el-button
                link
                type="primary"
                size="small"
                @click.prevent="deleteRow(scope.$index)"
                >
                删除
                </el-button>
            </template>
            </el-table-column>
        </el-table>
    </template>
    <template v-else>
         <vxe-table
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
    <el-row style="margin-top: 2rem;">
        <el-button :disabled="isFirstStep" style="margin-top: auto 12px;" @click="prev" type="primary">上一步</el-button>
        <el-button :disabled="isLastStep" style="margin-top: auto 12px;" @click="next" type="primary">下一步</el-button>
    </el-row>
  </el-main>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue'
import { Search } from '@element-plus/icons-vue'
import { Delete } from '@element-plus/icons-vue'
import { getStockName, getStockSpotList } from '@/service/stock'

let firstStep = 1;
let lastStep = 3;
const active = ref(1)
let settingStocks = ref([])

const next = () => {
  if (active.value === 2 && selectedStocks.value.length > 0) {
    let stockCodes = selectedStocks.value.map((item) => item.stockCode)
    console.log(active.value)
    let params = {
        "stock_code": stockCodes.join(",")
    }
    getStockSpotList(params).then((res) => {
        settingStocks.value = res.data.spot_data
    })
  }
  if (active.value < lastStep) active.value++
}
const prev = () => {
  if (active.value > firstStep) active.value--
}
const isLastStep = computed(() => {
  return active.value === lastStep
})
const isFirstStep = computed(() => {
  return active.value === firstStep
})

// step 1
const combinationName = ref('')
const combinationDescription = ref('')

// step 2
const searchStocks = ref('')
let selectedStocks = ref([])
const handlerClearBtn = () => {
    selectedStocks.value = []
    searchStocks.value = ''
}
const deleteRow = (index: number) => {
  selectedStocks.value.splice(index, 1)
}
const handlerSearchBtn = () => {
    let stockNameQueryStr = searchStocks.value.replace(/\s+/g, '')
    if (stockNameQueryStr === '') {
        return
    }
    let params = {
        "stock_name": stockNameQueryStr
    }
    getStockName(params).then((res) => {
        res.data.names.forEach((item) => {
            if (selectedStocks.value.find((element) => element.stockCode === item[0])) {
                return
            }
            selectedStocks.value.push({
                stockCode: item[0],
                stockName: item[1]
            });
        })
    })
}

// step 3


// expose
defineExpose({
  combinationName,
  combinationDescription,
  settingStocks,
})
</script>
<style scoped>
.btn {
    margin: 0 0;
}
</style>