from dataclasses import dataclass


@dataclass
class MembershipType:
    """会員区分"""

    # 会員区分コード
    code: int
    # 会員区分名
    name: str
