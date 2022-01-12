def linear_search(item, data, ordered=False):
    for index, element in enumerate(data):
        print(index, element)
        if element == item:
            return index
        elif ordered and element > item:
            break

data = [0, 1, 2, 3, 4, 6, 7, 8, 9]
item = 5
index = linear_search(item, data, ordered=True)
print(f'Nilai {item} ditemukan di posisi {index}' if index else 'Tidak ketemu')