from dataclasses import dataclass
from enum import Enum
from typing import Optional


class UserType(Enum):
    """ユーザーの種類"""

    # 顧客
    Customer = 1
    # 従業員
    Employee = 1


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

    def change_email(self, id: int, new_email: str) -> None:
        """ユーザーのEメールアドレスを変更する。

        Args:
            id (int): Eメールアドレスを変更するユーザーのユーザーID
            new_email (str): 新しいEメールアドレス
        """
        # データベースからユーザーを取得
        user = Repository.retrieve_user_by_id(id)
        if user is None:
            # データベースからユーザーを取得できない場合、処理を終了
            return
        if user.email == new_email:
            # 現在のEメールアドレスと新しいEメールアドレスが等しい場合、処理を終了
            return

        # データベースから会社を取得
        company = Repository.retrieve_company()
        # Eメールアドレスからドメイン名を切り出し
        _, email_domain_name = new_email.split("@")
        # ユーザーが従業員か確認
        is_employee = True if company.domain_name == email_domain_name else False
        # ユーザーの種類を取得
        new_user_type = UserType.Employee if is_employee else UserType.Customer

        if user.type != new_user_type:
            # 従業員数を増減
            delta = 1 if new_user_type == UserType.Employee else -1
            company.number_of_employees += delta
            # 会社をデータベースに保存
            Repository.save_company(company)

        # データベースにユーザーを保存
        user.email = new_email
        user.type = new_user_type
        Repository.save_user(user)

        # メッセージバスで外部システムにユーザーのEメールアドレスが変更されたことを通知
        MessageBus.send_email_changed_message(user.id, new_email)


@dataclass
class Company:
    """会社"""

    # ドメイン名
    domain_name: str
    # 従業員数
    number_of_employees: int


class Repository:
    """データベース"""

    @classmethod
    def retrieve_user_by_id(cls, id: int) -> Optional[User]:
        """ユーザーIDをキーに、データベースからユーザーを取得する。

        Args:
            id (int): ユーザーID

        Returns:
            Optional[User]: ユーザー、見つからなかった場合はNone
        """
        pass

    @classmethod
    def save_user(cls, user: User) -> None:
        """データベースにユーザーを保存する。

        Args:
            user (User): ユーザー
        """
        pass

    @classmethod
    def retrieve_company(cls) -> Company:  # type: ignore
        """データベースから会社を取得する。

        Returns:
            Company: 会社
        """
        pass

    @classmethod
    def save_company(cls, company: Company) -> None:
        """データベースに会社を保存する。

        Args:
            company (Company): 会社
        """
        pass


class MessageBus:
    """メッセージバス"""

    @classmethod
    def send_email_changed_message(cls, id: int, new_email: str) -> bool:  # type: ignore
        """ユーザーのEメールアドレスが変更されたことを通知するメッセージをメッセージバスから送信する。

        Args:
            id (int): Eメールアドレスが変更されたユーザーのユーザーID
            new_email (str): 新しいEメールアドレス

        Returns:
            bool: メッセージの送信に成功した場合はTrue、失敗した場合はFalse
        """
        pass
