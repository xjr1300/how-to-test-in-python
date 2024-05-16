import unittest

from boring_module import Point


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
