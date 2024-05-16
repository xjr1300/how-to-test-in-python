import os
from typing import List


def list_entries(dir: str) -> List[str]:
    """ディレクトリ内のエントリをリストする。

    Args:
        dir (str): ディレクトリのパス

    Returns:
        List[str]: ディレクトリ内のエントリの名前を格納したリスト
    """
    return os.listdir(dir)
