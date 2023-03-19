"""
Rajzolj egy üres derékszögű háromszöget programozottan, "n" méretben.
n értékét kérd be. (n>=2)

n=2
|\
--
n=3
|\
| \
---
n=4
|\
| \
|  \
----
n=5
|\
| \
|  \
|   \
-----
"""

szam = int(input('n= '))
utsosor = 0

for i in range(szam):
    utsosor += 1
print(utsosor)

if szam >= 2:
    for sor in range(szam + 1):

        for oszlop in range(szam):
            if sor == szam:
                print("-", end="")

        for oszlop in range(szam):
            if oszlop == 0 and sor != utsosor:
                print("|", end="")

        for oszlop in range(szam):
            if sor == oszlop:
                print("\\", end="")
            else:
                print(" ", end="")
        print()
else:
    print("Ennél nagyobb számot adj meg.")