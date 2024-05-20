import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch
from zoneinfo import ZoneInfo

from vls2.visitor_manager import VisitorManager


class VisitorManagerTest(unittest.TestCase):
    """訪問者記録システムテストクラス"""

    @patch("vls2.file_system.FileSystem")
    def test_a_new_file_is_created_when_current_file_overflows(
        self, mocked_fs: MagicMock
    ) -> None:
        """現在のファイルの上限を超えているとき、新しいファイルが作成されることを確認

        単体テストでモックしたい外部依存をインターフェイス化して、プロダクションコードでは実際の外部依存を、
        単体テストではモックを使用できるようにリファクタリングした例です。
        本テストで検証していることは、プロダクションコードの品質にまったく役に立ちません。
        """
        # 準備
        visitors_per_file = 5
        mocked_fs.retrieve_files.side_effect = [
            ["visitor_0001.txt", "visitor_0002.txt"],
            ["visitor_0001.txt", "visitor_0002.txt", "visitor_0003.txt"],
        ]
        mocked_file = MagicMock()
        mocked_fs.open_visitor_file.return_value = mocked_file
        mocked_fs.recorded_visitors.return_value = visitors_per_file
        sut = VisitorManager(visitors_per_file, mocked_fs)
        time_of_visit = datetime.now(tz=ZoneInfo("Asia/Tokyo"))

        # 実行
        sut.add_record("家重", time_of_visit)

        # 検証
        visitor_files = mocked_fs.retrieve_files()
        self.assertEqual(3, len(visitor_files))
