<template>
  <el-table :data="td" style="width: 100%">
    <el-table-column prop="名称" label="名称" />
    <el-table-column prop="最新价" label="最新价" />
    <el-table-column prop="总市值" label="总市值" />
    <el-table-column prop="年初至今涨跌幅" label="年内涨跌幅" />
    <el-table-column label="持股比例">
        <template #default="scope">
            待查
        </template>
        </el-table-column>
    <el-table-column prop="market" label="market" />
    <el-table-column label="3年后估值">
        <template #default="scope">
            待设置
        </template>
    </el-table-column>
    <el-table-column label="理想买点">
        <template #default="scope">
            待计算
        </template>
    </el-table-column>
    <el-table-column label="1年内卖的">
        <template #default="scope">
            待计算
        </template>
    </el-table-column>
  </el-table>
</template>
<script>
import { getStockSpot, getStockSpotList } from "@/service/stock.js";

export default {
  data() {
    return {
      td: [],
    };
  },
  mounted() {
    // getStockSpot('000001').then((res) => {
    //   this.td = res.data.spot_data;
    // });
    const params = {
      page: 1,
      page_size: 10,
    };
    getStockSpotList(params).then((res) => {
      this.td = res.data.spot_data;
    });
  },
};
</script>
