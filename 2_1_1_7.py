"""
Дано пятизначное или шестизначное натуральное число. Напишите программу,
которая изменит порядок его последних пяти цифр на обратный.
"""
cislo = input()
if len(cislo) == 5:
    cfp = cislo[::-1].lstrip("0")
    print(cfp)
elif len(cislo) == 6:
    cfp = (cislo[0] + cislo[-1:-6:-1]).lstrip("0")
    print(cfp)

