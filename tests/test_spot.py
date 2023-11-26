import unittest

from src.spot import stock_all_spot


class TestSpot(unittest.TestCase):
    def test_stock_all_spot(self):
        df = stock_all_spot()
        self.assertTrue(df is not None)
        self.assertTrue(len(df) > 0)
