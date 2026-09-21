# Logical operators

x = 11

sonuc1 = (x > 5) and (x < 10)

# 1- and
sonuz2 = (x > 0) and (x % 2 == 0)  # True -> x is even

# 2- or
sonuc3 = (x > 0) or (x % 2 == 0)  # x is positive or odd

# 3-Not

sonuc4 = not (x > 0)  # False -> x is positive

# Examples

# 1- Yaş 18'den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.

yas = int(input("Yasınız: "))
veliIzni = int(input("veliIzni var mı?:(y/n) "))
if (yas > 18 or veliIzni == y):
    print("Çalışaiblirsiniz!!")
else:
    print("Çalışamazsınız")

# no if-else -> printf(f"Ders geçme durumu:{}")

# 2- Ders notu 50-100 arasındaysa geçti değilse kaldın bilgisini yazdırınız.

dersNotu = int(input("Not: "))
if (dersnotu > 50 and dersnotu < 100):
    print("Geçti")
else:
    print("Kaldı")

# 3- Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.
notOrtalama = int(input("notOrtalama: "))
zayıfSayisi = 0
(notOrtalama >= 70 and zayıfSayisi == 0)


# 4- İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu.
egitim = "önlisans"
sigara_icme = True

sonuc = (egitim == "önlisans" or egitim == "lisans") and (not (sigara_icme))

# 5- Uygulamaya giriş kontrolünü "username yada email" ve "parola" için yapalım.

email = "abcde@gmail.com"
username = "abcd"
password = "ruhi123"

girilen_bigi = input("email ya da username: ")
gieilen_parola = input("parola: ")

sonuc = (email == gieilen_bilgi or username ==
         girilen_bigi) and (password == gieilen_parola)
print(sonuc)
