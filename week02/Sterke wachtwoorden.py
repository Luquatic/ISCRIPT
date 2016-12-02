"""
opdracht 11 - Sterke wachtwoorden
https://dodona.ugent.be/nl/exercises/417422714/
"""

# Variables
wachtwoordArray = []
global aantalVoorwaarden

def main():
    # User input
    aantalWachtwoorden = float(input("Hoeveel wachtwoorden wil je gebruiken: "))

    # Create array
    getAantalWachtwoordenArray(aantalWachtwoorden)

    # Check elk wachtwoord op zijn sterkte
    for wachtwoord in wachtwoordArray:
        aantalVoorwaarden = 0
        # Check aantal karakters
        aantalVoorwaarden = aantalKarakters(aantalVoorwaarden, wachtwoord)
        # Check hoofdletter
        aantalVoorwaarden = heeftHoofdletter(aantalVoorwaarden, wachtwoord)
        # Check kleine letter
        aantalVoorwaarden = heeftKleineletter(aantalVoorwaarden, wachtwoord)
        # Check cijfer
        aantalVoorwaarden = heeftCijfer(aantalVoorwaarden, wachtwoord)
        # Check speciale karakter
        aantalVoorwaarden = heeftSpeciaalKarakter(aantalVoorwaarden, wachtwoord)
        # Check sterkte
        wwSterkte = wachtwoordSterkte(aantalVoorwaarden)
        print(wwSterkte)


def getAantalWachtwoordenArray(aantalWachtwoorden) -> wachtwoordArray:
    i = 0
    if aantalWachtwoorden >= 1 and aantalWachtwoorden <= 100:
        while i < aantalWachtwoorden:
            # User input
            ww = input("Wachtwoord: ")

            # Zet wachtwoord in array
            wachtwoordArray.append(ww)
            i = i + 1
    else:
        print("error")

def aantalKarakters(aantalVoorwaarden, wachtwoord):
    if len(wachtwoord) >= 8:
        aantalVoorwaarden = aantalVoorwaarden + 1
        return aantalVoorwaarden
    else:
        return aantalVoorwaarden

def heeftHoofdletter(aantalVoorwaarden, wachtwoord):
    for karakter in wachtwoord:
        if karakter.isupper():
            aantalVoorwaarden = aantalVoorwaarden + 1
            return aantalVoorwaarden
    else:
        return aantalVoorwaarden

def heeftKleineletter(aantalVoorwaarden, wachtwoord):
    for karakter in wachtwoord:
        if karakter.islower():
            aantalVoorwaarden = aantalVoorwaarden + 1
            return aantalVoorwaarden
    else:
        return aantalVoorwaarden

def heeftCijfer(aantalVoorwaarden, wachtwoord):
    for karakter in wachtwoord:
        if karakter.isdigit():
            aantalVoorwaarden = aantalVoorwaarden + 1
            return aantalVoorwaarden
    else:
        return aantalVoorwaarden

def heeftSpeciaalKarakter(aantalVoorwaarden, wachtwoord):
    valid = set('!@#$%^&*()_-+=,./?;:{[}]')
    for karakter in wachtwoord:
        if karakter in valid:
            aantalVoorwaarden = aantalVoorwaarden + 1
            return aantalVoorwaarden
    else:
        return aantalVoorwaarden

def wachtwoordSterkte(aantalVoorwaarden):
    if aantalVoorwaarden < 3:
        wachtwoordSterkte = "zwak"
    elif aantalVoorwaarden == 3 or aantalVoorwaarden == 4:
        wachtwoordSterkte = "matig"
    else:
        wachtwoordSterkte = "sterk"
    return wachtwoordSterkte

if __name__ == "__main__":
    main()