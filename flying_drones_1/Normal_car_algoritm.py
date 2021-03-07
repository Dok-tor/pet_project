import networkx as nx
from tqdm import tqdm

f_in = open("sdc.txt")
f_out = open("SDC_normal.txt", "w")

row = "01"
day = 84400
eight = 28800
ten = 36000
seventeen = 61200
nineteen = 68400
while True:
    row = f_in.readline().strip().split()
    if not row:
        break
    if "=====" in row and (row[1] == '06' or row[1] == '07' or row[1] == '08' or row[1] == '09' or row[1] == '10'):
        # row[1] == '01' or row[1] == '02' or row[1] == '03' or row[1] == '04' or row[1] == '05' or
        G = nx.DiGraph()
        # print(G.edges())
        test_num = row[1]
        print(test_num, 'start')
        n, m = map(int, f_in.readline().strip().split())
        pathways = dict()
        orders = []

        for i in range(m):
            s = f_in.readline().strip().split()
            init = [int(s) for s in s]
            G.add_edge(init[0], init[1], weight=init[2])
            pathways[init[0], init[1]] = [int(s[i]) for i in range(2, 8)]
        k = 1
        q = int(f_in.readline().strip())
        print('q =', q)
        # print(G.edges())
        for i in range(q):
            s1 = f_in.readline().strip().replace(':', ' ').split()
            init1 = [int(s1[i]) for i in range(4)]
            orders.append(init1)

        f_out.write('===== ' + test_num + ' =====' + '\n')
        # nx.draw(G)   # тип по умолчанию spring_layout
        # nx.draw(G, pos=nx.spectral_layout(G), nodecolor='r', edge_color='b')
        pbar = tqdm(total=q)

        for i in range(q):
            start_time = orders[i][2] * 3600 + orders[i][3] * 60
            path = nx.shortest_path(G, orders[i][0], orders[i][1], weight='weight')
            full_time = start_time
            time = 0
            for j in range(1, len(path)):
                all_inf_path = pathways[path[j-1], path[j]]
                # print(all_inf_path)
                dist = all_inf_path[0]
                v0 = all_inf_path[1]
                v1 = all_inf_path[2]
                v2 = all_inf_path[3]
                v3 = all_inf_path[4]
                v4 = all_inf_path[5]
                while dist > 0:
                    if 0 <= full_time % day < eight and dist > 0:  # v0
                        inst_time = dist / v0
                        if (inst_time + full_time) % day > eight:
                            inst_time = eight - (full_time % day)

                        dist -= inst_time * v0
                        full_time += inst_time
                        time += inst_time
                    if eight <= full_time % day < ten and dist > 0:  # v1
                        inst_time = dist / v1
                        if (inst_time + full_time) % day > ten:
                            inst_time = ten - (full_time % day)

                        dist -= inst_time * v1
                        full_time += inst_time
                        time += inst_time
                    if ten <= full_time % day < seventeen and dist > 0:  # v2
                        inst_time = dist / v2
                        if (inst_time + full_time) % day > seventeen:
                            inst_time = seventeen - (full_time % day)

                        dist -= inst_time * v2
                        full_time += inst_time
                        time += inst_time
                    if seventeen <= full_time % day < nineteen and dist > 0:  # v3
                        inst_time = dist / v3
                        if (inst_time + full_time) % day > nineteen:
                            inst_time = nineteen - (full_time % day)

                        dist -= inst_time * v3
                        full_time += inst_time
                        time += inst_time
                    if nineteen <= full_time % day < day and dist > 0:  # v4
                        inst_time = dist / v1
                        if 0 <= (inst_time + full_time) % day < eight and dist > 0:
                            inst_time = day - inst_time
                            time += inst_time
                        dist -= inst_time * v4
                        full_time += inst_time
                        time += inst_time
                    # if dist != 0:
                    #     print("error")
                    #     print(dist)
            print(i, time)
            # f_out.write(str(nx.shortest_path_length(G, *orders[i], weight='weight')/10) + '\n')
            pbar.update(1)
            # print(nx.shortest_path_length(G, *orders[i], weight='weight')/10)
        pbar.close()
        pbar.leave = False
        print(test_num, 'done')
        print('------------')


f_in.close()
f_out.close()