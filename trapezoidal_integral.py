from math import pi, sin, sqrt, exp

# --example--
# print(sin(0))
# >>> 0
# -----------


def trapezoidal_integral(f, a: int | float, b: int | float, n: int) -> float:
    sum = 0
    h = (b - a) / n
    for k in range(1, n + 1):
        sum += f(a + (k - 1) * h) + f(a + k * h)

    return sum * h / 2


def func2(x: int | float):
    return 4 / (1 + x**2)


def func3(x: int | float):
    return sqrt(pi) * exp(-(x**2))


print(f"S = {trapezoidal_integral(sin, 0, pi/2, 50)}")
print(f"S = {trapezoidal_integral(func2, 0, 1, 100)}")
print(f"S = {trapezoidal_integral(func3, -100, 100, 1000)}")
