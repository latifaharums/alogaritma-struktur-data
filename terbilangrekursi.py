#versi inggris

import math

def terbilang(n):
    if n < 0:
        return 'minus ' + terbilang(-n)

    namas = ['zero', 'one', 'two', 'three', 'four', 'five',
        'six', 'seven', 'eight', 'nine']
    
    if n < 10:
        return namas[n]
    if n == 10:
        return 'ten'
    if n == 11:
        return 'eleven'
    if n == 12:
        return 'twelve'
    
    n_digit = len(str(n))
    pangkat = n_digit - 1
    if pangkat > 3:
        pangkat //= 3
        pangkat *= 3
    pembagi = int(math.pow(10, pangkat))
    muka = n // pembagi
    ekor = n % pembagi
    
    if pangkat == 1:
        akhiran = 'ty'
    elif pangkat == 2:
        akhiran = ' hundred'
    elif pangkat == 3:
        akhiran = ' thousand'
    elif pangkat == 6:
        akhiran = ' million'
    elif pangkat == 9:
        akhiran = ' billion'
    else:
        raise ValueError
    
    if pangkat == 1:
        namas[2] = 'twen'
        namas[3] = 'thir'
        namas[4] = 'for'
        namas[5] = 'fif'
        namas[8] = 'eigh'
        pemisah = '-'
    elif ekor < 100:
        pemisah = ' and '
    else:
        pemisah = ' '

    if n > 12 and n < 20:
        namas[4] = 'four'
        muka = ekor
        ekor = 0
        akhiran = 'teen'
        
    if muka < 10:
        hasil = namas[muka]
    else:
        hasil = terbilang(muka)
    hasil += akhiran
    if ekor > 0:
        hasil += pemisah + terbilang(ekor)
    return hasil

for i in range(1000, 1200):
    print(terbilang(i))