import random
import cal_time

ls=list(range(10000))
random.shuffle(ls)

@cal_time.run_time
def insert_sort(ls):
    for i in range(1,len(ls)):
        tmp=ls[i]
        while i-1>=0 and ls[i-1]>tmp:
            ls[i]=ls[i-1]
            i-=1
        ls[i]=tmp



insert_sort(ls)



