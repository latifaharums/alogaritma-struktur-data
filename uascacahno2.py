#SOAL 2 MENAMBAHKAN 2 FUNGSI AGAR TIDAK ERROR
#NAMA : LATIFAH ARUM SULISTYANINGSIH
#NPM  : 202103008


class Deret:
    def __init__(self, nama, data):
        self.nama = nama
        self.data = data
    def __repr__(self):
        return self.nama

deretan = [
    Deret('Genap', [2 * x for x in range(8)]),
    Deret('Ganjil', [1, 3, 5, 7, 9, 11, 13]),
    Deret('Prima', [2, 3, 5, 7, 11, 13, 17]),
    Deret('Kelipatan 3', [3, 6, 9, 12, 15]),
    Deret('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13]),
    Deret('Kelipatan 7', [7, 14, 21, 28]),
    Deret('Puluhan', [10, 20, 30]),
    Deret('Ratusan', [100, 200]),
]

def cacah_elemen(self):
    urutan = len(self.data)
    return urutan
def total_elemen(self):
    total = sum(self.data)
    return total

deretan.sort(key=cacah_elemen)
print(deretan)
deretan.sort(key=total_elemen)
print(deretan)
