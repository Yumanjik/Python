# Данная программа решает квадратные уравнения вида ax^2 + bx + c = 0 и выводит его корни
import math


def square():
    print("Введите коэффициенты для уравнения \nax^2 + bx + c = 0:")

    try:
        a = float(input("a = "))
    except ValueError:
        print("Ошибка 1 \nНеверный формат введённых данных")
        return 'Ошибка 1'

    try:
        b = float(input("b = "))
    except ValueError:
        print('Ошибка 1 \nНеверный формат введённых данных')
        return 'Ошибка 1'

    try:
        c = float(input("c = "))
    except ValueError:
        print('Ошибка 1 \nНеверный формат введённых данных')
        return 'Ошибка 1'

    discr = b ** 2 - 4 * a * c  # Нахождение дискриминанта
    print("Дискриминант D = %.2f" % discr)

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)  # Нахождение корней квадратного уравнения, если дискриминант больше нуля
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        return x1, x2
    elif discr == 0:  # Нахождение корня квадратного уравнения, если дискриминант равен нулю
        x = -b / (2 * a)
        print("x = %.2f" % x)
        return x
    else:
        print("Корней нет")  # Корней квадратного уравнения нет, так как дискриминант меньше нуля
        return None


square()
