from src.store import (
    save_stock_all_spot,
    read_stock_all_spot,
    read_stock_all_spot_updatetime,
)


def test_save_stock_all_spot():
    save_stock_all_spot()
    assert True


def test_read_stock_all_spot():
    df = read_stock_all_spot()
    assert df is not None
    assert len(df) > 0


def test_read_stock_all_spot_updatetime():
    updatetime = read_stock_all_spot_updatetime()
    print(updatetime)
    assert updatetime is not None
