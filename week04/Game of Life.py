"""
Opdracht 16 - Game of Life
https://dodona.ugent.be/nl/exercises/511272034/
"""

def showGeneration(tabel):
    for row in tabel:
        line = ""
        for cel in row:
            if cel:
                line += "X"
            else:
                line += "O"
            line += " "

        print(line)

def numberOfNeighbours(tabel, x, y):
    neighbours = 0
    for xOff in range(-1, 2):
        for yOff in range(-1, 2):
            xNeighbour = x + xOff
            yNeighbour = y + yOff
            if (not ((xOff == 0) & (yOff == 0))) & (xNeighbour >= 0) & (yNeighbour >= 0) & (xNeighbour < len(tabel)) & \
                    (yNeighbour < len(tabel[0])):
                if tabel[xNeighbour][yNeighbour]:
                    neighbours += 1
    return neighbours

def nextGeneration(tabel):
    ret = [[False] * len(tabel[0]) for _ in range(len(tabel))]
    for rowIndex in range(len(tabel)):
        row = tabel[rowIndex]
        for celIndex in range(len(row)):
            cel = row[celIndex]
            neighbours = numberOfNeighbours(tabel, rowIndex, celIndex)
            if neighbours == 2:
                ret[rowIndex][celIndex] = cel
            elif neighbours == 3:
                ret[rowIndex][celIndex] = True
            else:
                ret[rowIndex][celIndex] = False
    return ret


def main():
    generation = [[True] + [False] * 7 for _ in range(6)]
    showGeneration(generation)

    print(numberOfNeighbours(generation, 0, 0))
    print(numberOfNeighbours(generation, 1, 1))
    print(numberOfNeighbours(generation, 2, 2))
    print()

    next = nextGeneration(generation)
    showGeneration(next)
    print()
    next = nextGeneration(next)
    showGeneration(next)
    print()
    next = nextGeneration(next)
    showGeneration(next)
    print()
    next = nextGeneration(next)
    showGeneration(next)

if __name__ == '__main__':
    main()