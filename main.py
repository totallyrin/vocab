import random

with open('german.txt') as ger:
    grmn = ger.read().splitlines()

with open('english.txt') as eng:
    engl = eng.read().splitlines()

for i in range(len(grmn)):
    rand = random.randint(0, len(grmn))
    while grmn[rand] == "":
        rand = random.randint(0, len(grmn))
    userin = input(grmn[rand] + ": ")
    while userin not in engl[rand].lower():
        userin = input(grmn[rand] + ": ")
    if userin == "":
        print(engl[rand])
    grmn[rand] = ""

print()

for i in range(len(engl)):
    rand = random.randint(0, len(engl))
    while engl[rand] == "":
        rand = random.randint(0, len(engl))
    userin = input(engl[rand] + ": ")
    while userin not in grmn[rand]:
        userin = input(engl[rand] + ": ")
    if userin == "":
        print(grmn[rand])
    engl[rand] = ""

input()