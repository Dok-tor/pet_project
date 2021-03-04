from scipy.spatial import distance
import time


def get_key(diction: dict, x: int, y: int):
    """ Возвращает ключ по значению из словаря """
    for key, item in diction.items():
        if item == [x, y]:
            return key


def distance1(x0: int, y0: int, x1: int, y1: int):
    """ Расчитывает линейное расстояние между точками """
    return abs(((int(x1) - int(x0)) ** 2 + (int(y1) - int(y0)) ** 2) ** (1 / 2))


def next_point(coord: dict, x: int, y: int):  # Вызывает distance() и get_key()
    """ Находит в словаре coord следующую точку для дрона.
    Возвращает ее номер, координаты и расстояние до неё """
    min_distance = 40000
    for key, items in coord.items():
        dist = distance1(x, y, *items)
        if dist < min_distance:
            min_distance = dist
            fin_cords = items
            fin_point = key
    return fin_point, fin_cords, min_distance



f_in = open("9test.txt")

row = f_in.readline().strip().split()
test_num = row[1]
if test_num == '09':
    m, n = map(int, f_in.readline().strip().split())
    coordinates = dict()
    coord = []
    for i in range(n):
        s = f_in.readline().strip().split()
        coordinates[i+1] = [str(s) for s in s]
    g = 0


def closest_node(node, nodes):
    closest_index = distance.cdist([node], nodes).argmin()
    return nodes[closest_index]


start = time.time()
a = list(coordinates.values())
some_pt = (0, 0)
first_count = get_key(coordinates, *closest_node(some_pt, a))
end = time.time()
print("первый тест", end - start, first_count)

start = time.time()
second_count = list(next_point(coordinates, *some_pt))
end = time.time()
print("второй тест", end - start, second_count)
