"""
На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые
в соответствии со стандартным американским соглашением о запятых в больших числах.
"""

cislo = input()
if len(cislo) <= 3:
    print(cislo)
elif len(cislo) > 3:
    if len(cislo) % 3 == 0:
        comma_cnt = (len(cislo) // 3) - 1
    elif len(cislo) % 3 != 0:
        comma_cnt = len(cislo) // 3

    final_cislo = []
    n = -1
    k = -4
    while comma_cnt != -1:
        final_cislo.append((cislo[n:k:-1])[::-1])
        n += -3
        k += -3
        comma_cnt -= 1
    d = ",".join(final_cislo[::-1])
    print(d)
