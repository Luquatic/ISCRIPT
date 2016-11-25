"""
Opdracht 2 - Radialen naar graden
https://dodona.ugent.be/nl/exercises/975017137/
"""

import math

aantalRadiaal = input("Aantal radialen:\n")

graden = math.degrees(aantalRadiaal)

def gradenToGMS(graden):
    isPositive = graden >= 0
    minutes,seconds = divmod(graden*3600,60)
    degrees, minutes = divmod(minutes,60)
    degrees = degrees if isPositive else -degrees
    print (int(degrees))
    print (int(minutes))
    print (int(seconds))

gradenToGMS(graden)

