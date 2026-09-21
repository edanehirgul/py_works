a, b, c, d = 2, 2, 10, 5

print(a == b)  # True
print(a != c)  # True
print(a != b)  # False

print(True == 1)  # True
print(False == 0)  # True

# 1- Girilen 2 sayıdan hangisi büyüktür?

sayi1 = int(input("Sayı 1: "))
sayi2 = int(input("Sayı 2: "))

if sayi1 > sayi2:
    print(sayi1)
else:
    print(sayi2)
    print(f"{sayi2} büyüktür {sayi1}")

# 2- Girilen sayınınn tek çift kontrolünü yapınız.

sayi3 = int(input("Sayı 3: "))

if sayi3 % 2 == 0:
    print("even")
else:
    print("odd")

# 3- Bir öğrencinin girilen üç notuna göre başarı durumunu kontrol (50 ve üstü başarılı)

not1 = int(input("Not 1: "))
not2 = int(input("Not 2: "))
not3 = int(input("Not 3: "))

ogrenciNotlar = [not1, not2, not3]

if (ogrenciNotlar[0] + ogrenciNotlar[1] + ogrenciNotlar[2]) / len(ogrenciNotlar) >= 50:
    print("Başarılı!")
else:
    print("Başarısız :(")

# print(f"Öğrencinin not ortalaması: {}, başarı durumu {}") bu ifade de kullanılabilir.

# Identifier and Membership Operators

x = [1, 2, 50]
y = [1, 2, 3]

z = y

print(x is y)  # False
print(x == y)  # False
print(x is not y)  # True
print(z is y)  # True
