def main():
    """ Функция без параметров.
        Открывает файл, читает первый блок.
        Выводит:
            m(int) - количество дронов
            n(int) - количество точек
            coordinates(dict) - словарь из индекса точки в качестве ключа,
                                и кортежа координат в качестве значения
            test_num(str) - номер теста
    """

    f = open("testDrones.txt")

    # for j in range(10):
    test_num = f.readline().strip().split()[1]
    m, n = map(int, f.readline().strip().split())
    coordinates = dict()

    for i in range(n):
        s = f.readline().strip().split()
        coordinates[i+1] = [int(s) for s in s]
    return m, n, coordinates, test_num


m, n, slov, num = main()

print(slov)
help(main)

