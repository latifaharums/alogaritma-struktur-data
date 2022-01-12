def linear_search(item, data):
    for index, element in enumerate(data):
        if element == item:
            return index

data = [8, 3, 4, 5, 1, 2, 7, 3, 6, 9, 0]
item = 3
index = linear_search(item, data)
print(f'Nilai {item} ditemukan di posisi {index}' if index else 'Tidak ketemu')