import os
import re
from abc import ABC, abstractmethod
from typing import List, TextIO


class IFileSystem(ABC):
    """ファイルシステムインターフェイス"""

    # 訪問者記録ファイルのファイル名を示す正規表現
    file_expression = r"^visitor_[0-9]{3}[1-9].txt$"

    def __init__(self, dir: str) -> None:
        """イニシャライザ

        Args:
            dir (str): 訪問者記録ファイルを格納するディレクトリ
        """
        self.dir = dir

    @abstractmethod
    def retrieve_files(self) -> List[str]:
        """訪問者記録ファイルのファイル名を昇順で返す。

        Raises:
            NotImplemented:

        Returns:
            List[str]: 訪問者記録ファイルのファイル名を格納したリスト
        """
        raise NotImplementedError

    @abstractmethod
    def open_visitor_file(self, file_name: str) -> TextIO:
        """訪問者記録ファイルを開く。

        Args:
            file_name (str): 訪問者記録ファイル名

        Raises:
            NotImplementedError:

        Returns:
            TextIO: 開いた訪問者記録ファイル
        """
        raise NotImplementedError


class FileSystem(IFileSystem):
    """ファイルシステム"""

    def __init__(self, dir: str) -> None:
        """イニシャライザ

        Args:
            dir (str): 訪問者記録ファイルを格納するディレクトリ
        """
        super().__init__(dir)

    def retrieve_files(self) -> List[str]:
        """訪問者記録ファイルのファイル名を昇順で返す。

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
