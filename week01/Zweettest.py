"""
Opdracht 6 - Zweettest
https://dodona.ugent.be/nl/exercises/1173716008/
"""

def main():
    # User input
    leeftijdInMaanden = float(input("Leeftijd in maanden: "))
    chloride = float(input("Chlorideconcentratie: "))

    # Bereken of patient ouder of jonger is dan 6 maanden
    isOuderJonger = getOuderJonger(leeftijdInMaanden)

    # Bereken chlorideconcentratie
    isChloride = getChloride(chloride, isOuderJonger)

    # Print uitkomst
    print("CF " + isChloride)

def getOuderJonger(leeftijdInMaanden):
    if (leeftijdInMaanden <= 6):
        ouderJonger = "jonger"
    else:
        ouderJonger = "ouder"

    # Verkrijg leeftijd
    leeftijdBerekend = ouderJonger
    return leeftijdBerekend

def getChloride(chloride, isOuderJonger):
    if (isOuderJonger == "jonger"):
        if (chloride <= 29):
            chloride = "is hoogst onwaarschijnlijk"
        elif (chloride > 29 and chloride < 60):
            chloride = "is mogelijk"
        elif (chloride >= 60):
            chloride = "is waarschijnlijk"

    if (isOuderJonger == "ouder"):
        if (chloride <= 39):
            chloride = "is hoogst onwaarschijnlijk"
        elif (chloride > 39 and chloride < 60):
            chloride = "is mogelijk"
        elif (chloride >= 60):
            chloride = "is waarschijnlijk"

    # Verkrijg chloride
    chlorideBerekend = chloride
    return chlorideBerekend


if __name__ == "__main__":
    main()