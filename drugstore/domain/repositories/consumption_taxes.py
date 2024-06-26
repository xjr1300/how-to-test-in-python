import abc
from typing import List

from drugstore.domain.models.consumption_taxes import ConsumptionTax


class ConsumptionTaxRepository(abc.ABC):
    """消費税リポジトリ"""

    @abc.abstractmethod
    def list(self) -> List[ConsumptionTax]:
        """起点日時の昇順で格納された消費税リストを返す。

        Returns:
            List[ConsumptionTax]: 起点日時の昇順で格納された消費税リスト
        """
        pass

    @abc.abstractmethod
    def replace_list(self, consumption_taxes: List[ConsumptionTax]) -> None:
        """消費税リストを入れ替える。

        Args:
            consumption_taxes (List[ConsumptionTax]): 消費税リスト
        """
        pass
