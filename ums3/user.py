import json
import uuid
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, StrEnum, auto
from typing import Any, Dict, List
from zoneinfo import ZoneInfo

from .company import Company


class UserType(Enum):
    """ユーザーの種類"""

    # 顧客
    Customer = 1
    # 従業員
    Employee = 1


class UserEventType(StrEnum):
    """ユーザーに発生したイベントの種類"""

    # ユーザーが登録された
    Registered = auto()
    # ユーザーのEメールアドレスが変更された
    EmailChanged = auto()
    # ユーザーの種類が変更された
    TypeChanged = auto()
    # ユーザーが削除された
    Deleted = auto()


@dataclass
class UserEvent:
    """ユーザーに発生したイベント"""

    # イベントID
    event_id: uuid.UUID

    # 発生日時
    dt: datetime

    # ユーザーに発生したイベントの種類
    event_type: UserEventType

    # ユーザに発生したイベントのデータ
    event_data: Dict[str, Any]

    def __init__(
        self, event_id: uuid.UUID, event_type: UserEventType, event_data: Dict[str, Any]
    ) -> None:
        """イニシャライザ

        Args:
            event_id (uuid.UUID): イベントID
            event_type (UserEventType): ユーザーイベントの種裏
            event_data (Dict[str, Any]): イベントデータ
        """
        self.event_id = event_id
        self.dt = datetime.now(tz=ZoneInfo("Asia/Tokyo"))
        self.event_type = event_type
        self.event_data = event_data

    def to_json(self) -> str:
        """ユーザーイベントを表現するJSON形式の文字列を返す。

        Returns:
            str: ユーザーイベントを表現するJSON形式の文字列
        """
        data = {
            "event_id": self.event_id,
            "dt": self.dt.isoformat(),
            "domain": "user",
            "event_type": self.event_type,
        }
        data.update(self.event_data)
        return json.dumps(data, ensure_ascii=False)


class User:
    """ユーザー"""

    def __init__(self, id: int, email: str, type: UserType) -> None:
        """イニシャライザ

        Args:
            id (int): ユーザーID
            email (str): Eメールアドレス
            type (UserType): ユーザーの種類
        """
        self.id = id
        self.email = email
        self.type = type
        self.events: List[UserEvent] = []

    def change_email(self, new_email: str, company: Company) -> None:
        """ユーザーのEメールアドレスを変更する。

        ユーザーのEメールアドレスの変更と連動して、必要に応じてユーザーの種類を更新する。
        また、ユーザーの種類が顧客から従業員になった場合、または従業員から顧客になった場合、
        会社の従業員数が更新される。

        Args:
            new_email (str): 新しいEメールアドレス
            company (Company): 会社
        """
        event_id = uuid.uuid4()
        if self.email == new_email:
            # 現在のEメールアドレスと新しいEメールアドレスが等しい場合、処理を終了
            return

        # Eメールアドレスからドメイン名を切り出し
        _, email_domain_name = new_email.split("@")
        # ユーザーが従業員か確認
        is_employee = True if company.domain_name == email_domain_name else False
        # ユーザーの種類を取得
        new_user_type = UserType.Employee if is_employee else UserType.Customer

        if self.type != new_user_type:
            # 会社の従業員数を更新
            delta = 1 if new_user_type == UserType.Employee else -1
            company.number_of_employees += delta
            # ユーザーの種類が変更されたイベントを登録
            self.events.append(
                UserEvent(
                    event_id,
                    UserEventType.TypeChanged,
                    {
                        "user_id": self.id,
                        "before": self.type.name.lower(),
                        "after": new_user_type.name.lower(),
                    },
                )
            )

        # Eメール変更イベントを登録
        self.events.append(
            UserEvent(
                event_id,
                UserEventType.EmailChanged,
                {
                    "user_id": self.id,
                    "before": self.email,
                    "after": new_email,
                },
            )
        )

        # ユーザーを更新
        self.email = new_email
        self.type = new_user_type
