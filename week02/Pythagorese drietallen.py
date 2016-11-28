"""
Opdracht 8 - Pythagorese drietallen
https://dodona.ugent.be/nl/exercises/683768040/
"""

def main():
    # User input
    n = int(input("Voer getal in: "))

    # Bereken Pythagorees drietal
    pythagorees(n)

def pythagorees(n):
    if n > 0:
        for a in range (1, n-1):
            for b in range (a +1, n):
                for c in range (b+1, n+1):
                    if a**2 + b**2 == c**2 and a + b + c == n:
                        print(a,b,c)

if __name__ == "__main__":
    main()
