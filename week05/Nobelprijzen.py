"""
Opdracht 23
https://dodona.ugent.be/nl/exercises/1392321201/
"""

import csv

def prijsFilter(fileList, prijs):
    filter = []
    for row in fileList:
        if prijs == row[0].lower():
            filter.append(row)

    return filter

def disciplineFilter(fileList, discipline):
    filter = []
    for row in fileList:
        if discipline == row[1].lower():
            filter.append(row)

    return filter

def jaarFilter(fileList, jaar):
    filter = []
    for row in fileList:
        if str(jaar) == row[2].lower():
            filter.append(row)
    return filter

def nationaliteitFilter(fileList, nationaliteit):
    filter = []
    for row in fileList:
        if "(" +nationaliteit.lower() +")" in row[3].lower():
            filter.append(row)
    return filter

def laureatenFilter(fileList, laureaten):
    filter = []
    for row in fileList:
        if len(row[3].split(",")) >= laureaten:
            filter.append(row)

    return filter

def motiveringFilter(fileList, motivering):
    filter = []
    for row in fileList:
        if motivering in row[4]:
            filter.append(row)

    return filter


def prijzen(file: str, prijs=None, discipline=None, jaar=None, nationaliteit=None, laureaten=None, motivering=None):
    # Opent de file
    with open(file, encoding='utf-8') as file:
        fileRead = csv.reader(file, delimiter=";")
        # Maakt een copie van de file zodat deze in een andere functie gebruikt kan worden
        fileList = list(fileRead)

    if prijs != None:
        fileList = prijsFilter(fileList, prijs)
    if discipline != None:
        fileList = disciplineFilter(fileList, discipline)
    if jaar != None:
        fileList = jaarFilter(fileList, jaar)
    if nationaliteit != None:
        fileList = nationaliteitFilter(fileList, nationaliteit)
    if laureaten != None:
        fileList = laureatenFilter(fileList, laureaten)
    if motivering != None:
        fileList = motiveringFilter(fileList, motivering)

    for row in fileList:
        print(row[0], "voor de", row[1], "(" + row[2] + ")", row[3])
    print("\n")


def main():
    prijzen('prijzen.csv', prijs='nobelprijs', jaar=1994)
    prijzen('prijzen.csv', prijs='nobelprijs', discipline='wiskunde')
    prijzen('prijzen.csv', nationaliteit='bel')
    prijzen('prijzen.csv', discipline='scheikunde', laureaten=3)
    prijzen('prijzen.csv', motivering='röntgen', discipline='natuurkunde', nationaliteit='GB')

if __name__ == '__main__':
    main()