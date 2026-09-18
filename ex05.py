# --STRING METHODS---

msj = "BTK Akademi Python Kursu"

sonuc = msj.upper()
print(sonuc)  # BTK AKADEMI PYTHON KURSU
# hepsi uppercase oldu

sonuc1 = msj.lower()
print(sonuc1)  # btk akademi python kursu
# hepsi lowercase

sonuc2 = msj.title()
print(sonuc2)  # Btk Akademi Python Kursu
# Converts the first character of each word to upper case

sonuc3 = msj.capitalize()
print(sonuc3)  # Btk Akademi Python Kursu
# Converts the first character to upper case and rest became lower

sonuc4 = "abc".isupper()
print(sonuc4)  # Returns True if all characters in the string are upper case

sonuc5 = "abc".islower()
print(sonuc5)  # Returns True if all characters in the string are lower case

sonuc6 = msj.strip()  # başında ya da sonunda boşlukları siler
print(sonuc6)  # BTK Akademi Python Kursu


sonuc7 = msj.split()  # boşluklardan yola çıkıp listeleme yapar
print(sonuc7)  # ['BTK', 'Akademi', 'Python', 'Kursu']
# eğer .split(',') yazarsan virgüllere göre ayırır -> ()içindekine göre ayırır

sonuc8 = msj.index("i")
# sonuc8 = msj.index("Akademi") -> 4 // msj.index("z") -> error because it doesnt have z
print(sonuc8)  # 10
# Searches the string for a specified value and returns the position of where it was found

sonuc9 = msj.startswith("a")
print(sonuc9)  # False
# checks if the value starts with that

sonuc10 = msj.endswith("u")
print(sonuc10)  # True
# checks if the value ends with that

sonuc11 = msj.replace("Python", "Java")
print(sonuc11)  # BTK Akademi Java Kursu
# replaces values
