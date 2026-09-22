# for -> list

sayilar = [1, 2, 3, 5, 6, 8, 91, 300]  # 8 eleman

for x in sayilar:
    print(x)
    print("Merhaba BTK Akademi")  # 8 kere yazar

isimler = ["Emre", "Eda", "Ata"]
for y in isimler:
    print(y)  # isimleri alt alta yazar

isim = "Eda Nehir Gül"
for i in isim:
    print(i)


my_tuple = {(1, 2), (3, 4), (5, 6)}

for n, m in my_tuple:
    print(n, m)

my_dictionary = {"34": "Istanbul", "53": "Rize", "60": "Tokat"}
for a in my_dictionary.values():
    print(a)
for a in my_dictionary.keys():
    print(a)
for a,b in my_dictionary.items():
    print(a,b)
# while -> koşullu


