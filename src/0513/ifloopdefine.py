def a(x: int) -> int:
    return x % 2


def b(x: int) -> str:
    if x == 0:
        return "偶数"
    return "奇数"


for i in range(5):
    print(b(a(i)))
        
