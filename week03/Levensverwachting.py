"""
Opdracht 14 - Levensverwachting
https://dodona.ugent.be/nl/exercises/849566952/
"""

def berekenGeslacht(leeftijd, geslacht: str):
    if geslacht == 'man':
        return leeftijd
    else:
        leeftijd = leeftijd + 4
        return leeftijd

def berekenRoker(leeftijd, roker: bool):
    if roker == True:
        leeftijd = leeftijd - 5
        return leeftijd
    else:
        leeftijd = leeftijd + 5
        return leeftijd

def berekenSport(leeftijd, sport: int):
    if sport == 0:
        leeftijd = leeftijd - 3
        return leeftijd
    elif sport > 0:
        leeftijd = leeftijd + sport
        return leeftijd

def berekenAlcohol(leeftijd, alcohol: int):
    if alcohol == 0:
        leeftijd = leeftijd + 2
        return leeftijd
    elif alcohol <= 7:
        return leeftijd
    else:
        newAlcohol = (alcohol - 7) * 0.5
        leeftijd = leeftijd - newAlcohol
        return leeftijd

def berekenFastfood(leeftijd, fastfood: bool):
    if fastfood == True:
        return leeftijd
    else:
        leeftijd = leeftijd + 3
        return leeftijd

def levensverwachting(geslacht: str, roker: bool, sport: int, alcohol: int, fastfood: bool):
    leeftijd = 70
    leeftijd = berekenGeslacht(leeftijd, geslacht)
    leeftijd = berekenRoker(leeftijd, roker)
    leeftijd = berekenSport(leeftijd, sport)
    leeftijd = berekenAlcohol(leeftijd, alcohol)
    leeftijd = berekenFastfood(leeftijd, fastfood)
    print('%.1f' % leeftijd)

def main():
    levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10, fastfood=True)
    levensverwachting(geslacht='man', roker=True, sport=5, alcohol=5, fastfood=True)
    levensverwachting(geslacht='vrouw', roker=False, sport=5, alcohol=0, fastfood=False)
    levensverwachting(geslacht='vrouw', roker=False, sport=3, alcohol=14, fastfood=True)
    levensverwachting(geslacht='man', roker=False, sport=4, alcohol=4, fastfood=False)

if __name__ == '__main__':
    main()