# OOP Objected Oriented Programming

# Class
# Instance - Nesne - Object

liste1 = [1, 2, 3]
liste2 = [1, 2, 3, 4]

# print(type(liste1))  # <class 'list'>

# Class


class Product:
    # Instance method
    def get_product(self):
        return f"Ürün adı:{self.name}, Ürün fiyatı: {self.fiyat}"

    def kdv_price(self):
        return self.fiyat * 1.20

    # attribute, property

    #   Constructor
    def __init__(self, name, fiyat: int):  # self -> sııftan türetilecek nesnelerin alanı
        self.name = name
        self.fiyat = fiyat
#        print("Nesne Oluşturuldu.") # 2 times


# Instance, Nesne
p1 = Product("Iphone 15", 100)
p2 = Product("Samgung Galaxy A5", 100)

print(p1.name, p1.fiyat)  # Iphone 15 100
print(p2.name, p2.fiyat)  # Samgung Galaxy A5 100

liste = [p1, p2]

for i in liste:
    print(i.get_product())
    print("KDV'li fiyat: " + str(i.kdv_price()) + "\n")

"""
Ürün adı:Iphone 15, Ürün fiyatı: 100
Ürün adı:Samgung Galaxy A5, Ürün fiyatı: 100
"""
