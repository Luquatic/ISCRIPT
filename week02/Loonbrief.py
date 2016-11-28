"""
Opdracht 9 - Loonbrief
https://dodona.ugent.be/nl/exercises/990750894/
"""

def main():
    # Variables
    i = 0
    j = 0
    totaal = 0
    x = 0
    var = 1
    loonArray = []

    # User input
    willekeurig = input("Willekeurig getal: ")

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

    # Bereken totale loon
    while j < len(loonArray):
        totaal = (int(totaal) + int(loonArray[j]))
        j = j + 1

    # Print uitvoer per werknemer
    while x < len(loonArray):
        antwoord = (int(willekeurig) + int(loonArray[x]))
        print("Werknemer #" +str(x+1) +" fluistert €"+str(antwoord))
        x = x + 1

    # Print gemiddelde loon
    print("Gemiddeld loon: €" +str(totaal / len(loonArray)))

if __name__ == "__main__":
    main()