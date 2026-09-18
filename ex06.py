#--- EXAMPLES --

kursAdi = "Btk Akademi Python ile Programlama Dersleri"
website = "https://www.btkakademi.gov.tr/"


# 1- ' Btk Akademi ' karakter dizisinin baş ve sonundaki boşluk karakterlerini siliniz

print(' Btk Akademi '.strip())

# 2- kursAdi değişkeninin tüm karakterlerini küçük harfe çeviriniz

print(kursAdi.lower)

# 3- website değişkenindeki kaç tane '.' karakteri vardır ?

print(website.count('.')) # .count -> Returns the number of times a specified value occurs in a string

# 4- website değişkeni 'https' ile mi başlıyor?

print(website.startswith('https'))

# 5- webiste 'tr' ile mi bitiyor?

print(website.endswith('tr'))

# 6- kursAdi içerisindeki tüm karakterler harflerden mi oluşuyor ?

print(kursAdi.isalpha())

# 7- kursAdi değişkenindeki tüm boşlukları '-' ile değiştiriniz

print(kursAdi.replace(" ", '-'))

# 8- kursAdi değişkenindeki Python kelimesini ReactJs ile değiştiriniz

print(kursAdi.replace("Python", "ReactJc"))

# 9- website değişkeni "www" içeriyor mu?

print(website.find('www'))
# if there is no return value find method returns -1 besides index method 

# 10- kursAdi değişkenini listeye çeviriniz 

print(kursAdi.split())