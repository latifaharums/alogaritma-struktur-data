# rekursif

import math

def terbilang(n):
    if n < 0:
        return 'minus ' + terbilang(-n)

    namas = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima',
        'enam', 'tujuh', 'delapan', 'sembilan']
    
    if n < 10:
        return namas[n]
    
    n_digit = len(str(n))
    pangkat = n_digit - 1
    if pangkat > 3:
        pangkat //= 3
        pangkat *= 3
    pembagi = int(math.pow(10, pangkat))
    muka = n // pembagi
    ekor = n % pembagi
    
    if pangkat == 1:
        akhiran = 'puluh'
    elif pangkat == 2:
        akhiran = 'ratus'
    elif pangkat == 3:
        akhiran = 'ribu'
    elif pangkat == 6:
        akhiran = 'juta'
    elif pangkat == 9:
        akhiran = 'milyar'
    else:
        raise ValueError
    
    if n > 10 and n < 20:
        muka = ekor
        ekor = 0
        akhiran = 'belas'
        
    if muka == 1 and pangkat <= 3:
        namas[1] = 'se'
        pemisah = ''
    else:
        pemisah = ' '
    
    if muka < 10:
        hasil = namas[muka]
    else:
        hasil = terbilang(muka)
    hasil += pemisah + akhiran
    if ekor > 0:
        hasil += ' ' + terbilang(ekor)
    return hasil

for i in range(0, 200):
    print(terbilang(i))