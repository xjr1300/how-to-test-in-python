import unittest
from dataclasses import dataclass


@dataclass
class Point:
    """2次元ポイント"""

    _x: int
    _y: int

    @property
    def x(self) -> int:
        """X座標値を返す。

        Returns:
            int: X座標値
        """
        return self._x

    @property
    def y(self) -> int:
        """Y座標値を返す。

        Returns:
            int: Y座標値
        """
        return self._y


class PointTest(unittest.TestCase):
    """Pointをテストするクラス"""

    def test_x(self) -> None:
        """Xプロパティのテスト"""
        p = Point(3, 4)
        self.assertEqual(3, p.x)

    def test_y(self) -> None:
        """Yプロパティのテスト"""
        p = Point(3, 4)
        self.assertEqual(4, p.y)


if __name__ == "__main__":
    unittest.main()
