# Данная программа решает квадратные уравнения вида ax^2 + bx + c = 0 и выводит его корни


import math                     #Библиотеки необходимые для работы программы
from tkinter import *
from tkinter import messagebox


def square(a, b, c):            #Функция нахождения корней квадратного уравнения

    try:

        discr = b ** 2 - 4 * a * c  # Нахождение дискриминанта

        if discr > 0:   # Нахождение корней квадратного уравнения, если дискриминант больше нуля

            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)

            return "x1 = %.2f\nx2 = %.2f" % (x1, x2)

        elif discr == 0:  # Нахождение корня квадратного уравнения, если дискриминант равен нулю

            x = -b / (2 * a)

            return "x = %.2f" % x

        else:   # Корней квадратного уравнения нет, так как дискриминант меньше нуля

            return "Корней нет"

    except ZeroDivisionError:   # Отлов ошибки деления на 0

        return 'Ошибка 2 \nКоэффициент "а" не может быть нулём'


def btnclick():                 # Функция запуска поиска корней

    try:

        a = float(eval(ent_1.get()))      # Получение информации о введённых коэффициентах
        b = float(eval(ent_2.get()))
        c = float(eval(ent_3.get()))

        anslbl["text"] = ''                 # Очистка надписи с ответом
        anslbl["text"] = square(a, b, c)    # Наполнение надписи ответа

    except ValueError:              # Отлов ошибки неверного формата введённых данных

        anslbl["text"] = ''
        anslbl["text"] = 'Ошибка 1 \nНеверный формат введённых данных'

        return 'Ошибка 1 \nНеверный формат введённых данных'

    return


def on_close():             # Функция проверки желания закрытия окна

    if messagebox.askokcancel('Выход', 'Действительно хотите закрыть окно?'):

        mainwindow.destroy()


# Создание и настройка интерфейса
mainwindow = Tk()

# Основное окно
mainwindow.title('Калькулятор квадратных уравнений')
mainwindow.geometry('400x90')
mainwindow.resizable(width=False, height=False)
mainwindow.protocol('WM_DELETE_WINDOW', on_close)

# Главная надпись
mainlbl = Label(mainwindow, text='Введите коэффициенты квадратного уравнения вида ax² + bx + c = 0 ')
mainlbl.place(x=5, y=0)

# Надписи
lbl_1 = Label(mainwindow, text='x²+')
lbl_1.place(x=40, y=20)

lbl_2 = Label(mainwindow, text='x+')
lbl_2.place(x=105, y=20)

lbl_3 = Label(mainwindow, text='= 0')
lbl_3.place(x=160, y=20)

# Окна ввода
ent_1 = Entry(mainwindow, width=5)
ent_1.place(x=5, y=22)
ent_1.insert(0, '0')

ent_2 = Entry(mainwindow, width=5)
ent_2.place(x=70, y=22)
ent_2.insert(0, '0')

ent_3 = Entry(mainwindow, width=5)
ent_3.place(x=125, y=22)
ent_3.insert(0, '0')

# Кнопка
ansbtn = Button(mainwindow, text='Искать Ответ', command=btnclick)
ansbtn.place(x=310, y=50)

# Ответ
anslbl = Label(mainwindow)
anslbl.place(x=5, y=50)

# Поддержание интерфейса
mainwindow.mainloop()
