#  ---- LISTS ----

kurum = "BTK Akademi" .split()  # <class 'list'>

print(type(kurum))
print(kurum)

sayılar = [1, 2, 3, 4, 5]

print(type(sayılar))  # <class 'int'>
print(type(sayılar[0]))

ogrenci = ["Eda", "Gul", 90, 100, 80]

print(ogrenci[0] + " " + ogrenci[1])

ortalama = (ogrenci[2] + ogrenci[3] + ogrenci[4]) / 3

print(ortalama)

ogrenciler = ["Eda", "Gul", 90, 100, 80], ["Emre", "Kosova", 40, 80, 87]

print(ogrenciler[0])  # ['Eda', 'Gul', 90, 100, 80]
print(ogrenciler[1])  # ["Emre", "Kosova", 40, 80, 87]

print((ogrenciler[0][0]).upper())  # EDA

print("Eda" in ogrenciler[0])  # ogrenciler de Eda var mı ? -> True
# -> False çünkü liste liste arar value olarak değil
print("Eda" in ogrenciler)


for eleman in ogrenciler[0]:
    print(eleman)

"""
Eda
Gul
90
100
80
"""

del ogrenciler[0][0]

print(ogrenciler[0]) # ['Gul', 90, 100, 80]
