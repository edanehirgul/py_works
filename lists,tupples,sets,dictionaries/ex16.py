x = 10
y = 20

x = y 
print(x, y) # 20 20 

a = ["elma", "armut"]
b = ["elma", "armut"]

a = b # adresleri kopyalama
a[0] = "uzum"

print(a, b) #['uzum', 'armut'] ['uzum', 'armut']

# LISTE KOPYALAMA
# 1-

listeA = [10,20]

listeB = listeA.copy() # farklı adreste alan aç ve kopyayı oluştur
# aynı adrese atama olmaz
listeA[0] = 30
print(listeA,listeB)
#[30, 20] [10, 20]

listeB = listeA
print(listeA,listeB)
# [30, 20] [30, 20]


# 2-
listeA = [10,20]
listeB = list(listeA)
listeA[0] = 30
print(listeA,listeB)


# adres kopyalamak ile verinin kendisini kopyalamak farklı