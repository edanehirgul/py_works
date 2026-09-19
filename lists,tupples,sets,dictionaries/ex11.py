
# ---TUPLE---

# elemanları değiştirilemeyen listeler -> tuple 
# güvenlik, performans arttırma 
# my_tuple = 1,2,3

my_list = [1,2,3]
my_tuple = 1,2,3

print(type(my_list)) #<class 'list'>
print(type(my_tuple)) #<class 'tuple'>

# sonuc = my_tuple[0] = 0 tuple' object does not support item assignment

#print(sonuc)

my_tuple2 = tuple((2,3,4))
# 2,3,4, listesi tuple olarak değişti
my_list2 = list(2,3,4)
# 2,3,4, listesi list olarak değişti
