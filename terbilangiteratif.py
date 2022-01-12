# iteratif

import math

def terbilang(n):
    hasil = ''
    
    namas = ('nol', 'satu', 'dua', 'tiga', 'empat', 'lima',
        'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh',
        'sebelas')

    if n < 0:
        hasil += 'minus'
        n = -n

    if n < 12:
        if hasil:
            hasil += ' '
        hasil += namas[n]
        return hasil

    akhirans = ('', 'ribu', 'juta', 'milyar', 'triliun')
    n_digit = len(str(n))
    n_grup = math.ceil(n_digit / 3)
    
    sisa = n
    for g in range(n_grup, 0, -1):
        pembagi = int(math.pow(1000, g - 1))
        grup = sisa // pembagi
        sisa %= pembagi
        if grup == 0:
            continue
        akhiran = akhirans[g - 1]
        if grup == 1 and akhiran == 'ribu':
            hasil += 'seribu'
            continue
        muka = grup // 100
        ekor = grup % 100
        hasil_grup = ''
        if muka > 1:
            hasil_grup += namas[muka] + ' ratus'
        elif muka == 1:
            hasil_grup += 'seratus'
        if ekor > 0:
            if muka > 0:
                hasil_grup += ' '
            if ekor < 12:
                hasil_grup += namas[ekor]
            else:
                puluhan = ekor // 10
                satuan = ekor % 10
                if ekor >= 12 and ekor < 20:
                    hasil_grup += namas[satuan] + ' belas'
                else:
                    hasil_grup += namas[puluhan] + ' puluh'
                    if satuan > 0:
                        hasil_grup += ' ' + namas[satuan]
        hasil_grup += ' ' + akhiran
        
        if hasil:
            hasil += ' '
        hasil += hasil_grup

    return hasil

for i in range(0, 101):
    print(terbilang(i))