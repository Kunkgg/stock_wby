from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    Integer,
    SmallInteger,
    DECIMAL
)
from sqlalchemy import func
from sqlalchemy.orm import relationship

from src.config.db import Base


class Combination(Base):
    __tablename__ = "combination"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    note = Column(Text, nullable=True)
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now())
    is_active = Column(SmallInteger, nullable=False, default=1)


class CombinationStockItem(Base):
    __tablename__ = "combination_stock_item"

    id = Column(Integer, primary_key=True, index=True)
    stock_name = Column(String(255), nullable=False)
    stock_code = Column(String(255), nullable=False)
    price = Column(DECIMAL(20, 2), nullable=False)
    market_value = Column(DECIMAL(20, 2), nullable=False)
    eval_3y = Column(DECIMAL(20, 2), nullable=False)
    change_percent_1y = Column(DECIMAL(10, 2), nullable=False)
    holding_ratio = Column(DECIMAL(10, 2), nullable=False)
    holding_count = Column(Integer, nullable=False)

    combination_id = Column(Integer, nullable=False)
    Combination = relationship("Combination",
                               primaryjoin="Combination.id==foreign(CombinationStockItem.combination_id)",
                               backref="items")

class CombinationRecord(Base):
    __tablename__ = "combination_record"

    id = Column(Integer, primary_key=True, index=True)
    create_time = Column(DateTime, server_default=func.now())
    combination_id = Column(Integer, nullable=False)

    Combination = relationship("Combination",
                               primaryjoin="Combination.id==foreign(CombinationRecord.combination_id)",
                               backref="records")


class CombinationRecordItem(Base):
    __tablename__ = "combination_record_item"

    id = Column(Integer, primary_key=True, index=True)
    stock_name = Column(String(255), nullable=False)
    stock_code = Column(String(255), nullable=False)
    price = Column(DECIMAL(20, 2), nullable=False)
    market_value = Column(DECIMAL(20, 2), nullable=False)
    eval_3y = Column(DECIMAL(20, 2), nullable=False)
    change_percent_1y = Column(DECIMAL(10, 2), nullable=False)
    holding_ratio = Column(DECIMAL(10, 2), nullable=False)
    holding_count = Column(Integer, nullable=False)
    buy_point = Column(DECIMAL(10, 2), nullable=False)
    sell_point = Column(DECIMAL(10, 2), nullable=False)
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now())

    combination_record_id = Column(Integer, nullable=False)
    CombinationRecord = relationship("CombinationRecord",
                                     primaryjoin="CombinationRecord.id==foreign(CombinationRecordItem.combination_record_id)",
                                     backref="items")
