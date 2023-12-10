import sys

sys.path.append(".")

from sqlalchemy import MetaData

from src.config.db import engine
from src.combination.models import (
    Combination,
    CombinationStockItem,
    CombinationRecord,
    CombinationRecordItem,
)

tables = [
    Combination.__table__,
    CombinationStockItem.__table__,
    CombinationRecord.__table__,
    CombinationRecordItem.__table__,
]
meta = MetaData()


def create_all_tables():
    meta.create_all(engine, tables=tables)
    # meta.drop_all(engine, tables=tables)
