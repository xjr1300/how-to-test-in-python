import os
from dataclasses import dataclass
from typing import List, Self


@dataclass
class VisitorFile:
    """訪問者ファイル"""

    # 訪問者ファイルのファイル名
    file_name: str
    # ファイルに記録されている訪問者数
    number_of_records: int

    @classmethod
    def create(cls, dir: str, file_name: str) -> Self:
        """イニシャライザ

        訪問者記録ファイルに記録されている訪問者数をメンバ変数に記録する。

        Args:
            dir (str): 訪問者記録ファイルを格納するディレクトリのパス
            file_name (str): 訪問者記録ファイルのファイル名
        """
        number_of_records = 0
        with open(os.path.join(dir, file_name), "rt") as file:
            for _ in file:
                number_of_records += 1
        return cls(file_name, number_of_records)


def visitor_file_name(index: int) -> str:
    """訪問者記録ファイルのファイル名を返す。

    Args:
        index (int): 1から始まる訪問者記録ファイルのインデックス。

    Returns:
        str: 訪問者記録ファイルのファイル名
    """
    return f"visitor_{index:04}.txt"


class VisitorManager:
    """訪問管理者"""

    def __init__(self, max_entries_per_file: int) -> None:
        """イニシャライザ

        Args:
            max_entries_per_file (int): 訪問者記録ファイルに記録できる訪問者数の上限
        """
        self.max_entries_per_file = max_entries_per_file

    def file_visitor_should_be_recorded(self, visitor_files: List[VisitorFile]) -> str:
        """訪問者を記録するファイルのファイル名を返す。

        Args:
            visitor_files (List[VisitorFile]): 訪問者記録ファイルをファイル名の昇順で
                格納したリスト

        Returns:
            str: 訪問者を記録するファイルのファイル名
        """
        number_of_files = len(visitor_files)
        # 訪問者記録ファイルが存在しない場合は、インデックス1の
        if number_of_files == 0:
            return visitor_file_name(1)
        # 最新の訪問者記録ファイルに訪問者が上限まで記録されているか確認
        latest_file = visitor_files[number_of_files - 1]
        if latest_file.number_of_records < self.max_entries_per_file:
            # 最新の訪問者記録ファイルに訪問者が上限まで記録されていない場合、
            # 最新の訪問者記録ファイルに記録
            return latest_file.file_name
        else:
            # 最新の訪問者記録ファイルに訪問者が上限まで記録されている場合、
            # 新しい訪問者記録ファイルに記録
            return visitor_file_name(number_of_files + 1)
