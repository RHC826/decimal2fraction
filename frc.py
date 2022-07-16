"""
    0.001-0.999 の区間で小数を分数に変換するプログラム
"""
from functools import reduce
from typing import List, Tuple


def fracize(x: float) -> Tuple[int, int]:
    """
    小数を分数にする。
    返り値は(分母、分子)の形のタプルで返す
    """
    assert x < 1, "1.0 より小さい数を投げてください"
    digit = lambda x: len(str(x).split(".")[1])
    return (10 ** digit(x), int(x * (10 ** digit(x))))


def factorize(x: int) -> list:
    """
    素因数分解をする。
    返り値は約数のリストを返す。
    """
    if x == 1:
        return [x]

    divisors = []
    # while 文を内包表記に置き換えると読みづらくなるので for文で書く
    while x % 2 == 0:
        divisors.append(2)
        x = x // 2
    for i in range(3, x + 1, 2):
        while x % i == 0:
            divisors.append(i)
            x = x // i
    return divisors


def reduction(mom: int, chil: int) -> Tuple[int, int]:
    """
    分数を約分する。
    分母と分子を共通する約数がなくなるまで共通する約数で割る。
    引数・返り値ともに(分母、分子)の形のタプル
    """
    common_divisors: List[int] = list(set(factorize(mom)) & set(factorize(chil)))
    if len(common_divisors) == 0:
        return (mom, chil)

    division = lambda x, y: x // y
    lower: int = reduce(division, [mom] + common_divisors)
    upper: int = reduce(division, [chil] + common_divisors)

    return reduction(lower, upper)


def test():
    """
    テストモジュール
    """
    assert reduction(100, 380) == (5, 19), "約分が失敗しています"
    print(f"{fracize(0.876)}  {reduction(fracize(0.876)[0],fracize(0.876)[1])}")
    print("(1000, 876)  (250, 219)")

def main():
    """
    小数 : (分母,分子)
    """
    for numerator in range(1, 1000):
        print(
            f"{numerator/1000}:  {reduction(fracize(numerator/1000)[0],fracize(numerator/1000)[1])}"
        )


if __name__ == "__main__":
    main()
