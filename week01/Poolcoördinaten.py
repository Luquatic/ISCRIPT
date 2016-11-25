"""
Opdracht 3 - Poolcoördinaten
https://dodona.ugent.be/nl/exercises/333498206/
"""

import math

x = input("X cordinaat: ")
y = input("Y cordinaat: ")

def main(x, y):
    rho = math.sqrt(x**2 + y**2)
    phi = math.atan2(y, x)
    print(rho)
    print(phi)

if __name__ == "__main__":
    main(x, y)