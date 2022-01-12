def linear_search_all(item, data):
    result = []
    for index, element in enumerate(data):
        if element == item:
            result.append(index)
    return result

data = [8, 3, 4, 5, 1, 2, 7, 3, 6, 9, 0]
item = 3
index = linear_search_all(item, data)
print(f'Nilai {item} ditemukan di posisi {index}' if index else 'Tidak ketemu')