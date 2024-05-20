import time
from datetime import datetime
from zoneinfo import ZoneInfo

from .file_system import FileSystem
from .visitor_manager import VisitorManager

# 訪問者記録ファイルディレクトリ
VLS_DIR = "resources/vls2"
# 訪問者記録ファイルに記録可能な訪問者数
VISITORS_PER_FILE = 5


def main():
    """エントリポイント"""
    # ファイルシステムを構築
    file_system = FileSystem(VLS_DIR)

    # 訪問者管理
    manager = VisitorManager(VISITORS_PER_FILE, file_system)
    # 訪問者
    visitors = [
        "家康",
        "秀忠",
        "家光",
        "家綱",
        "綱吉",
        "家宣",
        "家継",
        "吉宗",
        # "家重",
        # "家治",
        # "家斉",
        # "家慶",
        # "家定",
        # "家茂",
        # "慶喜"
    ]

    for visitor in visitors:
        manager.add_record(visitor, datetime.now(tz=ZoneInfo("Asia/Tokyo")))
        time.sleep(1)


if __name__ == "__main__":
    main()
