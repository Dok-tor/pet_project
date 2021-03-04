class Square:
    def __init__(self, number):
        self.number = number
        self.points = []

    def insert(self, x, y, t, *reg):
        self.points.append(Point(x, y, t, *reg))
        # print('kek', self.points)


class Point:
    def __init__(self, x, y, t, *reg):
        self.x = int(x)
        self.y = int(y)
        self.t = int(t)
        self.regions = [int(i) for i in reg]


f_in = open('rovers.txt')
row = f_in.readline().strip().split()
test_num = row[1]

k, m, n = [int(i) for i in f_in.readline().strip().split()]
matrix = []
ln = 10000 // k
for i in range(1, k ** 2 + 1):
    matrix.append(Square(i))
for i in range(n):
    inf = [int(i) for i in f_in.readline().strip().split()]
    print(inf, k * ((inf[1] + 5000) // ln) + (inf[0] + 5000) // ln + 1)
    # matrix[k * ((inf[1] + 5000) // ln) + (inf[0] + 5000) // ln + 1].insert(*inf)
    for i in inf[3:]:
        print(i)
        matrix[i].insert(*inf)
print(matrix[46].points)
matrix.sort(reverse=True, key= lambda x: len(x.points))
print()
print(matrix[0].number)