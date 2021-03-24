import time
class Solution:
    def countPrimes(self, n):
        ls=list(x for x in range(n+1))
        res=[]
#         从2开始筛选
        for i in range(2,10):
            for j in range(len(ls)):
                if ls[j]%i==0:
                    ls[j]=0

        for i in ls:
            if i!=0:
                res.append(i)

        print(res)


a=Solution()
b=a.countPrimes(500)
print(b)