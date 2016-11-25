"""
Opdracht 5 - Territoriale wateren
https://dodona.ugent.be/nl/exercises/587558403/
"""
import math

def main():
    # User input
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    x3 = float(input("x3: "))
    y3 = float(input("y3: "))

    # Voetpunt berekenen
    isVoetpunt = getVoetpunt(x1, x2, x3, y1, y2, y3)

    # Afstand berekenen
    isAfstand = getAfstand(isVoetpunt, x3, y3)

    # Zone berekenen
    isZone = getZone(isAfstand)

    # Print uitkomst
    print("voetpunt: " + str(isVoetpunt))
    print("afstand: " + str(isAfstand) + " zeemijl")
    print("zone: " + str(isZone))

def getVoetpunt(x1, x2, x3, y1, y2, y3):
    # Verkrijg u
    u = ((x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1)) / (math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    # Verkrijg xv en yv
    xv = x1 + u * (x2 - x1)
    yv = y1 + u * (y2 - y1)

    # Maak voetpunt
    voetpunt = (xv, yv)
    return voetpunt

def getAfstand(isVoetpunt, x3, y3):
    # isVoetpunt splitsen naar xv en yv
    xv, yv = isVoetpunt

    # Verkrijg a
    a = math.sqrt(math.pow(xv - x3, 2) + math.pow(yv - y3, 2))

    # Maak afstand
    afstand = a
    return afstand

def getZone(isAfstand):
    # Zone berekenen
    if (isAfstand >= 0 and isAfstand <= 12):
        zone = "territoriale wateren"
    elif (isAfstand > 12 and isAfstand <= 24):
        zone = "aansluitende zone"
    elif (isAfstand > 24 and isAfstand <= 200):
        zone = "exclusieve economische zone"
    elif (isAfstand > 200):
       zone = "internationale wateren"
    else:
        zone = "something went wrong"

    # Verkrijg zone
    zoneBerekend = zone
    return zoneBerekend

if __name__ == "__main__":
    main()