from sqlalchemy.orm import Session

from src.combination.schemas import CreateCombination
from src.combination.models import Combination, CombinationStockItem


def create_combination(db: Session, combination: CreateCombination):
    db_combination = Combination(
        name=combination.name,
        note=combination.note,
        is_active=combination.is_active,
    )
    for item in combination.items:
        item_obj = CombinationStockItem(
                stock_name=item.stock_name,
                stock_code=item.stock_code,
                price=item.price,
                market_value=item.market_value,
                eval_3y=item.eval_3y,
                change_percent_1y=item.change_percent_1y,
                holding_ratio=item.holding_ratio,
                holding_count=item.holding_count,
            )
        db_combination.items.append(item_obj)
    db.add(db_combination)
    db.commit()
    db.refresh(db_combination)

    return combination


def get_combination(db: Session, combination_id: int):
    return db.query(Combination).filter(
        Combination.id == combination_id
    ).first()


def list_combination(db: Session):
    results = db.query(Combination).all()

    return results

