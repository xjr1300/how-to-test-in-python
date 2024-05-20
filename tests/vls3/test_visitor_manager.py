import unittest
from typing import List

from vls3.visitor_manager import VisitorFile, VisitorManager, visitor_file_name


class VisitorFileName(unittest.TestCase):
    """訪問者記録ファイル名テスト

    この単体テストは、ほとんどビジネス上の価値を持たないため、テスト対象オブジェクトは取るに足らないコードに該当します。
    取るに足らないコードは、テストを避けることを推奨します。
    """

    def test_ok(self):
        """訪問者記録ファイルのファイル名を正しく生成できるか確認"""
        pairs = [
            (1, "visitor_0001.txt"),
            (2, "visitor_0002.txt"),
            (9999, "visitor_9999.txt"),
        ]
        for input, expected in pairs:
            actual = visitor_file_name(input)
            self.assertEqual(expected, actual, f"({input}, {expected})")


class VisitorManagerTest(unittest.TestCase):
    """訪問管理者テスト"""

    def test_new_file_was_selected_when_visitor_file_does_not_exist(self):
        """訪問者ファイルが存在しないときときに、新しいファイルが閃tなくされるか確認"""
        # 準備
        manager = VisitorManager(5)
        visitor_files: List[VisitorFile] = []
        expected = "visitor_0001.txt"

        # 実行
        actual = manager.file_visitor_should_be_recorded(visitor_files)

        # 検証
        self.assertEqual(expected, actual)

    def test_latest_file_was_selected_when_visitors_did_not_record_to_the_limit(self):
        """最新の訪問者記録ファイルに訪問者数の上限まで記録されていないときに、最新のファイルが選択されることを確認"""
        # 準備
        manager = VisitorManager(5)
        visitor_files: List[VisitorFile] = [
            VisitorFile("visitor_0001.txt", 5),
            VisitorFile("visitor_0002.txt", 5),
            VisitorFile("visitor_0003.txt", 4),
        ]
        expected = "visitor_0003.txt"

        # 実行
        actual = manager.file_visitor_should_be_recorded(visitor_files)

        # 検証
        self.assertEqual(expected, actual)

    def test_new_file_was_selected_when_visitors_recorded_to_the_limit(self):
        """最新の訪問者記録ファイルに訪問者数の上限まで記録されていたときに、新しいファイルが選択されるか確認"""
        # 準備
        manager = VisitorManager(5)
        visitor_files: List[VisitorFile] = [
            VisitorFile("visitor_0001.txt", 5),
            VisitorFile("visitor_0002.txt", 5),
            VisitorFile("visitor_0003.txt", 5),
        ]
        expected = "visitor_0004.txt"

        # 実行
        actual = manager.file_visitor_should_be_recorded(visitor_files)

        # 検証
        self.assertEqual(expected, actual)
