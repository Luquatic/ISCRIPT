"""
Opdracht 18 - Experimentele verjaardagsparadox
https://dodona.ugent.be/nl/exercises/1257408557/
"""

import random

def checkDuplicates(duplicates):
    return len(duplicates) != len(set(duplicates))


def happenTogether(m: int, n: int):
    duplicates = []

    for i in range(0, n):
        duplicates.append(random.randint(1, m))

    return checkDuplicates(duplicates)


def estimateChance(m: int, n: int, tests: int):
    teller = 0

    for i in range(0, tests):
        if happenTogether(m, n) == True:
            teller = teller + 1

    return (teller / tests)


def main():
    print(happenTogether(6, 3))
    print(happenTogether(6, 3))

    print(estimateChance(6, 2, 10000))
    print(estimateChance(365, 23, 10000))

if __name__ == '__main__':
    main()