from . import Address, Color


def main() -> None:
    """値オブジェクトの振る舞いを確認する。"""
    address = Address("Tokyo", "Shinjuku", "1-1-1")
    print(f"address: {address.full_address()}")
    # Tokyo Shinjuku 1-1-1

    print(Color.RED)
    # Color.RED
    print(Color.RED.value)
    # 1

    color = Color.RED
    if color == Color.RED:
        print("same color")
    else:
        print("different color")
    # same color

    for color in Color:
        print(color)
    # Color.RED
    # Color.GREEN
    # Color.BLUE


if __name__ == "__main__":
    main()
