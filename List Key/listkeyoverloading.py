class Mahasiswa:
  def __init__(self, npm, nama, jk):
    self.npm = npm
    self.nama = nama
    self.jk = jk
  def __repr__(self):
    return f'Mahasiswa dgn NPM {self.npm} dan nama {self.nama}'
  def __lt__(self, other):
    return self.npm < other.npm

mhs = [
  Mahasiswa('21031', 'Andi Lau', 'L'),
  Mahasiswa('21030', 'Bill Gates', 'L'),
  Mahasiswa('21032', 'Diana Prince', 'P'),
  Mahasiswa('21020', 'Mary Jane', 'P'),
]

mhs.sort()

for m in mhs:
  print(m)
