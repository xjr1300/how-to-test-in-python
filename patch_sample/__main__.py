# ruff: noqa
import os
import unittest
from unittest.mock import patch, MagicMock


class PatchTest(unittest.TestCase):
    def test_patch_context_manager(self) -> None:
        """patchコンテキストマネージャーを使用する例"""
        with patch("os.path.join") as mock:
            # モックが返す値を設定
            mock.return_value = "foo/bar/spam.txt"
            # モックされたos.path.join関数の実行
            path1 = os.path.join("1", "2", "grok.txt")
            # モックが返した値を検証
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
        # モックが返した値を検証
        self.assertEqual("foo/bar/spam.txt", path1)
        # 関数終了後、モックが解除

    @patch("os.path.join", return_value="a", custom_attribute="hello")
    def test_patch_decorator2(self, mock: MagicMock) -> None:
        """patchデコレーターの引数にモックが受け取るキーワード引数とモックの属性を指定"""
        self.assertEqual("a", os.path.join(""))
        self.assertEqual("hello", mock.custom_attribute)
        # 関数終了後、モックが解除

    @patch("os.path.join", side_effect=["a", "b"])
    def test_patch_decorator3(self, _: MagicMock) -> None:
        """モックを呼び出すたびに異なる値を返すようにpatchデコレーターの引数を設定"""
        self.assertEqual("a", os.path.join(""))
        self.assertEqual("b", os.path.join(""))
        # 関数終了後、モックが解除


class Foo:
    def __init__(self) -> None:
        self.x = "Hello, world!"
        self.y = 65

    def get_y(self) -> int:
        return self.y


class PatchObjectTest(unittest.TestCase):
    def test_patch_object1(self) -> None:
        foo = Foo()
        # fooのxの属性をモック
        with patch.object(foo, "x", "Hello, python!"):
            self.assertEqual("Hello, python!", foo.x)

    # Fooのget_yメソッドをモック
    @patch.object(Foo, "get_y", return_value=32)
    def test_patch_object2(self, mock: MagicMock) -> None:
        foo = Foo()
        self.assertEqual(32, foo.get_y())


@patch.dict("os.environ", {"custom_key": "custom_value"})
class PatchDictTest(unittest.TestCase):
    def test_patch_dict1(self) -> None:
        self.assertTrue("custom_key" in os.environ)
        self.assertEqual("custom_value", os.environ["custom_key"])

    def test_patch_dict2(self) -> None:
        d = {}
        with patch.dict(d, {"a": 65, "b": "Hello, world!"}):
            self.assertTrue("a" in d.keys())
            self.assertEqual(65, d["a"])
            self.assertTrue("b" in d.keys())
            self.assertEqual("Hello, world!", d["b"])
        self.assertFalse("a" in d.keys())
        self.assertFalse("b" in d.keys())


if __name__ == "__main__":
    unittest.main()
