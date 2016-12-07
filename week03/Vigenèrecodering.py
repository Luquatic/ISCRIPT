"""
Opdracht 15 - Vigenèrecodering
https://dodona.ugent.be/nl/exercises/862295437/
"""

import string

def main():
    # Codeer 1
    codeer('NOBODY EXPECTS THE SPANISH INQUISITION!', 'CIRCUS')

    # Decodeer 1
    decodeer('PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!', 'CIRCUS')

    # Codeer 2
    codeer('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR')

    # Decodeer 2
    decodeer('OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!', 'ARTHUR')


def codeer(tekst: str, sleutelwoord: str) -> None:
    # Verkrijg lengte van tekst
    tekstLengte, tekst = getLengteTekst(tekst)
    # Verkrijg lengte van sleutelwoord
    sleutelwoordLengte = getLengteSleutelwoord(sleutelwoord)
    print(tekstLengte)
    print(sleutelwoordLengte)

    aantalkeer_passend, overige_letters = divmod(tekstLengte, sleutelwoordLengte)
    print(aantalkeer_passend, overige_letters)

    # Verkrijg sleutelzin met de lengte van tekst
    sleutelZin = getSleutelzin(sleutelwoord, aantalkeer_passend, overige_letters)
    print(sleutelZin)

    i = 0
    while i < tekstLengte:
        # Verkrijg letter van string
        letterCode = tekst[:i]
        # Transform eerste letter naar cijfer
        Oi = string.ascii_uppercase.index(letterCode)
        print(Oi)

        # # Verkrijg eerste letter van string
        # letterSleutel = sleutelZin[:i]
        # # Transform eerste letter naar cijfer
        # Si = string.ascii_uppercase.index(letterSleutel)
        #
        # Vi = Oi + Si % 26
        # print(string.ascii_uppercase[Vi])
        i = i + 1

# def decodeer(tekst: str, sleutelwoord: str) -> None:
#     print("decodeer")

def getLengteTekst(tekst):
    # Verwijder spaties van string
    tekst = tekst.replace(" ", "")
    # Verwijder uitroeptekens van string
    tekst = tekst.replace("!", "")
    lengte = len(tekst)
    return lengte, tekst

def getLengteSleutelwoord(sleutelwoord):
    lengte = len(sleutelwoord)
    return lengte

def getSleutelzin(sleutelwoord, aantalkeer_passend, overige_letters):
    zin = sleutelwoord * aantalkeer_passend + sleutelwoord[0:overige_letters]
    return zin


if __name__ == "__main__":
    main()