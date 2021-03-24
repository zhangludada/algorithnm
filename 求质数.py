import time
class Solution:
    def countPrimes(self, n):
        if n<2:
            return 0
        #生成长度为n的list
        isPrime=[1]*n
        isPrime[0],isPrime[1]=0,0

        for i in range(2,int(n**0.5)+1): #遍历2-根号n
            #如果i为质数，所有i的倍数为0
            if isPrime[i]:
                isPrime[i**2:n:i]=[0]*((n-1-i**2)//i+1)

        return sum(isPrime)

a=Solution()
b=a.countPrimes(49997999)
print(b)