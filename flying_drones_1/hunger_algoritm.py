import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, sqrt

myList = []
fname = 'test_01.txt'
with open(fname) as f:
    for PointNumber, line in enumerate(f, 1):
        line = str(PointNumber) + " " + line
        line = line.rstrip('\n').strip().split()
        n_x_y = [int(line) for line in line]
        myList.append(n_x_y)

X = np.array(myList)

TotalPoints = len(X)
AllLengths = []     # Все варианты длин замкнутых путей
AllPaths = []       # Все варианты путей (номера точек)
RIB = []
s = []
for ib in np.arange(0, TotalPoints, 1):
    nnn = ib
    M = np.zeros([TotalPoints, TotalPoints])    # Матрица относительных расстояний между точками ("каждый с каждым")
    for i in np.arange(0, TotalPoints, 1):
        for j in np.arange(0, TotalPoints, 1):
            if i != j:
                M[i, j] = sqrt((X[i][1] - X[j][1]) ** 2 + (X[i][2] - X[j][2]) ** 2)     # Пифагора знают все!
            else:
                if i == 0 and j == 0:
                    M[i, j] = 0.1
                else:
                    M[i, j] = float('inf')
    way = []
    way.append(ib)
    for i in np.arange(1, TotalPoints, 1):
        s = []
        for j in np.arange(0, TotalPoints, 1):
            s.append(M[way[i - 1], j])
        way.append(s.index(min(s)))
        for j in np.arange(0, i, 1):
            M[way[i], way[j]] = float('inf')
    S = sum([sqrt((X[way[i]][1] - X[way[i + 1]][1]) ** 2 + (X[way[i]][2] - X[way[i + 1]][2]) ** 2) for i in np.arange(0, TotalPoints - 1, 1)]) \
        + sqrt((X[way[TotalPoints - 1]][1] - X[way[0]][1]) ** 2 + (X[way[TotalPoints - 1]][2] - X[way[0]][2]) ** 2)
    AllLengths.append(S)
    AllPaths.append(way)
    RIB.append(ib)
S = min(AllLengths)
way = AllPaths[AllLengths.index(min(AllLengths))]
print(way)
ib = RIB[AllLengths.index(min(AllLengths))]
ttt = AllLengths.index(min(AllLengths))
X1 = [X[way[i]][1] for i in np.arange(0, TotalPoints, 1)]
Y1 = [X[way[i]][2] for i in np.arange(0, TotalPoints, 1)]
plt.title('Общий путь-%s.Номер точки-%i.Всего точек -%i.\n Координаты X,Y заданы' % (round(S, 3), ib, TotalPoints), size=14)
plt.plot(X1, Y1, color='r', linestyle=' ', marker='o')
plt.plot(X1, Y1, color='b', linewidth=1)
for i in range(TotalPoints):
    plt.text(X1[i], Y1[i], way[i])
X2 = [X[way[TotalPoints - 1]][1], X[way[0]][1]]
Y2 = [X[way[TotalPoints - 1]][2], X[way[0]][2]]
plt.plot(X2, Y2, color='g', linewidth=2, linestyle='-', label='Путь от  последней \n к первой точке')
plt.legend(loc='best')
plt.grid(True)
plt.show()

Z = sqrt((X[way[TotalPoints - 1]][1] - X[way[0]][1]) ** 2 + (X[way[TotalPoints - 1]][2] - X[way[0]][2]) ** 2)
Y3 = [sqrt((X[way[i + 1]][1] - X[way[i]][1]) ** 2 + (X[way[i + 1]][2] - X[way[i]][2]) ** 2) for i in
      np.arange(0, TotalPoints - 1, 1)]
X3 = [i for i in np.arange(0, TotalPoints - 1, 1)]
plt.title('Пути от точки к точке')
plt.plot(X3, Y3, color='b', linestyle=' ', marker='o')
plt.plot(X3, Y3, color='r', linewidth=1, linestyle='-', label='Без учёта замыкающего пути - %s' % str(round(Z, 3)))
plt.legend(loc='best')
plt.grid(True)
plt.show()
