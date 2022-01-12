#mengurutkan jenis kelamin dan nama menggunakan key

class Mahasiswa:
  def __init__(self, npm, nama, jk):
    self.npm = npm
    self.nama = nama
    self.jk = jk
  def __repr__(self):
    return f'Mahasiswa dgn NPM {self.npm} dan nama {self.nama}'

mhs = [
  Mahasiswa('21031', 'Barry Allen', 'L'),
  Mahasiswa('21020', 'Mary Jane', 'P'),
  Mahasiswa('21030', 'Bill Gates', 'L'),
  Mahasiswa('21032', 'Astuti', 'P'),
]

def urut_jk_dan_nama(m):
  return m.jk, m.nama

mhs.sort(key=urut_jk_dan_nama)
# mhs.sort(key=lambda m: m.jk, m.nama)

for m in mhs:
  print(m)