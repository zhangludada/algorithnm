import random
import cal_time

ls=list(range(10000))
random.shuffle(ls)

@cal_time.run_time
def insert_sort(ls):
    for i in range(1,len(ls)):
        tmp=ls[i]
        for j in range(i+1):
            if tmp<ls[j]:
                ls.insert(j,ls.pop(i))
                break


insert_sort(ls)
