"""
Opdracht 10 - Palindroomzinnen
https://dodona.ugent.be/nl/exercises/23570674/
"""

zinArray = []
reversedArray = []

def main():
    # User input
    aantalZinnen = float(input("Hoeveel zinnen wil je gebruiken: "))

    # Uitvoeren
    getZinArray(aantalZinnen)
    getReversedArray(zinArray)
    checkPalindroom(zinArray, reversedArray)

def getZinArray(aantalZinnen) -> zinArray:
    i = 0
    while i < aantalZinnen:
        # User input
        zin = input("zin: ")

        # Verander de zin
        zin = zin.lower()
        zin = "".join(c for c in zin if c not in ('!', '.', ':', ';'))

        # Zet zin in array
        zinArray.append(zin)
        i = i + 1

def getReversedArray(zinArray) -> reversedArray:
    i = 0
    while i < len(zinArray):
        reversedZin = zinArray[i][::-1]
        # Draai elke zin om
        reversedArray.append(reversedZin)
        i = i + 1

def checkPalindroom(zinArray, reversedArray):
    i = 0
    while i < len(zinArray):
        if zinArray[i] == reversedArray[i]:
            print("Paldindroomzin")
        else:
            print("Geen palindroomzin")
        i = i + 1


if __name__ == "__main__":
    main()