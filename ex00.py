"""
Uygulama 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.

Uygulama 2: Klavyeden girilen kilometre bilgisini mil cinsinden hesaplyaınız.

"""

# 1:

pi = 3.14


r = (float(input("r = ")))

cemberAlan = pi * (r ** 2)
cevre = (2 * pi * r)

print("Alan ", cemberAlan)
print("Cevre " + str(cevre))

# 2:

km = float(input("km = "))  # girilen değer her zaman string olarak alınır
# string  ile bölme yapamayacağına göre her zaman döüştürmelisin

milHesaplama = km / 1.60934
milHesaplama = round(milHesaplama, 2)  # ondalıkllı kısmı iki basamağa yuvarla

print(milHesaplama)
print(str(km) + " km = " + str(milHesaplama) + " mil")
