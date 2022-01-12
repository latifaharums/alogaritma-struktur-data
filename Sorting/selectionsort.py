from random import randint
from time import time

def selection_sort(data):
    count = len(data)
    for k in range(count):
        j = count - k - 1
        big = 0
        for i in range(j + 1):
            if data[i] > data[big]:
                big = i
        data[j], data[big] = data[big], data[j]

data = [randint(0, 100) for _ in range(10_000)]
start = time()
selection_sort(data)
end = time()
print(end - start)