from src.spot import stock_all_spot


def test_stock_all_spot():
    df = stock_all_spot()
    assert df is not None
    assert len(df) > 0
    df.to_excel("test.xlsx", index=False)
