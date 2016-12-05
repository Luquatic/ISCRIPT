"""
Opdracht 14 - Levensverwachting
https://dodona.ugent.be/nl/exercises/849566952/
"""

global levensverwachting

def main():
    levensverwachting = 70
    levensverwachting = getGeslacht(levensverwachting)
    levensverwachting = getRoker(levensverwachting)
    levensverwachting = getSport(levensverwachting)
    levensverwachting = getAlcohol(levensverwachting)
    levensverwachting = getFastfood(levensverwachting)
    getLevensverwachting(levensverwachting)

def getGeslacht(levensverwachting):
    geslacht = input("Man of vrouw? ")
    if geslacht == "man":
        return levensverwachting
    elif geslacht == "vrouw":
        levensverwachting = levensverwachting + 4
        return levensverwachting
    else:
        print("error")
        quit()

def getRoker(levensverwachting):
    roker = input("Rookt u? ")
    if roker == "ja":
        roker = True
        levensverwachting = levensverwachting - 5
        return levensverwachting
    elif roker == "nee":
        roker = False
        levensverwachting = levensverwachting + 5
        return levensverwachting
    else:
        print("error")
        quit()

def getSport(levensverwachting):
    sport = int(input("Hoeveel uur in de week sport u? "))
    if sport == 0:
        levensverwachting = levensverwachting - 3
        return levensverwachting
    elif sport > 0:
        levensverwachting = levensverwachting + sport
        return levensverwachting
    else:
        print("error")
        quit()

def getAlcohol(levensverwachting):
    alcohol = int(input("Hoeveel glazen alcohol in de week drinkt u? "))
    if alcohol == 0:
        levensverwachting = levensverwachting + 2
        return levensverwachting
    elif alcohol <= 7:
        return levensverwachting
    elif alcohol > 7:
        newAlcohol = (alcohol - 7) * 0.5
        levensverwachting = levensverwachting - newAlcohol
        return levensverwachting
    else:
        print("error")
        quit()

def getFastfood(levensverwachting):
    fastfood = input("Eet u vaak fastfood? ")
    if fastfood == "ja":
        fastfood = True
        return levensverwachting
    elif fastfood == "nee":
        fastfood = False
        levensverwachting = levensverwachting + 3
        return levensverwachting
    else:
        print("error")
        quit()

def getLevensverwachting(levensverwachting):
    print(float(levensverwachting))



if __name__ == "__main__":
    main()