# open(dosya_adi,dosya_erişim_modu)
# dosya_erişim_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "r": (Read) okuma. Dosya konumda yoksa hata verir.
# "w": (Write) yazma modu.
#      Dosyayı konumda oluşturur.
#      Dosya içereğini siler ve yeniden ekleme yapar.
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "r+": Hem okuma hem yazma modunda açılır. Dosya konumda yoksa hata verir.

with open("dosya.txt", "a") as file:
    file.seek(0)  # a modunda seek komutu işlevsel değil çalışmaz.
    file.write("İkinci satır\n")

with open("dosya.txt", "r") as file:
    print(file.read())
