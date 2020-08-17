import random
from algorithmn.cal_time import *

ls = list(range(10000))
random.shuffle(ls)


def p(ls, left, right):
    tmp = ls[left]
    while left < right:
        if right > left and ls[right] > tmp:
            right -= 1
        ls[left], ls[right] = ls[right], ls[left]
        if left < right and ls[left] < tmp:
            left += 1
        ls[left], ls[right] = ls[right], ls[left]
    return left


def quick_sort(ls, left, right):
    if left < right:
        mid = p(ls, left, right)
        quick_sort(ls, left, mid - 1)
        quick_sort(ls, mid + 1, right)


@run_time
def main():
    quick_sort(ls, 0, len(ls) - 1)


main()
