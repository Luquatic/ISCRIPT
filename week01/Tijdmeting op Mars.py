"""
Opdracht 1 - Tijdmeting op Mars
https://dodona.ugent.be/nl/exercises/1813154454/
"""

aantalSol = input("Aantal sol: ")

solSeconds = (int(aantalSol) * 88775.24409)

def main(solSeconds):
    solDays = solSeconds / 86400
    solHours = (solSeconds / 3600) % 24
    solMinutes = (solSeconds / 60) % 60
    solSeconds = solSeconds % 60
    print(aantalSol), "sol = " , int(solDays) , "dagen, " , int(solHours) , "uren, " , int(solMinutes) , "minuten, " , int(solSeconds) , "seconden"

if __name__ == "__main__":
    main(solSeconds)

