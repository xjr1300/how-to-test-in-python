import random


def retrieve_number_of_users() -> int:
    """ユーザー数を返す。

    データベースにアクセスして、ユーザー数を返す実装を想像してください。
    0から99をランダムに返すため、単体テストで振る舞いを検証することが難しくなります。

    Returns:
        int: ユーザー数
    """
    return random.randint(0, 99)
