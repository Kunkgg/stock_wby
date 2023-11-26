import akshare as ak
import pandas as pd


def stock_zh_a_spot() -> pd.DataFrame:
    """
    实时行情数据-东财
    沪深京 A 股
    接口: stock_zh_a_spot_em
    目标地址: http://quote.eastmoney.com/center/gridlist.html#hs_a_board
    描述: 东方财富网-沪深京 A 股-实时行情数据
    限量: 单次返回所有沪深京 A 股上市公司的实时行情数据
    """
    return ak.stock_zh_a_spot_em()


def stock_hk_spot() -> pd.DataFrame:
    """
    实时行情数据-东财
    接口: stock_hk_spot_em
    目标地址: http://quote.eastmoney.com/center/gridlist.html#hk_stocks
    描述: 所有港股的实时行情数据; 该数据有 15 分钟延时
    限量: 单次返回最近交易日的所有港股的数据
    """
    return ak.stock_hk_spot_em()


def stock_all_spot() -> pd.DataFrame:
    """
    返回所有 A 股和港股的实时行情数据
    """
    a_df = stock_zh_a_spot()
    hk_df = stock_hk_spot()
    all_df = pd.concat([a_df, hk_df], axis=0, ignore_index=True)
    return all_df

