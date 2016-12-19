"""
Opdracht 23
https://dodona.ugent.be/nl/exercises/1392321201/
"""

import csv

def prijzen(file: str, prijs="", discipline="", jaar=0, nationaliteit="", laureaten=0, motivering=""):
    with open(file) as file:
        fileRead = csv.reader(file, delimiter=";")
        for row in fileRead:
            if prijs in row:
                if str(jaar) in row:
                        print(row[0], "voor de", row[1], "(" +row[2] +")", row[3])


def main():
    prijzen('prijzen.csv', prijs='Nobelprijs', jaar=1994)

if __name__ == '__main__':
    main()