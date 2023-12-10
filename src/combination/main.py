from fastapi import APIRouter, Depends
from fastapi import HTTPException
from src.config.db import SessionLocal
from src.combination import schemas
from src.combination import crud
from src.combination.create_db_tables import create_all_tables

create_all_tables()
combination_app = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@combination_app.get("/combination/{combination_id}", response_model=schemas.ReadCombination)
def get_combination(combination_id: int, db=Depends(get_db)):
    db_combination = crud.get_combination(db, combination_id)
    if db_combination is None:
        raise HTTPException(status_code=404, detail="Combination not found")
    return db_combination


@combination_app.get("/combination", response_model=list[schemas.ListCombination])
def list_combination(db=Depends(get_db)):
    return crud.list_combination(db)


@combination_app.post("/combination", response_model=schemas.CreateCombination)
def create_combination(combination: schemas.CreateCombination, db=Depends(get_db)):
    return crud.create_combination(db, combination)
