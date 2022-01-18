import math

Ax = float(input('Ax='))
Ay = float(input('Ay='))
Bx = float(input('Bx='))
By = float(input('By='))
Cx = float(input('Cx='))
Cy = float(input('Cy='))

Kx = float(input('Kx='))
Ky = float(input('Ky='))
Px = float(input('Px='))
Py = float(input('Py='))
Dx = float(input('Dx='))
Dy = float(input('Dy='))


def pl(Ax, Ay, Bx, By, Cx, Cy):
    a = math.sqrt(((Bx - Ax) ** 2) + (By - Ay) ** 2)
    b = math.sqrt(((Cx - Ax) ** 2) + (Cy - Ay) ** 2)
    c = math.sqrt(((Cx - Cx) ** 2) + (By - Cy) ** 2)
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s


def in_tr(Ax, Ay, Bx, By, Cx, Cy, x, y):
    s_tr1 = pl(Ax, Ay, Bx, By, Cx, Cy)
    s_tr2 = pl(Ax, Ay, Bx, By, x, y) + pl(Ax, Ay, Cx, Cy, x, y) + pl(Bx, By, Cx, Cy, x, y)

    if abs(s_tr1 - s_tr2) < 0.0001:
        return True
    else:
        return False


if in_tr(Ax, Ay, Bx, By, Cx, Cy, Kx, Ky) and in_tr(Ax, Ay, Bx, By, Cx, Cy, Px, Py) and in_tr(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
    print("Трикутник KPD лежить в трикутнику ABC ")
else:
    print("Трикутник KPD  не лежить в трикутнику ABC ")
