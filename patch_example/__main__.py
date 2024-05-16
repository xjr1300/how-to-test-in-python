import unittest
from unittest.mock import patch

from . import list_entries


class TestListFiles(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def test_list_files_with_patch(self):
        """_summary_"""
        with patch("os.listdir") as mock_listdir:
            # MagicMockを設定して、特定の戻り値を返すようにする
            mock_listdir.return_value = ["file1.txt", "file2.txt", "file3.txt"]

            # テスト対象の関数を呼び出す
            result = list_entries(".")

            # os.listdirが呼び出されたことを確認
            mock_listdir.assert_called_once_with(".")

            # 関数の戻り値が期待通りであることを確認
            self.assertEqual(result, ["file1.txt", "file2.txt", "file3.txt"])

        # コンテキストを抜けると、os.listdirは元の状態に戻る
        # この時点でos.listdirは実際の関数を指している
        print(list_entries("."))


if __name__ == "__main__":
    unittest.main()
