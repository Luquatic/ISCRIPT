"""
Opdracht 22
https://dodona.ugent.be/nl/exercises/189652425/
"""

def cryptogram(opgave, oplossing):
    dictionary = {}
    for index in range(len(opgave)):
        if oplossing[index] is not "?":
            dictionary[opgave[index].lower()] = oplossing[index].lower()
            dictionary[opgave[index].upper()] = oplossing[index].upper()
    ret = ""
    for c in opgave:
        if c in dictionary:
            ret += dictionary[c]
        else:
            ret += "?"
    return ret

def main():
    opgave = 'Qmvrbwlf xwkd iopzlw vf zml pcwvfxzvyl.'
    oplossing = 'Ch?ld??? ??ow fas??r ?n ??? ?p?i?gt?me.'
    print(cryptogram(opgave, oplossing))

    opgave = 'Zhp suxobpuw sbmtkopw Nxwkdnx.'
    oplossing = '?h? p?n???a? ?rod?ces I???l??.'
    print(cryptogram(opgave, oplossing))

    opgave = 'Jujso ldmtq wyjqi tvadi ltek tq lads tw t wcqnej xjee.'
    oplossing = '?v?ry ??ma? ?p??? ?bout h??f ?? ???? ?s ? ??ng?e c?l?.'
    print(cryptogram(opgave, oplossing))

    opgave = "V atult'a amrdd qvl zr nrbrqbrn zx v wumvl v medr vivx."
    oplossing = "? ????k's ???l? ??n ?? ??t???ed ?y a hum?? ? ?i?? ?w??."
    print(cryptogram(opgave, oplossing))


if __name__ == '__main__':
    main()