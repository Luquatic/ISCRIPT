"""
Opdracht 23
https://dodona.ugent.be/nl/exercises/1392321201/
"""

import csv

def eerste(file:str, prijs=None, jaar=None):
    with open(file) as file:
        fileRead = csv.reader(file, delimiter=";")
        for row in fileRead:
            if prijs in row:
                if str(jaar) in row:
                    print(row[0], "voor de", row[1], "(" +row[2] +")", row[3])

def tweede(file:str, nationaliteit=None):
    with open(file) as file:
        fileRead = csv.reader(file, delimiter=";")
        for row in fileRead:
            if nationaliteit is not None:
                if any(nationaliteit in s for s in row):
                    print(row[0], "voor de", row[1], "(" + row[2] + ")", row[3])

def derde(file:str, discipline=None, laureaten=None):
    with open(file) as file:
        fileRead = csv.reader(file, delimiter=";")
        for row in fileRead:
            if discipline in row:

                    print(row[0], "voor de", row[1], "(" + row[2] + ")", row[3])

def prijzen(file: str, prijs=None, discipline=None, jaar=None, nationaliteit=None, laureaten=None, motivering=None):
    eerste(file, prijs, jaar)
    tweede(file, nationaliteit)


def main():
    prijzen('prijzen.csv', prijs='Nobelprijs', jaar=1994)
    prijzen('prijzen.csv', prijs='Nobelprijs', discipline='wiskunde')
    prijzen('prijzen.csv', nationaliteit='Bel')
    prijzen('prijzen.csv', discipline='scheikunde', laureaten=3)

if __name__ == '__main__':
    main()