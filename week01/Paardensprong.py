"""
Opdracht 4 - Paardensprong
https://dodona.ugent.be/nl/exercises/56374393/
"""

def main():
    # User input
    begin = input("Voer begin coordinaten in: ")
    eind = input("Voer eind coordinaten in: ")

    # Waarden splitsen
    bl, bc = (list(begin))
    el, ec = (list(eind))

    # Naar ascii waarden
    bl = ord(bl)-96
    bc = ord(bc)-48
    el = ord(el)-96
    ec = ord(ec)-48

    # Sprong berekenen
    sprong(bl, bc, el, ec, begin, eind)


def sprong(bl, bc, el, ec, begin, eind):
    if (bl == el or bc == ec):
        print("Het paard kan niet springen van %s naar %s" % (begin, eind))
    elif (bl < 1 or bl > 8 or bc < 1 or bc > 8):
        print("Deze positie bestaat niet")
    elif (el < 1 or el > 8 or ec < 1 or ec > 8):
        print("Deze positie bestaat niet")
    elif ((bl +2 == el or bl -2 == el) and (bc +1 == ec or bc -1 == ec)):
        print("Het paard kan springen van %s naar %s" % (begin, eind))
    elif ((bl +1 == el or bl -1 == el) and (bc +2 == ec or bc -2 == ec)):
        print("Het paard kan springen van %s naar %s" % (begin, eind))
    else:
        print("Het paard kan niet springen van %s naar %s" % (begin, eind))

if __name__ == "__main__":
    main()