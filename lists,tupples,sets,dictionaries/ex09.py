# ---LIST METHODS ----

sayılar = [4,6,2,8, 56, 4]
isimler = ["Eda", "Emre", "Ata", "Nehir"]


sonuc = min(sayılar)
sonuc1 = min(isimler)
sonuc2 = max(sayılar)
sonuc3= max(isimler)

#ekleme

sayılar.append(12)
isimler.append("Nehir")

sayılar.insert(0, 100) 
sayılar.insert(-1, 100) #eklenen eleman(lar)ın yerindekini sağa kaydırıyor 
#[100, 4, 6, 2, 8, 56, 100, 12]
sayılar.insert(-3,100)
sayılar.insert(len(sayılar),100 ) # liste olduğu için len - 1 gerek yok 
sonuc4 = sayılar

print(sonuc4)


#silme 

sonuc5 = sayılar.pop() # 0. index i siler silineni döndürür
print(sayılar) # [100, 4, 6, 2, 8, 100, 56, 100, 12]
sonuc6= sayılar.pop(2) # 2. index i sil  
sonuc7 = isimler.remove('Nehir')

print(sonuc5)

# sıralama
print(sayılar.sort()) # returns none
isimler.sort()
print(isimler) # ['Ata', 'Eda', 'Emre', 'Nehir']


sayılar.reverse()
print(sayılar) #[100, 100, 100, 56, 12, 8, 4, 2]

say = sayılar.count(4)

print(say) # 2

# arama 

bul = sayılar.index(4) 
print(bul) # 6 -> returns the first index that the number is found.