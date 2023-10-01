import math


def square():
    print("Введите коэффициенты для уравнения \nax^2 + bx + c = 0:")


    try:
        a = float(input("a = "))
    except ValueError:
        print("Ошибка 1 \nНеверный формат введённых данных")
        return

    try:
        b = float(input("b = "))
    except ValueError:
        print('Ошибка 1 \nНеверный формат введённых данных')
        return

    try:
        c = float(input("c = "))
    except ValueError:
        print('Ошибка 1 \nНеверный формат введённых данных')
        return

    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
        return x
    else:
        print("Корней нет")
        return None


square()
