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
