# 2.1 Часть 1
# https://stepik.org/lesson/415553/step/3?unit=405082

# put your python code here
massa, rost = float(input()), float(input())
imt = massa / (rost * rost)
if 18.5 <= imt <= 25:
    print("Оптимальная масса")
elif imt > 25:
    print("Избыточная масса")
else:
    print("Недостаточная масса")