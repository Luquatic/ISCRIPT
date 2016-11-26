"""
Opdracht 2 - Radialen naar graden
https://dodona.ugent.be/nl/exercises/975017137/
"""

import math

def main():
    # User input
    aantalRadiaal = input("Aantal radialen:\n")

    # Graden berekenen
    graden = math.degrees(aantalRadiaal)

    # Graden naar GMS omzetten
    gradenToGMS(graden)

def gradenToGMS(graden):
    isPositive = graden >= 0
    minutes,seconds = divmod(graden*3600,60)
    degrees, minutes = divmod(minutes,60)
    degrees = degrees if isPositive else -degrees

    # Uitkomst printen
    print (int(degrees))
    print (int(minutes))
    print (int(seconds))

if __name__ == "__main__":
    main()

