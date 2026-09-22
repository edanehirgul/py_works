isim = "Eda Nehir"

for harf in isim:
    if (harf == "d"):
        continue  # o turdaki kodu iptal et -> d yazmaz devamı yazar
        # break -> direkt çıkar -> Sadece E yazar
    print(harf)

i = 0
while (i < 5):
    i += i
    if (i == 2):
        continue
        print(i)

n = 0
while (n <= 100):
    n += 1
    if(n % 2 == 1):
        continue
    toplam += n
    print(toplam) # 100 e kadar çift sayıları toplama