<template>
  <el-row>
    <el-autocomplete
      v-model="state"
      :fetch-suggestions="getStockNames"
      placeholder="请输入股票代码或名称"
      @select="handleSelect"
    />
  </el-row>
  <el-row>
    <el-table
      :data="td"
      style="width: 100%"
      v-el-table-infinite-scroll="loadMore"
      :infinite-scroll-disabled="disabledScrollLoad"
      height="500px"
      :cell-style="cellStyle"
      :header-cell-style="headerCellStyle"
      @row-dblclick="handleRowDblclick"
    >
      <el-table-column prop="名称" label="名称" />
      <el-table-column prop="最新价" label="最新价" />
      <el-table-column prop="总市值" label="总市值" />
      <el-table-column prop="年初至今涨跌幅" label="年内涨跌幅" />
      <el-table-column label="持股比例">
        <template #default="scope"> 待设置 </template>
      </el-table-column>
      <el-table-column label="3年后估值">
        <template #default="scope"> 待设置 </template>
      </el-table-column>
      <el-table-column label="理想买点">
        <template #default="scope"> 待计算 </template>
      </el-table-column>
      <el-table-column label="1年内卖点">
        <template #default="scope"> 待计算 </template>
      </el-table-column>
    </el-table>
  </el-row>

  <el-dialog v-model="dialogFormVisible" :title="selectStockName">
    <el-form :model="form">
      <el-form-item label="持股比例" :label-width="formLabelWidth">
        <el-input v-model="form.equityRatio" autocomplete="off" />
      </el-form-item>
      <el-form-item label="3年后估值" :label-width="formLabelWidth">
        <el-input v-model="form.valuationAfterThreeYear" autocomplete="off" />
      </el-form-item>
      <el-form-item label="计算公式" :label-width="formLabelWidth">
        <el-input v-model="form.calcFormula" autocomplete="off" />
      </el-form-item>
      <el-divider></el-divider>
      <p v-if="this.selectBuyPoint">
        <el-text type="success">理想买点: {{ this.selectBuyPoint }}</el-text>
      </p>
      <p v-if="this.selectSellPoint">
        <el-text type="success">1年内卖点: {{ this.selectBuyPoint }}</el-text>
      </p>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>
<script>
import { getStockSpotList, getStockName } from "@/service/stock.js";

export default {
  props: {
    total: Number,
  },
  data() {
    return {
      state: "",
      stockNameList: [],
      td: [],
      page: 1,
      page_size: 10,
      dialogFormVisible: false,
      formLabelWidth: "120px",
      form: {
        equityRatio: '',
        valuationAfterThreeYear: '',
        calcFormula: '',
    },
    selectStockName: 'xxx Stock',
    selectBuyPoint: 'xxx Buy',
    selectSellPoint: 'xxx Sell',
    };
  },
  mounted() {
    const params = {
      page: 1,
      page_size: 30,
    };
    getStockSpotList(params).then((res) => {
      this.td = res.data.spot_data;
    });
  },
  computed: {
    disabledScrollLoad() {
      return this.noMore;
    },
    noMore() {
      return this.td.length >= this.total;
    },
  },
  methods: {
    loadMore() {
      if (this.disabledScrollLoad) {
        return;
      }

      this.page += 1;
      const params = {
        page: this.page,
        page_size: this.page_size,
      };
      getStockSpotList(params).then((res) => {
        this.td = this.td.concat(res.data.spot_data);
      });
    },
    cellStyle({ row, column, rowIndex, columnIndex }) {
      if (column.label === "持股比例" || column.label === "3年后估值") {
        return {
          color: "#409eff",
          backgroundColor: "#f5f7fa",
        };
      } else if (column.label === "理想买点" || column.label === "1年内卖点") {
        return {
          color: "#529b2e",
          backgroundColor: "#f5f7fa",
        };
      }
    },
    headerCellStyle({ row, column, rowIndex, columnIndex }) {
      if (column.label === "持股比例" || column.label === "3年后估值") {
        return {
          color: "#ecf5ff",
          backgroundColor: "#409eff",
        };
      } else if (column.label === "理想买点" || column.label === "1年内卖点") {
        return {
          color: "#f0f9eb",
          backgroundColor: "#529b2e",
        };
      }
    },
    handleRowDblclick(row, column, event) {
      this.selectStockName = row['名称']
      this.selectBuyPoint = row['buyPoint']
      this.selectSellPoint = row['sellPoint']
      this.dialogFormVisible = true;
    },
    getStockNames() {
    },
    handleSelect() {
    }
  },
};
</script>

<style scoped>
.el-table .cell-class-name {
  color: #409eff !important;
  background-color: red;
}
</style>