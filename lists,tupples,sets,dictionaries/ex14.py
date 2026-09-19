# --DICTOINARY METHODS ---

yemekTarifi = {
    "yemekAdi": "Musakka",
    "yemekTarifi": " tarif acıklamasi",
    "resim": "1.jpg"

}

# Access Items
sonuc = yemekTarifi["yemekAdi"]  # Musakka
print(sonuc)


sonuc1 = yemekTarifi.get("yemekAdi")
print(sonuc1)  # Musakka

sonuc2 = yemekTarifi.keys()
print(sonuc2)  # dict_keys(['yemekAdi', 'yemekTarifi', 'resim'])

sonuc3 = yemekTarifi.values()
print(sonuc3)  # dict_values(['Musakka', ' tarif acıklamasi', '1.jpg'])

sonuc4 = yemekTarifi.items()
print(sonuc4)
# dict_items([('yemekAdi', 'Musakka'), ('yemekTarifi', ' tarif acıklamasi'), ('resim', '1.jpg')])

# Update Items

yemekTarifi["yemekAdi"] = "Mantı"

print(yemekTarifi)
#{'yemekAdi': 'Mantı', 'yemekTarifi': ' tarif acıklamasi', 'resim': '1.jpg'}

yemekTarifi["yemekAdi2"] = "Mantı" # adds a new pair if there is no key-value pair
print(yemekTarifi)
#{'yemekAdi': 'Mantı', 'yemekTarifi': ' tarif acıklamasi', 'resim': '1.jpg', 'yemekAdi2': 'Mantı'}

yemekTarifi.update({"yemekAdi": "Mantı"})
yemekTarifi.update({"yemekAdi2": "Mantı"})
#ekleme, güncelleme kısmının metotları

#Delete Items

yemekTarifi.pop("yemekAdi")
print(yemekTarifi) # yemekAdi ikilisi silindi
#{'yemekTarifi': ' tarif acıklamasi', 'resim': '1.jpg', 'yemekAdi2': 'Mantı'}

yemekTarifi.popitem()
print(yemekTarifi)# son item silindi
#{'yemekTarifi': ' tarif acıklamasi', 'resim': '1.jpg'}

yemekTarifi.clear() # Her şeyi siler
print(yemekTarifi) # {}

# Copy => referans