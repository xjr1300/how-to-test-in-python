from .message_bus import MessageBus
from .repository import Repository


class UserService:
    """ユーザーサービス"""

    def change_email(self, id: int, new_email: str) -> None:
        """ユーザーのEメールアドレスを変更する。

        Args:
            id (int): Eメールアドレスを変更するユーザーのユーザーID
            new_email (str): 新しいEメールアドレス
        """
        # データベースからユーザーを取得
        user = Repository.retrieve_user_by_id(id)
        if user is None:
            # データベースにユーザーIDが一致するユーザーが存在しない場合は、処理を終了
            return
        # ユーザーの変更前のパスワードと新しいパスワードが一致している場合は、処理を終了
        if user.email == new_email:
            return

        # データベースから会社を取得
        company = Repository.retrieve_company()

        # ユーザーのEメールアドレスを変更
        user.change_email(new_email, company)

        # 従業員数が更新された可能性があるため、会社をデータベースに保存
        Repository.save_company(company)

        # ユーザーをデータベースに保存
        Repository.save_user(user)

        # メッセージバスで外部システムにユーザーのEメールアドレスが変更されたことを通知
        MessageBus.send_email_changed_message(user.id, new_email)
