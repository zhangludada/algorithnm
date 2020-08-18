#插入排序
import random

def insert_sort(ls,n):
    sort_ls=[]
    for i,v in enumerate(ls):
        if v<=n:
            sort_ls.append([v,i])
            #插入排序
            j=len(sort_ls)-1
            while j-1>=0 and v<sort_ls[j-1][0]:
                sort_ls[j]=sort_ls[j-1]
                j-=1
            sort_ls[j]=[v,i]
    print('排序后的有效列表:',sort_ls)

    #if a+b=n;a=ls[i];b=n-1  二分查找b
    l=len(sort_ls)-1
    if l<1:
        print('查无此数')
        return None
    for i in range(l+1):
        a=sort_ls[i][0]
        b=n-a
        if b!=a:
            #二分查找b
            left = 0
            right = len(sort_ls)-1
            while left <= right:
                mid = (left + right) // 2
                val=sort_ls[mid][0]
                if b<val:
                    right = mid - 1
                elif b > val:
                    left = mid + 1
                else:
                    print(sort_ls[i],sort_ls[mid])
                    return None
            print('查无此数2')








def main():
    ls=list(range(10))
    random.shuffle(ls)
    n=random.randint(0,9)
    print('源数据列表:{};求和总数{}'.format(ls,n))
    insert_sort(ls,n)

for i in range(1000):
    main()
    print('#'*20)






