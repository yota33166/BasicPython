from math import sin, pi

# --example--
# print(sin(0))
# >>> 0
# -----------

a, b = 0, pi / 2
sum = 0
N = 100
h = (b - a) / N

for k in range(1, N + 1):
    sum += sin(a + (k - 1) * h) + sin(a + k * h)

print(f"S = {sum * h / 2}")
