from math import pi

y0 = pi / 999
print(y0)
y1 = pi / 999
print(y1)
y2 = (pi - 400 * y0 - 500 * y1) / 99
print(y2)
for i in range(int(input())):
    y3 = (pi - 400 * y1 - 500 * y2) / 99
    y1 = y2
    y2 = y3
    print(y3)
