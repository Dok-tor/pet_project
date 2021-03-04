import random


f_out = open("rovers_out.txt", "w")
f1 = list(random.randint(1, 100) for i in range(1))
f2 = list(random.randint(1, 10000) for j in range(10))
f3 = list(random.randint(1, 100) for k in range(1000))
f4 = list(random.randint(1, 10000) for l in range(1000))
f5 = list(random.randint(1, 100) for m in range(2000))
f6 = list(random.randint(1, 100) for n in range(20000))
f7 = list(random.randint(1, 10000) for o in range(20000))
f8 = list(random.randint(1, 10000) for p in range(20000))
f9 = list(random.randint(1, 100) for q in range(10000))
f10 = list(random.randint(1, 100) for r in range(100000))
f_out.write("==== 01 ====" + "\n")

for i in f1:
    f_out.write(str(i))

f_out.write("\n")
f_out.write("==== 02 ====" + "\n")

for i in f2:
    f_out.write(str(i) + " ")

f_out.write("\n")
f_out.write("==== 03 ====" + "\n")

for i in f3:
    f_out.write(str(i) + " ")

f_out.write("\n")
f_out.write("==== 04 ====" + "\n")

for i in f4:
    f_out.write(str(i) + " ")

f_out.write("\n")
f_out.write("==== 05 ====" + "\n")

for i in f5:
    f_out.write(str(i) + " ")

f_out.write("\n")
f_out.write("==== 06 ====" + "\n")

for i in f6:
    f_out.write(str(i) + " ")

f_out.write("\n")
f_out.write("==== 07 ====" + "\n")

for i in f7:
    f_out.write(str(i) + " ")

f_out.write("\n")
f_out.write("==== 08 ====" + "\n")

for i in f8:
    f_out.write(str(i) + " ")

f_out.write("\n")
f_out.write("==== 09 ====" + "\n")

for i in f9:
    f_out.write(str(i) + " ")

f_out.write("\n")
f_out.write("==== 10 ====" + "\n")

for i in f10:
    f_out.write(str(i) + " ")

f_out.close()