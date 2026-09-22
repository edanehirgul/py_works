sayilar = [3, 5, 7, 2, 12, 32, 45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.

for i in sayilar:
    print(i)

# 2- "sayilar" listesindeki hangi sayilar 3 ün katıdır?
for x in sayilar:
    if (x % 3 == 0):
        print(f"{x} 3'ün katıdır.")
    else:
        print(f"{x} 3'ün katı değildir.")

# 3- "sayilar" listesindeki tüm sayıların toplamı nedir?
sum = 0
for n in sayilar:
    sum = sum + n
print(sum)

urunler = ["samsung s24", "samsung s22", "iphone 14", "iphone 15"]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz.

for m in urunler:
    print(m.find('iphone'))
    # varsa 0 yoksa -1 (.index -> yoksa hata verir)

# 5- "urunler" listesinde kaç adet samsung ürünü vardır?
adet = 0
for urun in urunler:
    index = urun.find('samsung')
    if (index > -1):
        adet += 1
print(adet)  # 2
