from . import retrieve_number_of_users


class UserQuery:
    """ユーザークエリ"""

    def number_of_users(self) -> int:
        """ユーザー数を返す。

        Returns:
            int: ユーザー数
        """
        return retrieve_number_of_users()
