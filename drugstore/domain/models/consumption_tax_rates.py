from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class ConsumptionTaxRate:
    """消費税率"""

    # 消費税率を適用する起点日時 (左閉区間)
    begin: datetime
    # 消費税率を適用する終点日時 (右開区間)
    end: datetime
    # 消費税率
    rate: Decimal
