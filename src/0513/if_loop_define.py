def a(x: int) -> int:
    return x % 2


def b(x: int) -> str:
    if x == 0:
        return "偶数"
    return "奇数"


y = [55, 6, 99, 66, 68, 90, 35, 56]

for i in y:
    print(b(a(i)))
