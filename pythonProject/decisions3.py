def marks(kom):
    mark = []
    markn = []
    for i in dat:
        s = 0
        for j, v in enumerate(i):
            s += v * kom[j]
        mark.append(s)
    s2 = sum(mark)
    for i in mark:
        markn.append(i / s2)
    return markn


def compets(marks):
    compet = []
    competn = []
    for i in datt:
        s = 0
        for j, v in enumerate(i):
            s += v * marks[j]
        compet.append(s)
    s2 = sum(compet)
    for i in compet:
        competn.append(i / s2)
    return competn


dat = ((7, 8, 7, 6),
       (4, 3, 2, 4),
       (5, 6, 5, 4),
       (8, 9, 9, 8),
       (2, 4, 3, 2)
       )
com = []
datt = [[0 for _ in dat] for _ in dat[0]]
for i in dat[0]:
    com.append(1 / len(dat[0]))

for i in range(len(dat)):
    for j in range(len(dat[0])):
        datt[j][i] = dat[i][j]

while True:
    comold = com.copy()
    com = compets(marks(comold))
    marksold = marks(comold)
    marksnew = marks(com)
    if abs(max(marksold) - max(marksnew)) < 0.000001:
        break
print(marksold)
print(marksnew)
