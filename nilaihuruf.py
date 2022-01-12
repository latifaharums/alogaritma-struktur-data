def nilai(huruf):
    if huruf == 'A':
        return 4
    elif huruf == 'B':
        return 3
    elif huruf == 'C':
        return 2
    elif huruf == 'D':
        return 1
    else:
        return 0

def nilai1(huruf):
    if huruf == 'A':
        return 4
    if huruf == 'B':
        return 3
    if huruf == 'C':
        return 2
    if huruf == 'D':
        return 1
    return 0

def nilai2(huruf):
    return ( 4 if huruf == 'A'
        else 3 if huruf == 'B'
        else 2 if huruf == 'C'
        else 1 if huruf == 'D'
        else 0 )

def nilai3(huruf):
    return {
        'A': 4,
        'B': 3,
        'C': 2,
        'D': 1,
    }.get(huruf, 0)

print(nilai('B'))
print(nilai1('B'))
print(nilai2('B'))
print(nilai3('B'))