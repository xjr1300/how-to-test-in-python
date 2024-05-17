"""MagicMockの実装例

test_number_of_users_with_context_managerで、モックが解除されたことを確認する場合、
test_number_of_usersをコメントアウトして実行できないようにしてください。
"""  # noqa: E501

import unittest
from unittest.mock import MagicMock, patch

from magic_mock.user_query import UserQuery


class UserQueryTest(unittest.TestCase):
    """ユーザークエリテストクラス"""

    # def test_number_of_users(self) -> None:
    #     """ユーザー数が正しいことを確認するテスト"""
    #     # 準備
    #     # ユーザークエリを構築
    #     query = UserQuery()
    #     # retrieve_number_of_users関数をモックします。
    #     # retrieve_number_of_users関数は0から99までの整数をランダムで返しますが、
    #     # モックされていることがわかりやすいように、100を返すようにしています。
    #     magic_mock.user_query.retrieve_number_of_users = MagicMock(return_value=100)

    #     # 実行
    #     # ユーザークエリを介して、ユーザー数を取得します。
    #     result = query.number_of_users()

    #     # 検証
    #     # ユーザー数が100人であるか確認します。
    #     self.assertEqual(100, result)

    def test_number_of_users_with_context_manager(self) -> None:
        """[コンテキストマネージャバージョン]: ユーザー数が正しいことを確認するテスト

        コンテキストマネージャーを使用するとモックオブジェクトが`mock_func`変数に格納されます。
        このmock_func変数にモックの振る舞いを定義します。

        with句のスコープを外れると、モックが解除されて、実際のretrieve_number_of_users関数
        が呼ばれます。
        """
        # 準備
        query = UserQuery()
        with patch("magic_mock.user_query.retrieve_number_of_users") as mock_func:
            mock_func.return_value = 100
            # 実行
            result = query.number_of_users()
            # 検証
            self.assertEqual(100, result)

        result = query.number_of_users()
        print(f"the real number of users is {result}")

    @patch("magic_mock.user_query.retrieve_number_of_users")
    def test_number_of_users_with_decorator(self, mock_func: MagicMock) -> None:
        """[デコレーターバージョン]: ユーザー数が正しいことを確認するテスト

        mock_func引数にモックの振る舞いを定義します。

        関数のスコープを外れると、モックが解除されて、実際のretrieve_number_of_users関数
        が呼ばれます。
        """
        # 準備
        query = UserQuery()
        mock_func.return_value = 100

        # 実行
        result = query.number_of_users()

        # 検証
        self.assertEqual(100, result)


if __name__ == "__main__":
    unittest.main()
