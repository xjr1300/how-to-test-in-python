from typing import Optional

from .company import Company
from .user import User


class Repository:
    """データベース"""

    @classmethod
    def retrieve_user_by_id(cls, id: int) -> Optional[User]:
        """ユーザーIDをキーに、データベースからユーザーを取得する。

        Args:
            id (int): ユーザーID

        Returns:
            Optional[User]: ユーザー、見つからなかった場合はNone
        """
        pass

    @classmethod
    def save_user(cls, user: User) -> None:
        """データベースにユーザーを保存する。

        Args:
            user (User): ユーザー
        """
        pass

    @classmethod
    def retrieve_company(cls) -> Company:  # type: ignore
        """データベースから会社を取得する。

        Returns:
            Company: 会社
        """
        pass

    @classmethod
    def save_company(cls, company: Company) -> None:
        """データベースに会社を保存する。

        Args:
            company (Company): 会社
        """
        pass
