import random
import cal_time

ls = list(range(100000))
random.shuffle(ls)

@cal_time.run_time
def count_sort(ls):
    count = [0 for i in range(100000)]
    for val in ls:
        count[val]+=1
    ls.clear()
    for i,v in enumerate(count):
        for n in range(v):
            ls.append(i)

@cal_time.run_time
def sys_sort(ls):
    ls.sort()

from copy import copy
ls1=ls.copy()

print('count_sort:',end='')
count_sort(ls)
print('sys_sort:',end='')
sys_sort(ls1)

