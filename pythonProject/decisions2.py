def normmin(x, mx, mn):
    a = (mx - x) / (mx - mn)
    return a


def normmax(x, mx, mn):
    a = (x - mn) / (mx - mn)
    return a


def main():
    a = {
        'a1': [5, 4.2, 5, 6, 10],
        'a2': [9, 6, 8.5, 2, 10],
        'a3': [3, 7, 5, 4, 10],
        'a4': [7, 3, 6.6, 5, 11],
        # 'a5': [5, 5, 16, 10]
    }

    w = [7, 8, 6, 5, 15]
    factnorm = [1, 0, 0, 1, 0]
    b = []
    s = []
    keys = []

    for k, z in a.items():
        b.append(z)
        keys.append(k)

    c = [[0 for _ in range(len(b))] for _ in range(len(b[0]))]
    d = [[0 for _ in range(len(b))] for _ in range(len(b[0]))]

    for i in range(len(b)):
        for j in range(len(b[0])):
            c[j][i] = b[i][j]

    for i in range(len(c)):
        for j in range(len(c[0])):
            if factnorm[i] == 1:
                d[i][j] = normmax(c[i][j], max(c[i]), min(c[i]))
            else:
                d[i][j] = normmin(c[i][j], max(c[i]), min(c[i]))

    for i in range(len(d[0])):
        sm = 0
        for j in range(len(d)):
            sm += d[j][i] * w[j]
        s.append(sm)

    print(f"Лучшая альтернатива это {keys[s.index(max(s))]}")


main()
