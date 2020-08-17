import random
import cal_time

ls = list(range(0, 100000))
random.shuffle(ls)


@cal_time.run_time
def radix_sort(ls):
    l = len(str(max(ls)))
    for m in range(l):
        bucket = [[] for i in range(10)]
        for val in ls:
            i = (val // (10 ** m)) % 10
            bucket[i].append(val)
        ls.clear()
        for i in bucket:
            for j in i:
                ls.append(j)

radix_sort(ls)
