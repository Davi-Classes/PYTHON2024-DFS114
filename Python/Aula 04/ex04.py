# num = 5
# 1 * 5 = 5
# 5 * 4 = 20
# 20 * 3 = 60
# 60 * 2 = 120
# 120 * 1 = 120
def fatorial(num: int) -> int:
    fat = 1
    while num > 0:
        fat *= num
        num -= 1

    return fat
