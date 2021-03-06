import random
from tqdm import tqdm

f_in = open("sdc.txt")
f_out = open("generate_paths.txt", "w")

while True:
    row = f_in.readline().strip().split()
    if not row:
        break
    test_num = row[1]
    print(test_num, 'start')
    n, m = map(int, f_in.readline().strip().split())

    for i in range(m):
        s = f_in.readline().strip().split()

    q = int(f_in.readline().strip())
    print('q =', q)

    for i in range(q):
        s1 = f_in.readline().strip().split()

    f_out.write('===== ' + test_num + ' =====' + '\n')
    pbar = tqdm(total=q)
    for i in range(q):
        f_out.write(str(random.randint(100, 100000)) + '\n')
        pbar.update(1)
    pbar.close()
    pbar.leave = False
    print(test_num, 'done')
    print('------------')


f_in.close()
f_out.close()