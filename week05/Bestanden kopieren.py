"""
Opdracht 24
https://dodona.ugent.be/nl/exercises/1985652400/
"""

import shutil

def copy(source, destination):
    shutil.copyfile(source, destination)

def main():
    copy("original.txt", "copy.txt")

if __name__ == '__main__':
    main()