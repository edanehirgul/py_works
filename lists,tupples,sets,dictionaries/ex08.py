# -- EXAMPLES ---

# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.

arabalar = ["Toyota", "Bmw", "Renault", "Mercedes"]

# 2- Liste kaç elemanlıdır?

print(len(arabalar))

# 3- Listenin ilk ve son elemanı nedir?

print(arabalar[0], arabalar[-1])

# 4- "Renault" markasını "Togg" ile güncelleyiniz.

arabalar[2] = "Togg"
print(arabalar)

# 5- "Togg" listenin bir elemanı mıdır?
print("Togg" in arabalar)
print("Togg" not in arabalar)

# 6- Listenin ilk 2 elemanını siliniz.

del arabalar[0], arabalar[1]
print(arabalar)

# 7- Listenin sonuna "Ford" ve "Citroen" markalarını sıralayınız.

print(arabalar + ["Ford", "Citroen"])

# 8- Listenin son elemanını siliniz.

adet = len(arabalar)
del arabalar[adet - 1]
print(arabalar)

# 9- Aşağıdaki verileri liste içerisinde saklayınız.
# ogrenci1: Yiğit Bilgi 2010 [70,80,90]
# ogrenci2: Ada Bilgi 2011 [70,70,90]
# ogrenci3: Çınar Turan 2017 [60,60,90]

ogrenci1 = ["Yiğit", "Bilgi", 2010, 70, 80, 90]
ogrenci3 = ["Çınar", "Turan", 2017, 60, 60, 90]
ogrenci2 = ["Ada", "Bilgi", 2011, 70, 70, 90]

ogrenciler = [ogrenci1, ogrenci2, ogrenci3]

# 10- Öğrencilerinin yaşlarını hesaplayınız.

year = int(input("What year are we in? "))
print(year - ogrenci1[2])
print(year - ogrenciler[0][2])
print(year - ogrenci2[2])
print(year - ogrenci3[2])


# 11- Öğrencilerin yaş ortalamasını hesaplayınız.

hesaplama = ((year - ogrenci1[2]) + (year - ogrenci2[2]) + (year - ogrenciler[0][2])) / len(ogrenciler)
print(hesaplama)
