"""
opdracht 11 - Sterke wachtwoorden
https://dodona.ugent.be/nl/exercises/417422714/
"""

# Variables
wachtwoordArray = []
i = 0

def main():
    # User input
    aantalWachtwoorden = float(input("Hoeveel zinnen wil je gebruiken: "))

    # Create array
def getAantalWachtwoordenArray(aantalWachtwoorden, i) -> wachtwoordArray:
    if aantalWachtwoorden >= 1 and aantalWachtwoorden <= 100:
        while i < aantalWachtwoorden:
            # User input
            ww = input("zin: ")

            # Zet wachtwoord in array
            wachtwoordArray.append(ww)
            i = i + 1
    else:
        print("error")

if __name__ == "__main__":
    main()