customers = ["sadikturan", "ahmetyilmaz", "cintarturan", "yigitbilgi"]
order_totals = [12000, 13000, 5000, 15000]

# 1- 'sadikturan' kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyiniz.
customers.append("sadikturan")
order_totals.append("5000")


# 2- Son eklenen siparişi siliniz.

customers.pop(4)
order_totals.pop(4)


# 3- Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız.
#    '<username>' isimli müşterinin sipariş toplamı '<10000>' liradır.

print(f"{customers[0]} isimli müşterinin sipariş toplamı {order_totals[0]} liradır.")
print(f"{customers[1]} isimli müşterinin sipariş toplamı {order_totals[1]} liradır.")
print(f"{customers[2]} isimli müşterinin sipariş toplamı {order_totals[2]} liradır.")
print(f"{customers[3]} isimli müşterinin sipariş toplamı {order_totals[3]} liradır.")


# 4- Müşterileri alfabetik olarak sıralayınız.
customers.sort()


# 5- Sipariş toplamlarını azalan şekilde sıralayınız.
order_totals.sort()
order_totals.reverse()

# 6- En düşük sipariş hangisidir?

print(order_totals[0])

# 7- 'sadikturan' isimli kullanıcının kaç tane siparişi vardır?

customers.index("sadikturan")

# 8- Customers listesinden 'ahmetyilmaz' isimli kullanıcıyı siliniz.

customers.remove("ahmetyilmaz")

# 9- Listelerdeki tüm içerikleri siliniz.

customers.clear()
order_totals.clear()

# 10- Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.

ad = input("Ad: ")
fiyat = input("Fiyat: ")

customers.append(ad)
order_totals.append(fiyat)



print(customers)
print(order_totals)
