"""
    Dosy açmak ve oluşturmak için open() fonksiyonu kullanılır.

    Kullanım          :open(dosya_adı,dosya_erişme_modu)
    dosya_erişme_modu :dosyayı hangi amaçla açtığımızı belirtir.
    "r" okuma komutu  :okuma modu,belirtilen konumda dosya olmalıdır.
    seek              :cursor konumu
"""

# there has to be a file as log.txt

f = open("log.txt", "r")

print(f.read())

print(f.readlines())
