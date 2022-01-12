#mengurutkan secara berkelompok dr digit yg lbh banyak:

from random import randint

def sortfunc(e):
    return -len(str(e)), e

data = [randint(0, 9) for _ in range(5)] +\
       [randint(10, 99) for _ in range(5)] +\
       [randint(100, 999) for _ in range(5)]
data.sort(key=sortfunc)

print(data)