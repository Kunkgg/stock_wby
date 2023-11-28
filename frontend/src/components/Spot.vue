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
      <el-table-column label="1年内卖的">
        <template #default="scope"> 待计算 </template>
      </el-table-column>
    </el-table>
  </el-row>
</template>
<script>
import { getStockSpot, getStockSpotList, getStockName } from "@/service/stock.js";

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
    getStockNames() {


    },
    handleSelect() {

    }
  },
};
</script>
