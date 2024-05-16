def is_adult(year: int) -> bool:
    """年齢から大人か子供かを判定する。

    18才以上を大人と判定する。

    Args:
        year (int): 年齢

    Returns:
        bool: 大人の場合はTrue、子供の場合はFalse

    Raises:
        ValueError: 年齢は0以上を指定してください。
    """
    if year < 0:
        raise ValueError("年齢は0才以上を指定してください。")
    return True if 18 <= year else False
