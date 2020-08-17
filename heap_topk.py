import random

ls = list(range(1000))
random.shuffle(ls)


# 小根堆
def sift(ls, low, height):
    tmp = ls[low]
    i = low
    j = 2 * i + 1
    while j <= height:
        if j + 1 <= height and ls[j + 1] < ls[j]:
            j = j + 1
        if tmp > ls[j]:
            ls[j], ls[i] = tmp, ls[j]
            i = j
            j = i * 2 + 1
        else:
            break
    ls[i] = tmp


def topk_sort(ls, k):
    heap = ls[0:k]
    n = len(heap)
    # 1，建立heap的小根堆
    for i in range((k - 2) // 2, -1, -1):
        sift(ls, i, k - 1)
    # 2.从剩余列表中取数加入heap的堆顶，并建堆
    for i in range(k, len(ls)):
        if ls[i] > heap[0]:
            heap[0] = ls[i]
            sift(heap, 0, n - 1)
    # 3.heap最终建堆完成，重新排列出数
    for i in range(n - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap


a = topk_sort(ls, 10)
print(a)
