#SOAL 1 BAHASA KHAYAL, BAHASA WAJA
#NAMA : LATIFAH ARUM SULISTYANINGSIH
#NPM  : 202103008

def terbilang(n):
    if n < 0:
        raise ValueError
    if n < 10:
        return [
            'elun', 'jisi', 'rolo',
            'letu', 'tatap', 'mila',
            'emen', 'tipu', 'lowu', 'ngasa'
        ][n]


    if n >10 and n < 20:
        head = n // 10 
        tail = n %10
        return terbilang (tail) + 'was' 

    if n > 20 and n < 30:
        head = n // 10 
        tail = n %10
        return terbilang (tail) + 'kilur' 

    if n < 100:
        head = n // 10
        tail = n % 10
        return terbilang(head) + 'lupuh' + (
            f' {terbilang(tail)}' if tail else ''
        )
    if n < 1000:
        head = n // 100
        tail = n % 100
        return terbilang(head) + 'tasus' + (
            f' {terbilang(tail)}' if tail else ''
        )

    raise ValueError
    

print(terbilang(1))
print(terbilang(10))
print(terbilang(12))
print(terbilang(20))
print(terbilang(25))
print(terbilang(40))
print(terbilang(100))
print(terbilang(101))
print(terbilang(999))