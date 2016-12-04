"""
opdracht 12 - Rorschachtest
https://dodona.ugent.be/nl/exercises/695254392/
"""

regelArray = []
reversedRegelArray = []
rorschachtestArray = []

def main():
    getRegelArray()
    getRorschachtest(regelArray)

def getRegelArray() -> regelArray:
    state = 1

    eersteRegel = input("")
    aantalKarakters = len(eersteRegel)
    regelArray.append(eersteRegel)

    # Infinite loop
    while state == 1:
        regel = input("")
        if regel == "":
            state = 2
        elif len(regel) == aantalKarakters:
            regelArray.append(regel)
        elif len(regel) != aantalKarakters:
            print("Probeer opnieuw")

def getRorschachtest(regelArray):
    i = 0
    while i < len(regelArray):
        print(''.join(regelArray[i] + regelArray[i][::-1]))
        i = i + 1


if __name__ == "__main__":
    main()