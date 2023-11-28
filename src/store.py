import json
import pandas as pd
from datetime import datetime
from redis import Redis

from src.spot import stock_all_spot
from src.consts import TIME_FMT

r = Redis(host="redis", port=6379, db=0)


# 2. 把 DataFrame 对象转换成 json 字符串
def df_to_json(df):
    return json.dumps(df.to_dict(orient="records"))


# 3. 把 json 字符串保存到 redis 中
def save_to_redis(key: str, value: str):
    r.set(key, value)


# 4. 从 redis 中读取 json 字符串
def read_from_redis(key: str):
    value = r.get(key)
    return value


# 5. 把 json 字符串转换成 DataFrame 对象
def json_to_df(value):
    return pd.DataFrame.from_records(json.loads(value))


def save_stock_all_spot():
    try:
        df = stock_all_spot()
        df_dict = df.to_dict(orient="records")
        update_time = datetime.now().strftime(TIME_FMT)
        save_to_redis("stock_all_spot_updatetime", update_time)
        save_to_redis("stock_all_spot", json.dumps(df_dict))
        save_to_redis("stock_all_spot_total", str(df.shape[0]))
        data = {
            "update_time": update_time,
            "spot_data": df_dict,
            "total": df.shape[0],
        }
    except Exception as e:
        data = {
            "update_time": None,
            "spot_data": None,
            "error": str(e),
        }
    return data


def read_stock_all_spot():
    value = read_from_redis("stock_all_spot")
    if not value:
        return None

    df = json_to_df(value)
    return df


def read_stock_all_spot_updatetime():
    value = read_from_redis("stock_all_spot_updatetime")
    if not value:
        return None

    return datetime.strptime(value.decode("utf-8"), TIME_FMT)


def read_stock_all_spot_total():
    value = read_from_redis("stock_all_spot_total")
    if not value:
        return None

    return int(value.decode("utf-8"))