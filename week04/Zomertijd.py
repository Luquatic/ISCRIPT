"""
Opdracht 20 - Zomertijd
https://dodona.ugent.be/nl/exercises/116986379/
"""

import calendar
from datetime import date, timedelta

def wintertijd():
    print("wintertijd")

def zomertijd(input: int):
    cal = calendar.Calendar(0)
    month = cal.monthdatescalendar(input, 3)
    lastweek = month[-1]
    sunday = lastweek[6]
    print(sunday)

def main():
    vandaag = date.today()
    morgen = vandaag + timedelta(1)

    zomertijd(2013)

if __name__ == "__main__":
    main()