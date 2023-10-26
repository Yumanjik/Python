import math
import matplotlib.pyplot as plt

n = int(input('Введите размер матрицы '))
matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = 1
        elif i < j:
            matrix[i][j] = int(input(f'Введите элемент {i + 1} {j + 1} '))
        else:
            matrix[i][j] = 1 / matrix[j][i]

sv = []
alt = ['A' + str(i + 1) for i in range(n)]

for i in matrix:
    sv.append(math.prod(i) ** (1 / len(i)))
s = sum(sv)

for i in range(len(sv)):
    sv[i] /= s
print(sv)
print(f'Выбираем альтернативу №{sv.index(max(sv)) + 1}')
print(matrix)
plt.bar(list(alt), sv)
plt.title('Оценки альтернатив по МАИ')
plt.xlabel('Альтернативы')
plt.ylabel('Нормированные оценки')
plt.legend()
plt.show()
