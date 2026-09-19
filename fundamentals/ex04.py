
# Examples

title = "Pyhton ile Programlama Dersleri"

# 1- "title" değişkeni içerisindeki karakter sayısı nedir ?

adet = len(title)
print(adet)

# 2- "title" içerisindeki 'Python' kelimesine alın.

print(title[:6])

# 3- "title" değişkeninin ilk 5 ve son 5 karakterini alın

print(title[:6])
print(title[-8:])

# 4- "title" title değişkenini tersten yazdırınız

print(title[::-1])

# 5- Klavyeden girile bilgiye göre örnek verilen cümleyi yazdırınız.
# Örnek: Çınar Turan isimli öğrencinin  1. notu 60,2. notu 60 ve not ortalaması 60 olarak hesaplanmıştır.

not1 = int(input("1. not: "))
not2 = int(input("2. not: "))
ortHesapla = (not1 + not2) / 2

ad = input("Ad: ")
soyad = input("Soyad: ")

msj = f"{ad} {soyad} isimli öğrencinin 1. notu {not1}, 2.notu {not2} ve not ortalaması {ortHesapla} olarak hesaplanmıştır."

print(msj)
