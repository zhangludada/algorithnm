import numpy as np


def check(s1, s2):
    m = len(s1)
    n = len(s2)
    ls = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    result = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    print(ls)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                ls[i][j] = ls[i - 1][j - 1] + 1
                result[i][j] = 1  # 左上
            # else:
            #     ls[i][j]=max(ls[i-1][j],ls[i][j-1])
            elif ls[i - 1][j] > ls[i][j - 1]:
                ls[i][j] = ls[i - 1][j]
                result[i][j] = 2  # 上方
            else:
                ls[i][j] = ls[i][j - 1]
                result[i][j] = 3  # 左方
    return result


a = 'bdcaba'
b = 'abcbdab'

c = check(a, b)


def track_back(a, b):
    ls = check(a, b)
    i = len(a)
    j = len(b)
    res = []
    while i > 0 and j > 0:
        if ls[i][j] == 1:
            res.append(a[i - 1])
            i -= 1
            j -= 1
        elif ls[i][j] == 2:
            i -= 1
        else:
            j -= 1
    res.reverse()
    return res


print(track_back(a, b))
