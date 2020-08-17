import random
import cal_time
n=100
ls = list(range(100000))
random.shuffle(ls)

@cal_time.run_time
def bucket_sort(ls,n):
    bucket=[[] for x in range(n)]
    for val in ls:
        i=val//(len(ls)//n)
        bucket[i].append(val)
        j=len(bucket[i])-1
        while j-1>=0 and bucket[i][j-1]>val:
            bucket[i][j]=bucket[i][j-1]
            j-=1
        bucket[i][j]=val
    print(bucket)


bucket_sort(ls,n)

