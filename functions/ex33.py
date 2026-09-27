# Parameterized Functions
#Dynamic (değişim)

def selamlama(isim):
    return "Merhaba " + isim


print(selamlama("Eda"))
print(selamlama("Emre"))


def toplam(sayi1, sayi2):
    return sayi1 + sayi2


print(toplam(10, 20))


def yasHesapla(dogumYili):
    return 2026 - dogumYili


def emeklilikYasi(dogumYili, isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas

    if kalanSure > 0:
        return (f"{isim}, emekliliğinize {kalanSure} kaldı.")
    else:
        return (f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz.")
    # abs abstraction -> mutlak değer


print(emeklilikYasi(2000, "Eda"))
print(emeklilikYasi(1950, "Emre"))
