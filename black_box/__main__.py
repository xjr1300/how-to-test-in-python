import unittest


def is_adult(year: int) -> bool:
    """年齢から大人か子供かを判定する。

    18才以上を大人と判定する。

    Args:
        year (int): 年齢

    Returns:
        bool: 大人の場合はTrue、子供の場合はFalse

    Raises:
        ValueError: 年齢は0以上を指定してください。
    """
    if year < 0:
        raise ValueError("年齢は0才以上を指定してください。")
    return True if 18 <= year else False


class EquivalencePartitioningTest(unittest.TestCase):
    """同値分割法でis_adult関数をテストするクラス"""

    def test_is_adult(self) -> None:
        """大人と判定されることを確認するテスト"""
        self.assertTrue(is_adult(18))
        self.assertTrue(is_adult(20))
        self.assertTrue(is_adult(100))

    def test_is_child(self) -> None:
        """子供と判定されることを確認するテスト"""
        self.assertFalse(is_adult(0))
        self.assertFalse(is_adult(10))
        self.assertFalse(is_adult(17))

    def test_raises_exception_when_negative_years_old(self) -> None:
        """0未満の年齢を判定しようとしたときに、例外が発生することを確認するテスト"""
        with self.assertRaises(ValueError):
            is_adult(-1)
            is_adult(-10)
            is_adult(-100)


class BoundaryValueAnalysisTest(unittest.TestCase):
    """境界値分析でis_adult関数をテストするクラス"""

    def test_is_adult(self) -> None:
        """大人と判定されることを確認するテスト"""
        self.assertTrue(is_adult(18))
        self.assertTrue(is_adult(19))

    def test_is_child(self) -> None:
        """子供と判定されることを確認するテスト"""
        self.assertFalse(is_adult(17))
        self.assertFalse(is_adult(16))

    def test_raises_exception_when_negative_years_old(self) -> None:
        """0未満の年齢を判定しようとしたときに、例外が発生することを確認するテスト"""
        with self.assertRaises(ValueError):
            is_adult(-1)
            is_adult(-2)


if __name__ == "__main__":
    unittest.main()
