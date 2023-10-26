matrix = [[14, 25, 24, 16],
          [20, 18, 19, 21],
          [13, 15, 34, 17],
          [19, 22, 25, 15],
          [26, 14, 22, 17]
          ]

p = [0.4, 0.2, 0.3, 0.1]


def laplas(m):
    s = []
    for i in m:
        s.append(sum(i) / len(i))
    return s.index(max(s)) + 1


def gurvic(m, alpha):
    s = []
    for i in m:
        s.append(max(i) * alpha + min(i) * (1 - alpha))
    return s.index(max(s)) + 1


def vald(m):
    s = []
    for i in m:
        s.append(min(i))
    return s.index(max(s)) + 1


def maxopt(m):
    s = []
    for i in m:
        s.append(max(i))
    return s.index(max(s)) + 1


def bayes(m):
    s = []
    for i in m:
        sm = 0
        for j in range(len(i)):
            sm += i[j] * p[j]
        s.append(sm)
    return s.index(max(s)) + 1


def savage(m):
    s = []
    tran = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    risk = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    riskt = [[0 for _ in range(len(risk))] for _ in range(len(risk[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            tran[j][i] = m[i][j]
    for i in range(len(tran)):
        for j in range(len(tran[0])):
            risk[i][j] = max(tran[i]) - tran[i][j]
    for i in range(len(risk)):
        for j in range(len(risk[0])):
            riskt[j][i] = risk[i][j]
    for i in riskt:
        s.append(max(i))
    return s.index(min(s)) + 1


alpha = float(input('Введите альфа '))

dic = {'laplas': f'Лучшая альтернатива {laplas(matrix)}',
       'bayes': f'Лучшая альтернатива {bayes(matrix)}',
       'vald': f'Лучшая альтернатива {vald(matrix)}',
       'maxopt': f'Лучшая альтернатива {maxopt(matrix)}',
       'savage': f'Лучшая альтернатива {savage(matrix)}',
       'gurvic': f'Лучшая альтернатива {gurvic(matrix, alpha)}'
       }
for k, v in dic.items():
    print('По критерию', k, v)
print(dic)
