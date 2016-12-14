"""
Opdracht 20 - Zomertijd
https://dodona.ugent.be/nl/exercises/116986379/
"""

from datetime import date, timedelta, datetime

def klok(input: str):
    datum = datetime.strptime(input, '%d/%m/%Y')
    datum = datetime.date(datum)

    zomer = zomertijd(datum.year)
    winter = wintertijd(datum.year)

    if winter < datum and datum > zomer:
        print("wintertijd")

    elif winter > datum and datum > zomer:
        print("zomertijd")

    elif datum == wintertijd(datum.year):
        print("omschakeling van zomertijd naar wintertijd.")

    elif datum == zomertijd(datum.year):
        print("omschakeling van wintertijd naar zomertijd.")

def wintertijd(input: int):
    jaar = input
    dag = date(jaar, 11, 1) - timedelta(1)
    while dag.weekday() is not 6:
        dag = dag - timedelta(1)
    return dag

def zomertijd(input: int):
    jaar = input
    dag = date(jaar, 4, 1) - timedelta(1)
    while dag.weekday() is not 6:
        dag = dag - timedelta(1)
    return dag

def main():
    klok('27/06/2013')

if __name__ == "__main__":
    main()