# Aşağıdaki öğrenci bilgilerini dictionary listesinde saklayınız.

# 101 Yiğit Bilgi 2010 (40,80,90)
# 102 Ada Bilgi   2012 (80,80,80)
# 103 Çınar Turan 2017 (70,70,70)

ogrenciler = {
    101: {
        "Ad": "Yigit",
        "Soyad": "Bİlgi",
        "DogumYili": 2010,
        "Notlar": (40, 80, 90)
    },
    102: {
        "Ad": "Ada",
        "Soyad": "Bİlgi",
        "DogumYili": 2012,
        "Notlar": (80, 80, 80)
    },
    103: {
        "Ad": "Çınar",
        "Soyad": "Turan",
        "DogumYili": 2017,
        "Notlar": (70, 70, 70)

    }
}


# Klavyeden girilen öğrenci numarasına göre aşağıdaki cümleyi yazdırınız.

# 101 numaralı Yiğit Bilgi isimindeki öğrencinin yaşı 14 ve not ortalaması 70.

ogrenciNo = int(input("Ogrenci no: "))
print(ogrenciler[ogrenciNo])

ogrenci = ogrenciler[ogrenciNo]
ortalama = (ogrenci["Notlar"][0] + ogrenci["Notlar"]
            [1] + ogrenci["Notlar"][2]) / 3

print(
    f"{ogrenciNo} numaralı {ogrenci["Ad"]} isimindeki öğrencinin yaşı {2026 - ogrenci["DogumYili"]} ve not ortalaması {ortalama}.")
