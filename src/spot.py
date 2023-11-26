import akshare as ak
import pandas as pd

from src.logger import logger


def stock_zh_a_spot() -> pd.DataFrame:
    """
    实时行情数据-东财
    沪深京 A 股
    接口: stock_zh_a_spot_em
    目标地址: http://quote.eastmoney.com/center/gridlist.html#hs_a_board
    描述: 东方财富网-沪深京 A 股-实时行情数据
    限量: 单次返回所有沪深京 A 股上市公司的实时行情数据
    """
    a_df = ak.stock_zh_a_spot_em()
    logger.info("stock_zh_a_spot: %s, %s", a_df.shape[0], a_df.shape[1])
    return a_df


def stock_hk_spot() -> pd.DataFrame:
    """
    实时行情数据-东财
    接口: stock_hk_spot_em
    目标地址: http://quote.eastmoney.com/center/gridlist.html#hk_stocks
    描述: 所有港股的实时行情数据; 该数据有 15 分钟延时
    限量: 单次返回最近交易日的所有港股的数据
    """
    hk_df = ak.stock_hk_spot_em()
    logger.info("stock_hk_spot: %s, %s", hk_df.shape[0], hk_df.shape[1])
    return hk_df


def stock_all_spot() -> pd.DataFrame:
    """
    返回所有 A 股和港股的实时行情数据
    """
    a_df = stock_zh_a_spot()
    a_df['market'] = 'A'
    hk_df = stock_hk_spot()
    hk_df['market'] = 'HK'
    all_df = pd.concat([a_df, hk_df], axis=0, ignore_index=True)
    logger.info("stock_all_spot: %s, %s", all_df.shape[0], all_df.shape[1])
    return all_df
