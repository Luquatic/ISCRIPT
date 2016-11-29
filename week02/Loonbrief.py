"""
Opdracht 9 - Loonbrief
https://dodona.ugent.be/nl/exercises/990750894/
"""

# Variables
loonArray = []

def main():

    # User input
    willekeurig = input("Willekeurig getal: ")

    # Maak loonArray aan
    getLoonArray(willekeurig)

    # Bereken totale loon
    totaalLoon = getTotaal(loonArray)

    # Bereken gemiddelde loon
    getGemiddeldeLoon(willekeurig, loonArray, totaalLoon)

def getLoonArray(willekeurig) -> loonArray:
    i = 0
    var = 1
    # Infinite loop
    while var == 1:
        # User input
        loon = input("Loon: ")
        # Add to array
        loonArray.append(loon)

        # Loon must have atleast 3 inputs
        if (loon == "stop" and i < 3):
            print("Loon moet minstens 3 getallen bevatten.")
            loonArray.remove("stop")
            var = 1
        elif (loon == "stop" and i > 2):
            loonArray.remove("stop")
            var = 2
        i = i + 1

def getTotaal(loonArray):
    i = 0
    totaal = 0
    # Bereken totale loon
    while i < len(loonArray):
        totaal = (int(totaal) + int(loonArray[i]))
        i = i + 1
    return totaal

def getGemiddeldeLoon(willekeurig, loonArray, totaalLoon):
    i = 0
    # Print uitvoer per werknemer
    while i < len(loonArray):
        antwoord = (int(willekeurig) + int(loonArray[i]))
        print("Werknemer #" +str(i+1) +" fluistert €"+str(antwoord))
        i = i + 1

    # Print gemiddelde loon
    print("Gemiddeld loon: €" +str(totaalLoon / len(loonArray)))

if __name__ == "__main__":
    main()