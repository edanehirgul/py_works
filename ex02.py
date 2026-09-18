
# ---- STRING SLICING ----

kurs = "Python ile programlama"

print(kurs[0])  # P
print(kurs[-1])  # a

adet = len(kurs)

print(adet)  # dizi uzunluğu verir
print(kurs[adet - 1])  # son karaktere gider
# adet dersen out of range olur index 0 dan başlar çünkü len -1 e kadar gider

# ---- SLICING String ---
# Pytho 4.index e kadaar alır string de en sonda "\0" null var
print(kurs[0:5])  # pytho
print(kurs[0:6])  # pyhton
print(kurs[:6])  # python
print(kurs[11:adet])  # programlama
print(kurs[11:])  # programlama

print(kurs[-11:-1])  # programlam  !! a yı almadı len - 1 mantığı
print(kurs[-11:0])  # programlama

print(kurs[7:0])  # ile programlama

# dizi hep sağa doğru sayar
# !! index her zaman 0 dan başlar sayarken 0 dan başlamalısın
# !! space  vs kısımlar da birer indextir

print(kurs[0:20:2])  # 1-3-5-7...  ikişer sayma
print(kurs[::])  # Python ile programlama = print(kurs[::1])
# amalmargorp eli nohtyP  ters çevirdi (geriye doğru git örüntüde gitmek gibi aynen)
print(kurs[::-1])
