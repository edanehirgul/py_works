# for => list
# whlie => koşullu

i = 0
while (i < 10):
    print("Merhaba BTK Akademi!")
    i += 1  # 10 times

# for yerine while
sayilar = [1, 3, 5, 7, 67]
n = 0
while (n < len(sayilar)):
    print(sayilar[n])
    n += 1

# 1- Başlangıç ve bitiş değerlerini kullanıcıdan alınız.
# Bu değerler arasındaki çift sayıları yazdırınız.

baslangıc = int(input("Başlangıç değeri: "))
son = int(input("Bitiş değeri: "))

n = 0
while (not (n > baslangıc and n < son)):
    n += 1

while (n >= baslangıc and n < son):
    if (n % 2 == 0):
        print(n)
    n += 1

# 2- (1-100) arasındaki sayıları azalan şekilde sıralayınız.
m = 100
while (m > 0):
    print(m)
    m -= 1
# 3- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı şekilde yazdırınız.
k = 0
sayilar = []
while (k < 5):
    sayi = input("sayı: ")
    sayilar.append(sayi)
    k += 1

# 4- Klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar
# username girişi isteyiniz.

username = ""  # karakter olmaması -> boşluk var

while not (username):
    username = input("Kullanıcı Adı: ")
print("Girilen username: " + username)
