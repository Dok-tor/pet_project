import networkx as nx
from tqdm import tqdm
# G.add_edge(1, 10, weight=10)

f_in = open("sdc.txt")
f_out = open("SDC_OUT_v2.txt", "w")

row = "01"

while True:
    row = f_in.readline().strip().split()
    if not row:
        break
    if "=====" in row and (row[1] == '09'):
        # row[1] == '01' or row[1] == '02' or row[1] == '03' or row[1] == '04' or
        G = nx.DiGraph()
        # print(G.edges())
        test_num = row[1]
        print(test_num, 'start')
        n, m = map(int, f_in.readline().strip().split())

        orders = []

        for i in range(m):
            s = f_in.readline().strip().split()
            init = [int(s) for s in s]
            G.add_edge(init[0], init[1], weight=init[2])
        k = 1
        q = int(f_in.readline().strip())
        print('q =', q)
        # print(G.edges())

        for i in range(q):
            s1 = f_in.readline().strip().split()
            init1 = [int(s1[i]) for i in range(2)]
            orders.append(init1)

        f_out.write('===== ' + test_num + ' =====' + '\n')
        # nx.draw(G)   # тип по умолчанию spring_layout
        # nx.draw(G, pos=nx.spectral_layout(G), nodecolor='r', edge_color='b')
        pbar = tqdm(total=q)

        for i in range(len(orders)):
            # print(orders[i])
            f_out.write(str(nx.shortest_path_length(G, *orders[i], weight='weight')/10) + '\n')
            pbar.update(1)
            # print(nx.shortest_path_length(G, *orders[i], weight='weight')/10)
        pbar.close()
        pbar.leave = False
        print(test_num, 'done')
        print('------------')


f_in.close()
f_out.close()