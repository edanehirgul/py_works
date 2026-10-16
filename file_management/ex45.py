# Not Uygulaması

# 1-Menu
# 1- Not Gir
# 2- Ortalamaları Göster (90-100 -> AA, 85-89 -> BA)
# 3- Notları Kayıt Et
# 4- Çıkış

def not_hesapla(satır):
    satır = satır[:-1]  # \n i çıkardık
    # satırı : 'dan ayırdı ilk kısım [0], son kısım [1]
    liste = satır.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")  # ayırdığımız kısmı da ayırıyoruz

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 80 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 75 and ortalama <= 79:
        harf = "BB"
    elif ortalama >= 70 and ortalama <= 74:
        harf = "CB"
    elif ortalama >= 65 and ortalama <= 69:
        harf = "CC"
    elif ortalama >= 50 and ortalama <= 64:
        harf = "DC"
    elif ortalama >= 40 and ortalama <= 49:
        harf = "DD"
    elif ortalama >= 0 and ortalama <= 39:
        harf = "FF"
    return f"{ogrenciAdi} : {harf} ({ortalama})\n"


def not_gir():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = input("Not1: ")
    not2 = input("Not2: ")
    not3 = input("Not3: ")

    with open("sınav_notları.txt", "a", encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + not1 +
                   "," + not2 + "," + not3 + "\n")


def notları_oku():
    with open("sınav_notları.txt", "r", encoding="utf-8") as file:
        for satır in file:
            print(not_hesapla(satır))


def notları_kaydet():
    with open("sınav_notları.txt", "r", encoding="utf-8") as file:
        liste = []
        for satır in file:
            liste.append(not_hesapla(satır))

        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            file2.writelines(liste)
            print("Sonuclar ,sonuclar dosyasına yazıldı!")


while True:
    islem = input("1- Not Gir\n2-Notları Oku\n3- Notları Kayıt Et\n4-Çıkış\n")

    if islem == "1":
        not_gir()
    elif islem == "2":
        notları_oku()
    elif islem == "3":
        notları_kaydet()
    else:
        break
