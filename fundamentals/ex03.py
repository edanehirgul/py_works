# ---- STRING FORMATLAMA ---

# ---string concat---
ad = "Eda"
soyad = "Gul"
yas = 20

mesaj = "My Name is: " + ad + " " + soyad + "."
print(mesaj)  # My Name is: Eda Gul.


# --string format--

# {} lar yerine sırayla var lar geliyo .format

msj = "My name is {} {}. I'm {} years old. ".format(ad, soyad, yas)
msj1 = "My name is {1} {0}. I'm {2} years old. ".format(ad, soyad, yas)  # index mantığı tamamen gul eda 20 olucak
msj2 = "My name is {a} {s}. I'm {y} years old. ".format(a =ad, s = soyad,y = yas)

print(msj)
# My name is Eda Gul. I'm 20 years old.
print(msj1)
#My name is Gul Eda. I'm 20 years old. 
print(msj2)
#My name is Eda Gul. I'm 20 years old. 



#    f-string

msj3 = f"My name is {ad} {soyad}. I'm {yas} years old."
print(msj3)
# {} lar yerine sırayla var lar geliyo .format
