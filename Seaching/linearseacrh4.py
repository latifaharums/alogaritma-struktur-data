def linear_search_all(item, data, ordered=False):
    result = []
    for index, element in enumerate(data):
        print(index, element)
        if element == item:
            result.append(index)
        elif ordered and element > item:
            break
    return result

data = [0, 1, 2, 3, 3, 4, 6, 7, 8, 9]
item = 3
index = linear_search_all(item, data, ordered=True)
print(f'Nilai {item} ditemukan di posisi {index}' if index else 'Tidak ketemu')