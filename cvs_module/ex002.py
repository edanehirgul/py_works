import csv

with open('ogrenciler.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('ogrenciler2.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

print("Yeni csv ogrenciler2 olustu")
#ogreniler 2 olustu 
# isim	yas	sehir	puan
# Ahmet	20	Istanbul	85
# Ayse	22	Ankara	92
# Mehmet	19	Izmir	78
# Zeynep	21	Bursa	95

