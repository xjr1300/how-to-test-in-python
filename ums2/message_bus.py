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
