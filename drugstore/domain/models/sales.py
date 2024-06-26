import uuid
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from drugstore.domain.models.customers import Customer
from drugstore.domain.models.items import Item


@dataclass
class SaleDetail:
    """売上明細"""

    # 売上ID
    id: uuid.UUID
    # 商品
    item: Item
    # 数量
    quantities: int
    # 小計
    amount: Decimal


@dataclass
class Sale:
    """売上"""

    # 売上ID
    id: uuid.UUID
    # 顧客
    customer: Optional[Customer]
    # 売上日時
    sold_at: datetime
    # 販売明細
    sale_details: List[SaleDetail]
    # 小計
    subtotal: Decimal
    # 割引率
    discount_rate: Decimal
    # 割引額
    discount_amount: Decimal
    # 課税対象額
    taxable_amount: Decimal
    # 消費税率
    consumption_tax_rate: Decimal
    # 消費税額
    consumption_tax_amount: Decimal
    # 合計額
    total: Decimal
