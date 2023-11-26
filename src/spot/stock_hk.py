# 实时行情数据-东财
# 接口: stock_hk_spot_em
# 目标地址: http://quote.eastmoney.com/center/gridlist.html#hk_stocks
# 描述: 所有港股的实时行情数据; 该数据有 15 分钟延时
# 限量: 单次返回最近交易日的所有港股的数据

import akshare as ak

stock_hk_spot_em_df = ak.stock_hk_spot_em()
print(stock_hk_spot_em_df)
