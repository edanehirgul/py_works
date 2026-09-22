# Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
# dictionary listesi yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyad) şeklinde olsun.
# öğrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz.
devammi = "e"
ogrenciler = []
while (devammi != "h"):
    ogrenciNo = input("Öğrenci no: ")
    ogrenciAdi = input("Öğrenci adı: ")
    ogrenciSoyad = input("Öğrenci soyadı: ")

    ogrenciler.append({
        "ogrenciNo": ogrenciNo,
        "ogrenciAdi": ogrenciAdi,
        "ogrenciSoyadi": ogrenciSoyad,
    })

    devammi = input("Devam mı? (e/h): ")

for ogrenci in ogrenciler:
    print(
        f"{ogrenci["ogrenciNo"]} numaralı öğrencinin adı {ogrenci["ogrenciAdi"]} {ogrenci["ogrenciSoyadi"]}")
