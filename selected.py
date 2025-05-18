import timeit
from random import randint

#сортировка выбором

def selected(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr_10 = []
for i in range(10):
    arr_10.append(randint(1, 100))

arr_100 = []
for i in range(100):
    arr_100.append(randint(1, 1000))

arr_50 = []
for i in range(50):
    arr_50.append(randint(1, 1000))

arr = arr_50

# arr = [361, 455, 963, 349, 99, 229, 916, 490, 748, 605, 977, 471, 289, 422, 274, 817, 291, 853, 151, 605, 741, 901, 638, 347, 349, 677, 87, 440, 313, 644, 926, 495, 898, 46, 440, 715, 14, 989, 944, 112, 991, 896, 286, 645, 210, 286, 718, 713, 699, 232, 496, 871, 734, 155, 991, 76, 112, 641, 185, 923, 63, 123, 240, 561, 29, 594, 161, 779, 899, 675, 932, 88, 390, 863, 827, 701, 36, 793, 938, 153, 934, 400, 6, 121, 705, 367, 360, 647, 253, 976, 452, 747, 384, 24, 942, 285, 300, 885, 267, 761]

print(selected(arr))



print(timeit.timeit(stmt = "selected(arr)", globals=globals(), number = 1000))

# время для 10 элементов
# пузырь - 0,0018
# выбор - 0,0017

# время для 50 элементов
# пузырь - 0,034
# выбор - 0,028

# время для 100 элементов
# пузырь - 0,12
# выбор - 0,10




