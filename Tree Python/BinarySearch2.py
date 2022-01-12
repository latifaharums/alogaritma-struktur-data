def binary_search(item, data):
    left = 0
    right = len(data) - 1
    while left <= right:
        print('.')
        if data[left] == item:
            return left
        if data[right] == item:
            return right
        mid = (left + right) // 2
        if data[mid] < item:
            left += 1
        elif data[mid] > item:
            right -= 1
        else:
            return mid

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
item = 8
index = binary_search(item, data)
print(f'Nilai {item} ditemukan di posisi {index}'
    if index is not None else 'Tidak ketemu')