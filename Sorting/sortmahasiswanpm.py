#mengurutkan mahasiswa berdasarkan NPM:

class Mahasiswa:
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
    def __repr__(self):
        return '{} {}'.format(self.npm, self.nama)

mhs = [
    Mahasiswa('202103011', 'Wiro Sableng'),
    Mahasiswa('202103001', 'Sinto Gendeng'),
    Mahasiswa('202103006', 'Bill Gates'),
    Mahasiswa('202103004', 'Steve No Job'),
]

'''
def sorted_by_npm(e):
    return e.npm

mhs.sort(key=sorted_by_npm)
'''
mhs.sort(key=lambda e: e.npm)
print(mhs)