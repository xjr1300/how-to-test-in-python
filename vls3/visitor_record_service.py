import os
import re
from datetime import datetime
from operator import attrgetter
from typing import List

from .visitor_manager import VisitorFile, VisitorManager


class VisitorRecordService:
    """訪問者記録サービス"""

    # 訪問者記録ファイルのファイル名を示す正規表現
    file_expression = r"^visitor_[0-9]{3}[1-9].txt$"

    def __init__(self, max_entries_per_file: int, dir: str) -> None:
        """イニシャライザ

        Args:
            max_entries_per_file (int): 訪問者記録ファイルに記録できる訪問者数の上限
            dir (str): 訪問者記録ファイルを格納するディレクトリのパス
        """
        self.max_entries_per_file = max_entries_per_file
        self.dir = dir

    def _retrieve_visitor_files(self) -> List[VisitorFile]:
        """訪問者記録ファイルを取得する。

        Returns:
            List[VisitorFile]: 訪問者記録ファイルをファイル名の昇順で格納したリスト
        """

        def _is_match(entry: str) -> bool:
            """ファイルシステムのエントリが訪問者記録ファイルのファイル名に従っているか確認する。

            Args:
                entry (str): _description_

            Returns:
                bool: _description_
            """
            return re.fullmatch(self.file_expression, entry) is not None

        entries = os.listdir(self.dir)
        visitor_files: List[VisitorFile] = []
        for entry in filter(_is_match, entries):
            visitor_files.append(VisitorFile.create(self.dir, entry))
        visitor_files.sort(key=attrgetter("file_name"))
        return visitor_files

    def record_visitor(self, visitor_name: str, time_of_visit: datetime) -> None:
        """訪問者を訪問者記録ファイルに記録する。

        Args:
            visitor_name (str): 訪問者の名前
            time_of_visit (datetime): 訪問者が訪問した日時
        """
        visitor_files = self._retrieve_visitor_files()
        manager = VisitorManager(self.max_entries_per_file)
        visitor_file = manager.file_visitor_should_be_recorded(visitor_files)
        visitor_record = visitor_file_record(visitor_name, time_of_visit)
        with open(os.path.join(self.dir, visitor_file), "a+") as file:
            file.write(visitor_record + "\n")


def visitor_file_record(visitor_name: str, time_of_visit: datetime) -> str:
    """訪問者ファイルに記録するレコードを生成する。

    Args:
        visitor_name (str): 訪問者の名前
        time_of_visit (datetime): 訪問日時

    Returns:
        str: 訪問者ファイルに記録するレコード
    """
    return ",".join([visitor_name, time_of_visit.isoformat()])
