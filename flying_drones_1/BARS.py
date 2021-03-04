import time
from tqdm import tqdm
q = 1000
mylist = [1,2,3,4,5,6,7,8]
pbar = tqdm(total=q)

for i in range(100):
    pbar.update(10)
pbar.close()