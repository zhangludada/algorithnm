#二分查找

import numpy as np
ls=np.arange(25).reshape(5,5)
print(ls)

#m*n(column*row)的列表,n进制的index
#index 范围 [0:m*n-1]
def fd(num,ls,left,right):  #初始状态left=0,right=column*row-1
    column=len(ls)
    row=len(ls[0])
    #边界条件
    if num>ls[column-1][row-1] or num<ls[0][0]:
        print('不在范围内')
        return False

    while left<=right:
        mid=(left+right)//2
        m,n=mid//row,mid%row
        val=ls[m][n]
        if num<val:
            right=mid-1
        elif num>val:
            left=mid+1
        else:
            print('坐标[{},{}],数值{}'.format(m,n,ls[m][n]))
            break



init_right=len(ls)*len(ls[0])-1
result=fd(20,ls,0,init_right)







