import math


def get_key(diction: dict, x: int, y: int):
    """ Возвращает ключ по значению из словаря """
    for key, item in diction.items():
        if item == [x, y]:
            return key


def distance(x0: int, y0: int, x1: int, y1: int):
    """ Расчитывает линейное расстояние между точками """
    return abs(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** (1 / 2))


def count_time(dist):
    """ Считает общее время требуемое на преодоление расстояние и разгрузку """
    return math.ceil(dist/100) + 30


def time_to_home(x: int, y: int):
    """ Считает время полёта из координат (x, y) до точки (0, 0) """
    dist = distance(x, y, 0, 0)
    time = count_time(dist) - 30
    return time


def next_point(coord: dict, x: int, y: int):  # Вызывает distance() и get_key()
    """ Находит в словаре coord следующую точку для дрона.
    Возвращает ее номер, координаты и расстояние до неё """
    min_distance = 40000
    for x_next, y_next in coord.values():
        dist = distance(x, y, x_next, y_next)
        if dist < min_distance:
            min_distance = dist
            fin_cords = (x_next, y_next)
    return get_key(coord, *fin_cords), fin_cords, min_distance


def main():
    """ Основная функция.
        Открывает файл f_in(txt) на чтение и f_out(txt) на запись.
    """

    f_in = open("drones.txt")
    f_out = open("output.txt", "w")

    while True:
        row = f_in.readline().strip().split()
        if not row:
            break
        test_num = row[1]
        m, n = map(int, f_in.readline().strip().split())
        coordinates = dict()

        for i in range(n):
            s = f_in.readline().strip().split()
            coordinates[i+1] = [int(s) for s in s]
        g = 0
        f_out.write("=" * 4 + test_num + "=" * 4 + "\n")
        print(test_num)
        for i in range(m):
            f_out.write(str(i+1) + " ")
            if coordinates:
                arr_of_points = []
                time = 720
                point, cords, dist = next_point(coordinates, 0, 0)
                inst_time = count_time(dist)
                out_time = count_time(dist) + time_to_home(*cords)
                while out_time < time:
                    arr_of_points.append(str(point))
                    g += 1
                    time -= inst_time
                    coordinates.pop(point)
                    if not coordinates:
                        break
                    next_cords = cords
                    point, cords, dist = next_point(coordinates, *next_cords)
                    out_time = count_time(dist) + time_to_home(*cords)
                    inst_time = count_time(dist)
                f_out.write(str(len(arr_of_points)) + " ")
                for j in arr_of_points:
                    f_out.write(j + " ")
                f_out.write("\n")
            else:
                f_out.write("0" + "\n")
        print(g)
    f_in.close()
    f_out.close()


main()

