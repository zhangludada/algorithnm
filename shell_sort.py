import random
import cal_time

ls = list(range(100000))
random.shuffle(ls)

@cal_time.run_time
def shell_sort(ls):
    d=len(ls)//2
    while d>=1:
        for i in range(d,len(ls)):
            tmp=ls[i]
            while i-d>=0 and tmp<ls[i-d]:
                ls[i]=ls[i-d]
                i-=d
            ls[i]=tmp
        d//=2

shell_sort(ls)
