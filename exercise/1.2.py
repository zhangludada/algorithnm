def same_word(s1, s2):
    d1 = {}
    d2 = {}
    for i in s1:
        d1[i] = d1.get(i, 0) + 1
    for i in s2:
        d2[i] = d2.get(i, 0) + 1
    return d1 == d2


a = 'eabcd'
b = 'cdbae'
print(same_word(a, b))
