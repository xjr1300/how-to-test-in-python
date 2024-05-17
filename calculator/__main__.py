import unittest


# プロダクションコード
class Calculator:
    """計算機クラス"""

    def add(self, a: int, b: int) -> int:
        """2つの整数を足し算した結果を返す。

        Args:
            a (int): 演算子の左辺の値
            b (int): 演算子の右辺の値

        Returns:
            int: 2つの整数を足し算した結果
        """
        return a + b


# テストコード
class CalculatorTest(unittest.TestCase):
    """計算機テストクラス"""

    def test_add_two_numbers(self) -> None:
        """2つの整数を足した結果が正しいことを確認するテスト"""
        # 準備 (Arrange)
        calculator = Calculator()
        a = 1
        b = 2

        # 実行 (Act)
        result = calculator.add(a, b)

        # 検証 (Assert)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
