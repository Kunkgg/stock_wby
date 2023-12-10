from enum import Enum
from typing import Optional

import pandas as pd
from fastapi import FastAPI, HTTPException

from src.consts import TIME_FMT
from src.store import (
    save_stock_all_spot,
    read_stock_all_spot,
    read_stock_all_spot_updatetime,
    read_stock_all_spot_total
)


class Market(str, Enum):
    A = "A"
    HK = "HK"
    ALL = "ALL"
    A_HK = "A,HK"
    HK_A = "HK,A"



save_stock_all_spot()
app = FastAPI()


@app.get("/api/stock/spot/{stock_code}")
async def get_stock_spot_by_code(stock_code):
    update_time = read_stock_all_spot_updatetime()
    df = read_stock_all_spot()
    if df is None or df.empty or update_time is None:
        raise HTTPException(status_code=404, detail="No data")
    item = df.loc[df["代码"] == stock_code]

    if item.empty:
        raise HTTPException(status_code=404, detail="No data")

    item.fillna(value="", inplace=True)
    item_dict = item.to_dict(orient="records")
    return {
        "update_time": update_time.strftime(TIME_FMT),
        "spot_data": item_dict,
    }


@app.get("/api/stock/spot")
async def get_stock_spot(
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

    df = df.astype("object").where(pd.notnull(df), "")
    # Calculate start and end indices for the slice of data to return
    start = (page - 1) * page_size
    end = start + page_size

    # Select the slice of data
    df = df.iloc[start:end]
    total = df.shape[0]
    df_dict = df.to_dict(orient="records")

    return {
        "update_time": update_time.strftime(TIME_FMT),
        "spot_data": df_dict,
        "page": page,
        "page_size": page_size,
        "total": total,
        "max_page": cal_max_page(total, page_size),
    }


@app.post("/api/stock/spot/refresh")
async def refresh_stock_spot():
    data = save_stock_all_spot()
    if data["spot_data"] is None:
        raise HTTPException(status_code=404, detail="Refresh stock spot failed")
    return {"update_time": data["update_time"], "total": len(data["spot_data"])}


def cal_max_page(total, page_size):
    if total % page_size == 0:
        return total // page_size
    else:
        return total // page_size + 1


@app.get("/api/stock/name")
async def get_stock_name(
    page: int = 1,
    page_size: int = 500,
    stock_name: Optional[str] = None,
    stock_code: Optional[str] = None,
):
    update_time = read_stock_all_spot_updatetime()
    df = read_stock_all_spot()
    if df is None or df.empty or update_time is None:
        raise HTTPException(status_code=404, detail="No data")

    if stock_name:
        if "," in stock_name:
            stock_name_l = stock_name.split(",")
        else:
            stock_name_l = [stock_name]
        df = df[df["名称"].isin(stock_name_l)]

    if stock_code:
        if "," in stock_code:
            stock_code_l = stock_code.split(",")
        else:
            stock_code_l = [stock_code]
        df = df[df["代码"].isin(stock_code_l)]

    df = df[["代码", "名称"]]
    df = df.astype("object").where(pd.notnull(df), "")
    start = (page - 1) * page_size
    end = start + page_size

    # Select the slice of data
    df = df.iloc[start:end]
    total = df.shape[0]
    names = df.to_records(index=False).tolist()

    return {
        "update_time": update_time.strftime(TIME_FMT),
        "names": names,
        "page": page,
        "page_size": page_size,
        "total": total,
        "max_page": cal_max_page(total, page_size),
    }


@app.get("/api/stock/updatetime")
async def get_stock_updatetime():
    update_time = read_stock_all_spot_updatetime()
    if update_time is None:
        raise HTTPException(status_code=404, detail="No data")
    return {
        "update_time": update_time.strftime(TIME_FMT),
    }


@app.get("/api/stock/total")
async def get_stock_total():
    total = read_stock_all_spot_total()
    if total is None:
        raise HTTPException(status_code=404, detail="No data")
    return {
        "total": total,
    }


@app.get("/api/stock/status")
async def get_stock_status():
    update_time = read_stock_all_spot_updatetime()
    total = read_stock_all_spot_total()
    if update_time is None or total is None:
        raise HTTPException(status_code=404, detail="No data")
    return {
        "update_time": update_time.strftime(TIME_FMT),
        "total": total,
    }
