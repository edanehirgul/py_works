# enumerate() -> index,eleman adı çıktısını verir

markalar = ["opel", "bmw", "togg"]

index = 1
for marka in markalar:
    print(f"{index}-{marka}")
    index += 1

obj1 = enumerate(markalar)

print(type(obj1))
# <class 'enumerate'>

print(list(obj1))
# [(0, 'opel'), (1, 'bmw'), (2, 'togg')]

for index, marka in enumerate(markalar, 1):
    print(f"{index}-{marka}")
# 1-opel
# 2-bmw
# 3-togg

# ----zip method----
# birden fazla listeyi birleştirme

numara = [100, 200, 300]
ogrenci = ["Ali", "Ayşe", "Canan"]

print(list(zip(numara, ogrenci)))
# [(100, 'Ali'), (200, 'Ayşe'), (300, 'Canan')]


for no, isim in zip(numara, ogrenci):
    print(no, isim)

# 100 Ali
# 200 Ayşe
# 300 Canan
