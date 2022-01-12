def bubble_sort(data):
    count = len(data)
    for i in range(count - 1):
        for j in range(count - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

nilai = [2, 5, 2, 5, 6, 7, 8, 1, 0, 4, 5]
bubble_sort(nilai)
print(nilai)