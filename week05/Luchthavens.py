"""
Opdracht 25
https://dodona.ugent.be/nl/exercises/1748605282/
"""

from math import radians, cos, sin, sqrt, atan2

def leesLuchthavens(file: str):
    # Maak dictionary aan
    luchthavens = {}
    # Lees de file
    file = open(file, "r", encoding='utf8')
    # Verwijderd elke witte lijn
    read = file.read().split("\n")
    file.close()

    for row in read:
        if row[0] is "[":
            row = row.split("\t")
            luchthavens[row[0].replace("[", "").replace("]", "")] = row[1::]
    return luchthavens

def afstand(code1, code2, luchthavens):
    # Geef de afstand terug.
    R = 6372.795

    b1 = float(luchthavens[code1][0])
    b2 = float(luchthavens[code2][0])
    l1 = float(luchthavens[code1][1])
    l2 = float(luchthavens[code2][1])

    b1, b2, l1, l2 = map(radians, [b1, b2, l1, l2])
    dl = l1 - l2

    math_up = (((cos(b2) * sin(dl)) ** 2) + (((cos(b1) * sin(b2)) - (sin(b1) * cos(b2) * cos(dl))) ** 2))
    math_up_sqrt = sqrt(math_up)
    math_down = (sin(b1) * sin(b2) + cos(b1) * cos(b2) * cos(dl))
    total = R * atan2(math_up_sqrt, math_down)

    return total

def tussenlanding(code1, code2, luchthavens, reikwijdte):
    max_distance = 2 * reikwijdte
    if (afstand(code1, code2, luchthavens) > reikwijdte):
        code3 = ""

        for luchthaven in luchthavens:
            dist1 = afstand(code1, luchthaven, luchthavens)
            dist2 = afstand(luchthaven, code2, luchthavens)
            if dist1 < reikwijdte and reikwijdte > dist2:
                total = dist1 + dist2
                if total < max_distance:
                    max_distance = total
                    code3 = luchthaven

        if (not (max_distance == 2 * reikwijdte)):
            return code3
        else:
            return None

    else:
        return None

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
    print()
    print(tussenlanding('ADK', 'DCA', luchthavens, 4000))


if __name__ == '__main__':
    main()