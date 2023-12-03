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
                <el-button :icon="Search" class="btn" @click="handlerSearchBtn">搜索</el-button>
                <el-button :icon="Delete" class="btn" @click="handlerClearBtn" type="danger">清空</el-button>
            </el-col>
        </el-row>
        <el-table v-if="selectedStocks.length > 0" :data="selectedStocks" style="width: 100%">
            <el-table-column prop="stockCode" label="股票代码" />
            <el-table-column prop="stockName" label="股票名称" />
            <el-table-column fixed="right" label="Operations">
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
        <h1>设置</h1>
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
import { getStockName } from '@/service/stock'

let firstStep = 1;
let lastStep = 3;
const active = ref(1)

const next = () => {
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
</script>
<style scoped>
.btn {
    margin: 0 0;
}
</style>