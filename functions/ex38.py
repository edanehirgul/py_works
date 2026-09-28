# Bank Account

# Hesap bilgileri tutulacak.(dict)
# Menu,paraCekme,bakiyeSorgulama,paraYatirma, fonksiyonları tanımlanacak.
# Cekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.


hesaplar = [
    {
        "Ad": "Eda",
        "Soyad": "Gül",
        "username": "Eda Gül",
        "password": "ruhi123",
        "HesapNo": "Hesap1",
        "Bakiye": 1000,
        "EkHesap": 3000
    },
    {
        "Ad": "Eda",
        "Soyad": "Gül",
        "username": "Eda Gül",
        "password": "ruhi1234",
        "HesapNo": "Hesap2",
        "Bakiye": 5000,
        "EkHesap": 100
    }
]


def menu():
    print("Merhaba Eda Gül")

    print("1- Para Çekme")
    print("2- Para Yatırma")
    print("3- Bakiye Sorgulama")
    islemNo = int(input("Hangi işlemi yapmak istiyorsunuz(1/2/3)?: "))

    if islemNo == 1:
        paraCekme()
    elif islemNo == 2:
        paraYatırma()
    elif islemNo == 3:
        bakiyeSorgulama()
    else:
        print("Yanlış değer girdiniz! İşlem numarasını tekrar yazın.")


def login():

    un = (input("Username: "))
    psw = (input("Password: "))

    for hesap in hesaplar:
        if hesap["username"] == un and hesap["password"] == psw:
            menu()
            return
        print("Şifre ya da kullanıcı adı yanlış!")


def bakiyeSorgulama():
    print("Hesap 1 ana bakiyesi =  " + str(hesaplar[0]["Bakiye"]))
    print("Hesap 1 ek hesap bakiyesi = " + str(hesaplar[0]["EkHesap"]))
    print("Hesap 2 ana hesap bakiyesi = " + str(hesaplar[1]["Bakiye"]))
    print("Hesap 2 ek hesap bakiyesi = " + str(hesaplar[1]["EkHesap"]))


def paraCekme():
    sayi = int(input("Kaç para çekeceksiniz?: "))
    hesapno = int(input("Hangi hesaptan para çekilmeli ?(1/2): "))
    if hesapno == 1:
        if sayi > hesaplar[0]["Bakiye"]:
            print("Yetersiz Bakiyeden dolayı ek hesaptan para çekme deneniyor...")
            if sayi > hesaplar[0]["EkHesap"]:
                print(
                    "Ek hesapta da para olmadığından işlem iptal edildi.(Fakirsiniz :) ")
            else:
                hesaplar[0]["EkHesap"] -= sayi
                print(
                    f"Hesap1 EkHesap bakiyesi artık {hesaplar[0]["EkHesap"]}")
        else:
            hesaplar[0]["Bakiye"] -= sayi
            print(f"Hesap1 ana bakiyesi artık {hesaplar[0]["Bakiye"]}")
    else:
        if sayi > hesaplar[1]["Bakiye"]:
            print("Yetersiz Bakiyeden dolayı ek hesaptan para çekme deneniyor...")
            if sayi > hesaplar[1]["EkHesap"]:
                print(
                    "Ek hesapta da para olmadığından işlem iptal edildi.(Fakirsiniz :) )")
            else:
                hesaplar[1]["EkHesap"] -= sayi
                print(
                    f"Hesap1 EkHesap bakiyesi artık {hesaplar[1]["EkHesap"]}")

        else:
            hesaplar[1]["Bakiye"] -= sayi
            print(f"Hesap1 ana bakiyesi artık {hesaplar[0]["Bakiye"]}")


def paraYatırma():
    sayi = int(input("Kaç para yatıracaksınız?: "))
    hesapno2 = int(input("Hangi hesaba para yatırmak isteriniz?(1/2): "))
    if hesapno2 == 1:
        hesaplar[0]["Bakiye"] += sayi
        print(f"Para yatırıldı. Yeni bakiyeniz {hesaplar[0]["Bakiye"]}")
    else:
        hesaplar[1]["Bakiye"] += sayi
        print(f"Para yatırıldı. Yeni bakiyeniz {hesaplar[1]["Bakiye"]}")


login()

# pass -> null operation - nothing happens when it executes.
