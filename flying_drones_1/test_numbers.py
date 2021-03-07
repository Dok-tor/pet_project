f_in = open("sdc.txt")
max_nu = 0
while True:
    s = f_in.readline().strip().replace(':', ' ').split()
    if not s:
        break
    if "=====" not in s:
        init = [int(s) for s in s]
        for i in init:
            if i > max_nu and i != 733846 and i != 264346:
                max_nu = i
    else:
        num = s[1]
        if num == '03':
            k = 1
f_in.close()
print(max_nu)
