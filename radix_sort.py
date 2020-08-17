import random
import cal_time

ls = list(range(100))
random.shuffle(ls)

def radix_sort(ls):
    bucket=[[] for i in range(10)]
    l=len(str(ls))
    for m in range(l):
        for val in ls:
            i=val//(10**m)%10
            print(i)
    #         bucket[i].append(val)
    #         j = len(bucket[i]) - 1
    #         while j - 1 >= 0 and bucket[i][j - 1] > val:
    #             bucket[i][j] = bucket[i][j - 1]
    #             j -= 1
    #         bucket[i][j] = val
    # print(bucket)

radix_sort(ls)