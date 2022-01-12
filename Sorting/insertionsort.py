def insertion_sort(data):
    count = len(data)
    for j in range(1, count):
        for i in range(j, 0, -1):
            if data[i] < data[i - 1]:
                data[i], data[i - 1] = data[i - 1], data[i]
            else:
                break

data = [7, 5, 2, 8, 9, 1, 0, 5, 3, 4]
insertion_sort(data)
print(data)