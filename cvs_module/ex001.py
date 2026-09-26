import csv

with open("ogrenciler.csv", "w", newline="") as cvs_file:
    # with -> dosya ile işimiz bittiğinde dosyanın düzgün şekilde kapatılmasını sağlar.
    # "ogrenciler.csv" isimli dosyayı açıyoruz.
    # "w" -> write: yazma modu
    # Eğer dosya yoksa oluşturur.
    # Eğer dosya varsa içeriğini silip yeniden yazar.
    # newline="" -> satır sonlarının düzgün şekilde yazılmasına yardımcı olur.

    yazici = csv.writer(cvs_file)
    # writer() -> library for csv
    # csv.writer() -> açtığımız dosyaya CSV formatında
    # veri yazmamızı sağlayan writer nesnesini oluşturur.
    # cvs_file -> yazma işlemini yapacağımız dosya.

    # Sütun başlıkları
    yazici.writerow(["isim", "yas", "sehir", "puan"])  # writerow() -> satır yaz

    # Öğrenciler
    yazici.writerow(["Ahmet", 20, "Istanbul", 85])
    yazici.writerow(["Ayse", 22, "Ankara", 92])
    yazici.writerow(["Mehmet", 19, "Izmir", 78])
    yazici.writerow(["Zeynep", 21, "Bursa", 95])

print("CSV dosyası oluşturuldu!")
# after executing the programme there will be a new CSV file


import csv

with open("ogrenciler.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    print(csv_reader)  # only the adress is shown <_csv.reader object at 0x7e707b62c040>

    for line in csv_reader:
        print(line) #! dosya okundu bitti, tekrar işlem için açman şart
        
# ['isim', 'yas', 'sehir', 'puan']
# ['Ahmet', '20', 'Istanbul', '85']
# ['Ayse', '22', 'Ankara', '92']
# ['Mehmet', '19', 'Izmir', '78']
# ['Zeynep', '21', 'Bursa', '95']

with open("ogrenciler.csv", "r") as csv_file: #tekrar açıldı (başa dönüldü) 
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[2]) #şehirleri ->2. index i verecek
#sehir
#Istanbul
#Ankara
#Izmir
#Bursa  



        