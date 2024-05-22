# ruff: noqa
import os
import unittest
from unittest.mock import patch, MagicMock


class OsPathJoinTest1(unittest.TestCase):
    def test_patch_context_manager(self) -> None:
        """patchコンテキストマネージャーを使用する例"""
        with patch("os.path.join") as mock:
            # モックが返す値を設定
            mock.return_value = "foo/bar/spam.txt"
            # モックされたos.path.join関数の実行
            path1 = os.path.join("1", "2", "grok.txt")
            # モックが返した値を県s表
            self.assertEqual("foo/bar/spam.txt", path1)
        # モックが解除されている
        path2 = os.path.join("1", "2", "grok.txt")
        self.assertEqual("1/2/grok.txt", path2)

    @patch("os.path.join")
    def test_patch_decorator1(self, mock: MagicMock) -> None:
        # モックが返す値を設定
        mock.return_value = "foo/bar/spam.txt"
        # モックされたos.path.join関数の実行
        path1 = os.path.join("1", "2", "grok.txt")
        # モックが返した値を県s表
        self.assertEqual("foo/bar/spam.txt", path1)

    @patch("os.path.join", return_value="a", custom_attribute="hello")
    def test_patch_decorator2(self, mock: MagicMock) -> None:
        """patchデコレーターの引数にモックが受け取るキーワード引数とモックの属性を指定"""
        self.assertEqual("a", os.path.join(""))
        self.assertEqual("hello", mock.custom_attribute)

    @patch("os.path.join", side_effect=["a", "b"])
    def test_patch_decorator3(self, _: MagicMock) -> None:
        """モックを呼び出すたびに異なる値を返すようにpatchデコレーターの引数を設定"""
        self.assertEqual("a", os.path.join(""))
        self.assertEqual("b", os.path.join(""))


if __name__ == "__main__":
    unittest.main()
