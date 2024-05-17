from dataclasses import dataclass
from enum import Enum
from typing import Any


@dataclass
class Address:
    """住所"""

    # 都道府県
    prefecture: str
    # 市区町村
    city: str
    # 市区町村以下の住所
    address: str

    def __eq__(self, other: Any) -> bool:
        """住所が等しいか確認する。

        Args:
            other (Any): 等しいか確認する住所

        Returns:
            bool: 住所が等しい場合はTrue、等しくない場合はFalse
        """
        if not isinstance(other, Address):
            return False
        return (
            self.prefecture == other.prefecture
            and self.city == other.city
            and self.address == other.address
        )

    def __ne__(self, other: Any) -> bool:
        """住所が等しくないか確認する。

        Args:
            other (Any): 等しくないか確認する住所

        Returns:
            bool: 住所が等しくない場合はTrue、等しい場合はFalse
        """
        return not self.__eq__(other)

    def full_address(self) -> str:
        """完全な住所を返す。

        Returns:
            str: 完全な住所
        """
        return f"{self.prefecture} {self.city} {self.address}"


class Color(Enum):
    """色"""

    # 赤色
    RED = 1
    # 緑色
    GREEN = 2
    # 青色
    BLUE = 3
