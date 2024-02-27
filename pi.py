text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

pi = list(map(len, text.replace(",", "").replace(".", "").split()))
print("".join(map(str, pi)))
