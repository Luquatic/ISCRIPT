"""
Opdracht 15 - Vigenèrecodering
https://dodona.ugent.be/nl/exercises/862295437/
"""

import string

def codeer(tekst: str, sleutelwoord: str) -> None:
    tekstLengte = getLengteTekst(tekst)
    sleutelwoordLengte = len(sleutelwoord)
    # Kijkt hoevaak het sleutelwoord in de tekst kan en slaat de overige letters op
    aantalkeer_passend, overige_letters = divmod(tekstLengte, sleutelwoordLengte)
    # Verkrijg sleutelzin met de lengte van tekst
    sleutelZin = getSleutelzin(sleutelwoord, aantalkeer_passend, overige_letters)
    # Verander tekst naar versleutelde tekst
    tekstVersleuteld = getTekstVersleuteld(tekst, sleutelZin)
    print(''.join(tekstVersleuteld))

def decodeer(tekst: str, sleutelwoord: str) -> None:
    tekstLengte = getLengteTekst(tekst)
    sleutelwoordLengte = len(sleutelwoord)
    # Kijkt hoevaak het sleutelwoord in de tekst kan en slaat de overige letters op
    aantalkeer_passend, overige_letters = divmod(tekstLengte, sleutelwoordLengte)
    # Verkrijg sleutelzin met de lengte van tekst
    sleutelZin = getSleutelzin(sleutelwoord, aantalkeer_passend, overige_letters)
    # Verander tekst naar versleutelde tekst
    tekstUnlocked = getTekstUnlocked(tekst, sleutelZin)
    print(''.join(tekstUnlocked))

def getTekstVersleuteld(tekst, sleutelZin):
    tekstVersleuteld = []
    i = 0
    while i < len(tekst):
        # Verkrijg letter van string
        letterTekst = tekst[i]

        if letterTekst.isalpha():
            # Transform letter naar cijfer
            Oi = string.ascii_uppercase.index(letterTekst)
            # Verkrijg letter van string
            letterSleutel = sleutelZin[i]
            # Transform letter naar cijfer
            Si = string.ascii_uppercase.index(letterSleutel)
            # Bereken ascii
            Vi = (Oi + Si) % 26
            tekstVersleuteld.append((string.ascii_uppercase[Vi]))
        else:
            tekstVersleuteld.append(letterTekst)
        i = i + 1

    return tekstVersleuteld


def getTekstUnlocked(tekst, sleutelZin):
    tekstUnlocked = []
    i = 0
    while i < len(tekst):
        # Verkrijg letter van string
        letterTekst = tekst[i]

        if letterTekst.isalpha():
            # Transform letter naar cijfer
            Vi = string.ascii_uppercase.index(letterTekst)
            # Verkrijg letter van string
            letterSleutel = sleutelZin[i]
            # Transform letter naar cijfer
            Si = string.ascii_uppercase.index(letterSleutel)
            # Bereken ascii
            Oi = (Vi - Si) % 26
            tekstUnlocked.append((string.ascii_uppercase[Oi]))
        else:
            tekstUnlocked.append(letterTekst)
        i = i + 1

    return tekstUnlocked

def getLengteTekst(tekst):
    lengte = len(tekst)
    return lengte

def getSleutelzin(sleutelwoord, aantalkeer_passend, overige_letters):
    zin = sleutelwoord * aantalkeer_passend + sleutelwoord[0:overige_letters]
    return zin

def main():
    # Codeer 1
    codeer('NOBODY EXPECTS THE SPANISH INQUISITION!', 'CIRCUS')

    # Decodeer 1
    decodeer('PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!', 'CIRCUS')

    # Codeer 2
    codeer('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR')

    # Decodeer 2
    decodeer('OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!', 'ARTHUR')

if __name__ == "__main__":
    main()