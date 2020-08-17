import random
from algorithmn.cal_time import *

ls=list(range(10000))
random.shuffle(ls)

def sift(ls,low,height):
    tmp=ls[low]
    i=low
    j=2*i+1
    while j<=height:
        if j+1<=height and ls[j+1]>ls[j]:
            j=j+1
        if tmp<ls[j]:
            ls[i]=ls[j]
            i=j
            j=2*i+1
        else:
            break
    ls[i]=tmp

@run_time
def heap_sort(ls):
    l=len(ls)-1
    for i in range((2*l-1)//2,-1,-1):
        sift(ls,i,l)
    for i in range(l,-1,-1):
        ls[0],ls[i]=ls[i],ls[0]
        sift(ls,0,i-1)


heap_sort(ls)
# print(ls)

