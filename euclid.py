a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a, b = map(int, (a, b))


def euclid_gcd(a: int, b: int):
    if a < b:
        a, b = b, a

    remainder = a % b
    if remainder == 0:
        return b
    else:
        return euclid_gcd(b, remainder)


print("最大公約数は", euclid_gcd(a, b))
