a = input("aの値を入力: ")
b = input("bの値を入力: ")


# TODO
def is_prime(n: int):
    if not isinstance(n, int):
        raise TypeError("引数は整数である必要があります")
    elif n <= 0:
        raise ValueError("引数は正の整数である必要があります")

    if n <= 1:
        return False
    if n == 2:
        return True

    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False

    return True


for num in map(int, (a, b)):
    if is_prime(num):
        print(num, "は素数です")
    else:
        print(num, "は素数ではありません")
