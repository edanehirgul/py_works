# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

import random


def kereYaz(kelime):
    a = int(input("Kaç kere yazılmalı? "))
    count = 1
    while (a >= count):
        print(kelime)
        count += 1
# def yazdir(text, adet):
#   return text * adet
# print(yazdir("Eda", 2)) -> EdaEda

# 2- Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.


def alanHesapla(uzunluk, en):
    print("Çevre = " + str(2 * (uzunluk + en)))
    print("Alan = " + str(uzunluk * en))


alanHesapla(2, 5)


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
ihtimaller = ["Yazı", "Tura"]

sonuc = random.choice(ihtimaller)
print(sonuc)

# sayi = random.randint(1,10) -> print(sayi)  10>= sayi >=1 (int)
# sayi = random.random() -> print(sayi) 1>= sayi >=0  (float)
# isim = ["a","b"] -> sonuc = random.choice(isim) -> print(sonuc) a or b
# liste = [1,2,3] -> random.shuffle(liste) -> print(liste) [random order of numbs]

# 4- Kendisine gönderilen 2 sayı arasındaki tam asal sayıları bulan fonksiyonu yazınız.


def asalMı(sayi1):
    i = 2
    while (sayi1 > i):
        if (sayi1 % i == 0):
            return (-1)  # asal değil
        else:
            i += 1
    return (0)  # asal


def asalBul(sayi1, sayi2):
    if (sayi1 > sayi2):
        temp = sayi1
        sayi1 = sayi2
        sayi2 = temp
        print("Sayılar değişti: " + str(sayi1) + " " + str(sayi2))

    while (sayi2 > sayi1):
        sayi1 += 1
        if (asalMı(sayi1) == 0):
            print(sayi1)


asalBul(sayi1=int(input("Sayı 1: ")), sayi2=int(input("Sayı 2: ")))

# def asalSayilarBul(sayi1, sayi2):
#   for sayi in range(sayi1, sayi2 +1)
#       if(sayi > 1):
#           for i in range(2, sayi):
#               break
#           else:
#               print(sayi)

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir listede şeklinde döndüren fonksiyonu yazınız.


def boleniMi(sayi3):
    numb = 1
    liste = []
    while (sayi3 >= numb):
        if (sayi3 % numb == 0):
            # .append() : none döndürür (listeye eleman ekler)
            liste.append(numb)
        numb += 1

    return (liste)


print(boleniMi(12))
