# Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan bir
# uygulamayı yapınız.
# benzin : 39.35
# dizel  : 41.71
# lpg    : 20.28

yakıtTipi = input("(benzin/dizel/lpg)?:  ")
gidilenMesafe = int(input("Gidilen mesafe: "))

if (yakıtTipi == "benzin"):
    print(gidilenMesafe * 39.95)
elif (yakıtTipi == "dizel"):
    print(gidilenMesafe * 41.71)
else:
    print(gidilenMesafe * 20.28)


# Bir öğrencinin 2 yazılısı ve bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına
# karşılık gelen değerlendirmeyi yazdırınız.

#   0-24  -> 0
#   25-44 -> 1
#   45-54 -> 2
#   55-69 -> 3
#   70-84 -> 4
#   85-100 -> 5

yazili_1 = int(input("Yazılı 1: "))
yazili_2 = int(input("Yazılı 2: "))
sozlu_1 = int(input("Sözlü 1: "))

ortalamaHesapla = (yazili_1 + yazili_2 + sozlu_1) / 3

if (ortalamaHesapla <= 24):
    print("0")
elif (ortalamaHesapla <= 44):
    print("1")
elif (ortalamaHesapla <= 54):
    print("3")
elif (ortalamaHesapla <= 69):
    print("4")
else:
    print("5")
