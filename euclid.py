a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
import random

a, b = map(int, (a, b))

#問3
def euclid_gcd(a: int, b: int):
    if a < b:
        a, b = b, a

    remainder = a % b
    if remainder == 0:
        return b
    else:
        return euclid_gcd(b, remainder)


print("最大公約数は", euclid_gcd(a, b))


#問4
def is_coprime(a: int, b: int) -> bool:
    return euclid_gcd(a, b) == 1


pairs = [(random.randint(1, 10000), random.randint(1, 10000)) for _ in range(100000)]

n = 0
for a, b in pairs:
    if is_coprime(a, b):
        n += 1

print("各組が互いに素である確率", n/100000)