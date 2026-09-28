# Variadic functions -> Functions that take a variable number of parameters

# sayilar = (10,20,30,40)

# def toplam(liste):
#    sonuc = 0
#    for i in liste:
#        sonuc += i
#    return sonuc

# print(toplam(sayilar))

def toplam(*args):
    print(args)  # (10,20)
    print(type(args))  # <class 'tuple'>
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc


print(toplam(10, 20))  # 30
print(toplam(10, 20, 30))  # 50
