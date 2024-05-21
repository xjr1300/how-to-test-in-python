from dataclasses import dataclass


@dataclass
class Company:
    """会社"""

    # ドメイン名
    domain_name: str
    # 従業員数
    number_of_employees: int
