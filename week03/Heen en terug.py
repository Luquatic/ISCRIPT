"""
Opdracht 13 - Heen en terug
https://dodona.ugent.be/nl/exercises/738605545/
"""

def decodeer(boodschap: str, aantalKarakters: int):
    array = makeArray(boodschap, aantalKarakters)
    ontcijfer(array, aantalKarakters)

def makeArray(boodschap, aantalKarakters):
    array = []
    i = 0
    teller = 1
    karakterCount = aantalKarakters

    while i < len(boodschap):
        if teller % 2 == 0:
            array.append(boodschap[i:karakterCount][::-1])
        else:
            array.append(boodschap[i:karakterCount])
        teller = teller + 1
        i = i + aantalKarakters
        karakterCount = karakterCount + aantalKarakters

    return array

def ontcijfer(array, aantalKarakters):
    ontcijfer = []
    for i in range(0, aantalKarakters):
        for rij in array:
            ontcijfer.append(rij[i])

    print(''.join(ontcijfer))

def main():
    decodeer('aoesifibolwkrdexeioayngoxxfhtslhtlx', 5)

    decodeer('aohpdntilirndsnefxxftgonomceexxrloewftmyex', 6)

if __name__ == '__main__':
    main()