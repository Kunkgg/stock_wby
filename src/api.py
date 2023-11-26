from enum import Enum
from typing import Optional
from fastapi import FastAPI, HTTPException

from src.store import (
    read_stock_all_spot,
    read_stock_all_spot_updatetime,
    save_stock_all_spot,
)


class Market(str, Enum):
    A = "A"
    HK = "HK"
    ALL = "ALL"
    A_HK = "A,HK"
    HK_A = "HK,A"


save_stock_all_spot()
app = FastAPI()


@app.get("/stock/spot/{stock_code}")
async def get_stock_spot_by_code(stock_code):
    update_time = read_stock_all_spot_updatetime()
    df = read_stock_all_spot()
    if df is None or df.empty or update_time is None:
        raise HTTPException(status_code=404, detail="No data")
    item = df.loc[df["代码"] == stock_code]

    if item.empty:
        raise HTTPException(status_code=404, detail="No data")

    item.fillna(value='', inplace=True)
    item_dict = item.to_dict(orient="records")
    return {
        "update_time": update_time,
        "spot_data": item_dict,
    }


@app.get("/stock/spot")
async def read_stock_spot(
    page: int = 1,
    page_size: int = 50,
    stock_code: Optional[str] = None,
    stock_name: Optional[str] = None,
    market: Optional[Market] = None,
):
    update_time = read_stock_all_spot_updatetime()
    df = read_stock_all_spot()
    if df is None or df.empty or update_time is None:
        raise HTTPException(status_code=404, detail="No data")

    if stock_code:
        if "," in stock_code:
            stock_code_l = stock_code.split(",")
        else:
            stock_code_l = [stock_code]
        df = df[df["代码"].isin(stock_code_l)]

    if stock_name:
        if "," in stock_name:
            stock_name_l = stock_name.split(",")
        else:
            stock_name_l = [stock_name]
        df = df[df["名称"].isin(stock_name_l)]

    if market:
        if market in [Market.ALL, Market.A_HK, Market.HK_A]:
            market_l = ["A", "HK"]
        else:
            market_l = [market]
        df = df[df["market"].isin(market_l)]

    df.fillna(value='', inplace=True)
    # Calculate start and end indices for the slice of data to return
    start = (page - 1) * page_size
    end = start + page_size

    # Select the slice of data
    df = df.iloc[start:end]

    df_dict = df.to_dict(orient="records")

    return {
        "update_time": update_time,
        "spot_data": df_dict,
        "page": page,
        "page_size": page_size,
    }
