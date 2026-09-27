# Default Parameter Values

# !!!Sadece son değer default olabilir!!!

def selamlama(isim, mesaj="İyi Günler"):
    # mesaj için değer almazsa default olarak "İyi Günler" yazar.
    return f"{mesaj} {isim}"


print(selamlama("Eda"))
# İyi Günler Eda


def usAlma(taban, us=2):
    return taban ** us


print(usAlma(3))
# 3 ** 2 = 9


def toplam(a, b):
    return a+b


def cıkarma(a, b):
    return a-b


def islem(a, b, fn=toplam):
    return fn(a, b)


print(islem(3, 2, cıkarma))  # 3-2 = 1
print(islem(3, 2))  # Default -> 3+2 = 5

# fonk içinde fonk çağırma kısayolu -> fn fn
