"""
Opdracht 7 - Interessante getallen
https://dodona.ugent.be/nl/exercises/211647828/
"""

def main():
    # Set variables
    i = 0
    j = 0
    testgevallen = []

    # User input
    aantalGetallen = float(input("Hoeveel test gevallen wil je gebruiken: "))

    # Create array
    while i < aantalGetallen:
        # User input
        testgeval = int(input("Voer een testgeval in: "))
        # Bereken antwoord
        n = findNum(testgeval)
        # Zet antwoord in array
        testgevallen.append(n)

        i = i + 1

    # Print antwoorden
    while j < aantalGetallen:
        print(testgevallen[j])
        j = j + 1


def findNum(testgeval):
    testnum = testgeval
    while testnum <= 1000:
        tempnum = testnum
        sum = 0
        while tempnum > 0:
            sum = sum + (tempnum %10)
            tempnum = int (tempnum / 10)
        if sum == testgeval:
            return testnum
        testnum = testnum + testgeval
    return -1


if __name__ == "__main__":
    main()


