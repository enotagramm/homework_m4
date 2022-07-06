# Алгоритм сортировки вставками

data = [9, 3, 56, 8, 22, 95, 433, 54, 33]
N = len(data)

def insertion_sort(data):
    for i in range(1, N):
        for j in range(i, 0, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break
    return data

print(insertion_sort(data))



