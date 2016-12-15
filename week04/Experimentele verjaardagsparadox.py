"""
Opdracht 18 - Experimentele verjaardagsparadox
https://dodona.ugent.be/nl/exercises/1257408557/
"""

import random

def happen_together(m: int, n: int):
    duplicates = []

    for i in range(0, n):
        duplicates.append(random.randint(1, m))


def estimate_chance(m: int, n: int, tests: int):
    print("estimate")

def main():
    happen_together(6, 3)

if __name__ == '__main__':
    main()