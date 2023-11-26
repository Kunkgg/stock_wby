<template>
  <h1>Spot</h1>
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
export default {
  data() {
    return {
      td: [
        {
          序号: 18,
          代码: "832171",
          名称: "志晟信息",
          最新价: 11.51,
          涨跌幅: 29.91,
          涨跌额: 2.65,
          成交量: 167648,
          成交额: 178572661.15,
          振幅: 28.33,
          最高: 11.51,
          最低: 9,
          今开: 9.5,
          昨收: 8.86,
          量比: 3.66,
          换手率: 24.96,
          "市盈率-动态": -38.14,
          市净率: 3.11,
          总市值: 1153684535,
          流通市值: 773048812,
          涨速: 0,
          "5分钟涨跌": 0,
          "60日涨跌幅": 206.12,
          年初至今涨跌幅: 170.19,
          market: "A",
        },
        {
          序号: 18,
          代码: "832171",
          名称: "志晟信息",
          最新价: 11.51,
          涨跌幅: 29.91,
          涨跌额: 2.65,
          成交量: 167648,
          成交额: 178572661.15,
          振幅: 28.33,
          最高: 11.51,
          最低: 9,
          今开: 9.5,
          昨收: 8.86,
          量比: 3.66,
          换手率: 24.96,
          "市盈率-动态": -38.14,
          市净率: 3.11,
          总市值: 1153684535,
          流通市值: 773048812,
          涨速: 0,
          "5分钟涨跌": 0,
          "60日涨跌幅": 206.12,
          年初至今涨跌幅: 170.19,
          market: "A",
        },
      ],
    };
  },
};
</script>
