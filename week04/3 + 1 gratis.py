"""
Opdracht 17 - 3 + 1 gratis
https://dodona.ugent.be/nl/exercises/751779411/
"""

def winst(samenAntwd, gegroepeerdAntwd):
    winst = float(samenAntwd) - float(gegroepeerdAntwd)
    # Print winst tot in tiende
    print("%.1f" % winst)


def gegroepeerd(prijzen):
    grp1 = prijzen[0:4]
    grp2 = prijzen[4:8]
    grp3 = prijzen[8:12]

    # Verwijderd het laatste getal in de list
    del grp1[-int(1):]
    del grp2[-int(1):]

    a = sum(grp1)
    b = sum(grp2)
    c = sum(grp3)
    prijs = a + b + c
    print(prijs)
    return prijs

def groeperen(prijzen):
    # Pakt de eerste 4 van de list en maakt er een tuple van
    grp1 = tuple(prijzen[0:4])
    # Pakt de tweede 4 van de list en maakt er een tuple van
    grp2 = tuple(prijzen[4:8])
    # Pakt de derde 4 van de list en maakt er een tuple van
    grp3 = tuple(prijzen[8:12])

    print(grp1, grp2, grp3)

def samen(prijzen):
    # Maakt kopie van prijzen zodat prijzen hergebruikt kan worden
    kopie = list(prijzen)
    # Kijkt hoeveel producten gratis zijn
    aantal = len(prijzen) / 4
    # Verwijderd de aantal gratis producten van list
    del kopie[-int(aantal):]
    # Print nieuwe prijs tot in honderdste
    prijs = ("%.2f" % (sum(kopie)))
    print(prijs)
    return prijs

def main():
    # Sorteerd prijzen van hoog naar laag
    prijzen = sorted([3.23, 5.32, 8.23, 2.23, 9.98, 7.43, 6.43, 8.23, 4.23], reverse=True)
    samenAntwd = samen(prijzen)
    groeperen(prijzen)
    gegroepeerdAntwd = gegroepeerd(prijzen)
    winst(samenAntwd, gegroepeerdAntwd)

if __name__ == "__main__":
    main()