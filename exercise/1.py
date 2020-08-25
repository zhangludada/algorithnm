def same_word(s1, s2):
    count1 = [0 for x in range(26)]
    count2 = [0 for x in range(26)]
    for i in s1:
        id = ord(i) - ord('a')
        count1[id] += 1
    for i in s2:
        id = ord(i) - ord('a')
        count2[id] += 1
    if count1 == count2:
        return True
    else:
        return False


a = 'eabcd'
b = 'cdbae'
print(same_word(a, b))
