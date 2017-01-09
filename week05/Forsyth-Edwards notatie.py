"""
Opdracht 21
https://dodona.ugent.be/nl/exercises/867899652/
"""

import re

def grid2fen(grid, ascii="*"):
    fen = ""
    gridLines = grid.split("\n")
    for line in gridLines:
        if ascii in line:
            newLine = ""
            count = 0
            for c in line:
                if c == ascii:
                    count += 1
                else:
                    if count > 0:
                        newLine += str(count)
                        count = 0
                    newLine += c
            if count > 0:
                newLine += str(count)
            line = newLine
        fen += line + "/"
    return re.sub("/+$", "", fen)


def fen2grid(fen, ascii="*"):
    grid = ""
    fenLines = fen.split("/")
    for line in fenLines:
        if re.match("[0-9]", line) is not None:
            for i in range(1, 9):
                line = line.replace(str(i), ascii * i)
        grid += line + "\n"
    return grid

def main():
    print(fen2grid('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'))
    print(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', '.'))
    print(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '+'))
    rooster = '''rnbqkbnr
    pppppppp
    ********
    ********
    ********
    ********
    PPPPPPPP
    RNBQKBNR'''
    print(grid2fen(rooster))
    print(grid2fen(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR')))
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '.'), '.'))
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R', '+'), '+'))

if __name__ == '__main__':
    main()