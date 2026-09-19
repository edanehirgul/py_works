# ---- SETS ----
# indekslenemez .index yok
# sıralanamaz (random atanır)
# elemanlar güncellenemez
# elemanlar tekrarlanmaz
# eleman silinebilir ya da eklenebilir

# meyveler = {"elma","armut","kiraz"}

meyveler = {"elma", "armut", "kiraz", "elma"}
meyveler1 = {"elma", "armut", "kiraz","kavun"}

# sonuc = meyveler[0] error!! sets have no indexes

print(meyveler)  # {'kiraz', 'elma', 'armut'} random order

for x in meyveler:
    print(x)
print(meyveler) # {'armut', 'kiraz', 'elma'}

print("elma" in meyveler) # True -> Boolean

meyveler.add("karpuz")
print(meyveler) 
#{'kiraz', 'armut', 'elma', 'karpuz'}

meyveler.update(meyveler1) #combines the sets
print(meyveler)
#{'elma', 'karpuz', 'kiraz', 'armut', 'kavun'}

meyveler.remove("elma")
meyveler.discard("armut") # raise an error if set does not have the var
print(meyveler)
#{'elma', 'karpuz', 'kiraz', 'armut', 'kavun'}
meyveler.pop() # rastgele bir eleman siler (sıalama olmadığı için sondakini bilemeyiz)
print(meyveler)
#{'kavun', 'kiraz'}
meyveler.clear()#herkesi siler
print(meyveler)# set()