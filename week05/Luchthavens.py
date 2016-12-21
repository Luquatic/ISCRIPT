"""
Opdracht 25
https://dodona.ugent.be/nl/exercises/1748605282/
"""

import math

def leesLuchthavens(file: str):
    # Maak dictionary aan
    dictionary = {}
    # Lees de file
    file = open(file, "r", encoding='utf8')
    # Verwijderd elke witte lijn
    read = file.read().split("\n")
    file.close()

    for row in read:
        if row[0] is "[":
            row = row.split("\t")
            dictionary[row[0].replace("[", "").replace("]", "")] = row[1::]
    return dictionary

def afstand(code1, code2, luchthavens):
    R = 6372.795

    return R * math.atan(math.sqrt())

def tussenlanding(code1, code2, luchthavens, [reikwijdte=4000]):
    print("tussenlanding")

def main():
    luchthavens = leesLuchthavens('luchthavens.txt')
    print(luchthavens)
    print()

    print(luchthavens['ADK'])
    print(luchthavens['DCA'])
    print(luchthavens['4OM'])
    print()

    print(afstand('P60', 'MSN', luchthavens))
    print(afstand('ADK', 'DCA', luchthavens))


if __name__ == '__main__':
    main()