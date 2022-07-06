# Алгоритм бинарного поиска

from random import randint

num = []
for i in range(10):
    num.append(randint(1, 50))
num.sort()

print(num)

number = int(input())

def binary_search1(num, number):
    n = 0
    l_num = len(num)
    while n <= l_num:
        mid = (n + l_num) // 2
        if num[mid] == number:
            return mid
        elif num[mid] < number:
            n = mid + 1
        else:
            l_num = mid - 1

print((binary_search1(num, number)))



