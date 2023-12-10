from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel


class CreatreCombinationStockItem(BaseModel):
    stock_name: str
    stock_code: str
    price: Decimal = Decimal('-1')
    market_value: Decimal = Decimal('-1')
    eval_3y: Decimal = Decimal('-1')
    change_percent_1y: Decimal = Decimal('9999')
    holding_ratio: Decimal = Decimal('-1')
    holding_count: int = -1
    # combination_id: int


class CreateCombination(BaseModel):
    name: str
    note: str = ""
    is_active: int = 1
    items: List[CreatreCombinationStockItem]


class ReadCombinationStockItem(BaseModel):
    id: int
    stock_name: str
    stock_code: str
    price: Decimal
    market_value: Decimal
    eval_3y: Decimal
    change_percent_1y: Decimal
    holding_ratio: Decimal
    holding_count: int
    combination_id: int

    class Config:
        orm_mode = True


class ReadCombination(BaseModel):
    id: int
    name: str
    note: str
    create_time: datetime
    update_time: datetime
    is_active: int
    items: List[ReadCombinationStockItem]

    class Config:
        orm_mode = True

class ListCombination(BaseModel):
    id: int
    name: str
    note: str
    create_time: datetime
    update_time: datetime
    is_active: int

    class Config:
        orm_mode = True


class ReadCombinationRecordItem(BaseModel):
    id: int
    stock_name: str
    stock_code: str
    price: Decimal
    market_value: Decimal
    eval_3y: Decimal
    change_percent_1y: Decimal
    holding_ratio: Decimal
    holding_count: int
    combination_id: int
    create_time: datetime
    update_time: datetime
    combination_record_id: int

    class Config:
        orm_mode = True


class CreateCombinationRecord(BaseModel):
    combination_id: int


class CreateCombinationRecordItem(BaseModel):
    stock_name: str
    stock_code: str
    price: Decimal = Decimal('-1')
    market_value: Decimal = Decimal('-1')
    eval_3y: Decimal = Decimal('-1')
    change_percent_1y: Decimal = Decimal('9999')
    holding_ratio: Decimal = Decimal('-1')
    holding_count: int = -1
    buy_point: Decimal = Decimal('-1')
    sell_point: Decimal = Decimal('-1')

    # combination_record_id: int


class ReadCombinationRecord(BaseModel):
    id: int
    create_time: datetime
    combination_id: int
    items: List[ReadCombinationRecordItem]

    class Config:
        orm_mode = True
