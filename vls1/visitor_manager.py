import os
import re
from datetime import datetime
from typing import List, TextIO


def visitor_file_record(visitor_name: str, time_of_visit: datetime) -> str:
    """訪問者ファイルに記録するレコードを生成する。

    Args:
        visitor_name (str): 訪問者の名前
        time_of_visit (datetime): 訪問日時

    Returns:
        str: 訪問者ファイルに記録するレコード
    """
    return ",".join([visitor_name, time_of_visit.isoformat()])


def recorded_visitors(file: TextIO) -> int:
    """訪問者ファイルに記録されている訪問者の数を返す。

    Args:
        file (TextIO): 訪問者ファイル

    Returns:
        int: 訪問者ファイルに記録されている訪問者の数
    """
    file.seek(0)
    number_of_records = 0
    for _ in file:
        number_of_records += 1
    return number_of_records


def visitor_file_name(index: int) -> str:
    """訪問者記録ファイルのファイル名を返す。

    Args:
        index (int): 1から始まる訪問者記録ファイルのインデックス。

    Returns:
        str: 訪問者記録ファイルのファイル名
    """
    return f"visitor_{index:04}.txt"


class VisitorManager:
    """訪問者記録システム"""

    # 訪問者記録ファイルのファイル名を示す正規表現
    file_expression = r"^visitor_[0-9]{3}[1-9].txt$"

    def __init__(self, max_entries_per_file: int, dir: str) -> None:
        """イニシャライザ

        Args:
            max_entries_per_file (int): 訪問者記録ファイルに記録する訪問者の上限
            dir (str): 訪問者記録ファイルを格納するディレクトリのパス
        """
        self.max_entries_per_file = max_entries_per_file
        self.dir = dir

    def retrieve_files(self) -> List[str]:
        """訪問者記録ファイルをファイル名の昇順で取得して返す。

        Returns:
            List[str]: 訪問者記録ファイルのファイル名を格納したリスト
        """

        def is_match(entry: str) -> bool:
            """ファイルシステムのエントリが訪問者記録ファイルのファイル名に従っているか確認する。

            Args:
                entry (str): _description_

            Returns:
                bool: _description_
            """
            return re.fullmatch(self.file_expression, entry) is not None

        entries = os.listdir(self.dir)
        files = list(filter(is_match, entries))
        files.sort()
        return files

    def open_visitor_file(self, file_name: str) -> TextIO:
        """読み書き用で訪問者記録ファイルを開く。

        Args:
            file_name (str): 訪問者記録ファイル

        Returns:
            TextIO: 開いた訪問者記録ファイル
        """
        path = os.path.join(self.dir, file_name)
        return open(path, "a+")

    def add_record(self, visitor_name: str, time_of_visit: datetime) -> None:
        """訪問者とその訪問日時を訪問者記録ファイルに記録する。

        Args:
            visitor_name (str): 訪問者の名前
            time_of_visit (datetime): 訪問日時
        """
        # 訪問者記録ファイルを取得
        files = self.retrieve_files()
        number_of_files = len(files)
        if number_of_files == 0:
            # 訪問者記録ファイルが存在しない場合は、訪問者記録ファイルを開く
            file = self.open_visitor_file(visitor_file_name(1))
        else:
            # 最新の訪問者記録ファイルに記録されている訪問者数を取得
            file_name = files[number_of_files - 1]
            file = self.open_visitor_file(file_name)
            number_of_visitors = recorded_visitors(file)
            if self.max_entries_per_file <= number_of_visitors:
                # 最新の訪問者記録ファイルに記録されている訪問者が上限に達している場合、
                # 開いている訪問者記録ファイルを閉じて、新しい訪問者記録ファイルを作成し
                # て開く
                file.close()
                file = self.open_visitor_file(visitor_file_name(number_of_files + 1))
        # ファイルの末尾に訪問者を記録
        file.write(visitor_file_record(visitor_name, time_of_visit) + "\n")
