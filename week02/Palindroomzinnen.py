"""
Opdracht 10 - Palindroomzinnen
https://dodona.ugent.be/nl/exercises/23570674/
"""

def main():
    # Variables
    i = 0
    j = 0
    k = 0
    zinArray = []
    reversedArray = []

    # User input
    aantalZinnen = float(input("Hoeveel zinnen wil je gebruiken: "))

    # Create array
    while i < aantalZinnen:
        # User input
        zin = input("zin: ")

        # Verander de zin
        zin = zin.lower()
        zin = "".join(c for c in zin if c not in ('!', '.', ':', ';'))

        # Zet zin in array
        zinArray.append(zin)
        i = i + 1

    # Draai elke zin om
    while j < len(zinArray):
        reversedZin = zinArray[j][::-1]
        reversedArray.append(reversedZin)
        j = j + 1

    # Check palindroom
    while k < len(zinArray):
        if zinArray[k] == reversedArray[k]:
            print("Paldindroomzin")
            k = k + 1
        else:
            print("Geen palindroomzin")
            k = k + 1


if __name__ == "__main__":
    main()