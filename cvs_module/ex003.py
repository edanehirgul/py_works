import csv
with open('ogrenciler.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)
        # print(line'yas') -> sadece yas bilgilerini listeler

# {'isim': 'Ahmet', 'yas': '20', 'sehir': 'Istanbul', 'puan': '85'}
# {'isim': 'Ayse', 'yas': '22', 'sehir': 'Ankara', 'puan': '92'}
# {'isim': 'Mehmet', 'yas': '19', 'sehir': 'Izmir', 'puan': '78'}
# {'isim': 'Zeynep', 'yas': '21', 'sehir': 'Bursa', 'puan': '95'}
# easy to understand the pairs

    with open('ogrencilerDict.csv', 'w') as new_file:
        fieldnames = ['isim','sehir','puan']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader() #writes the headers

        for line in csv_reader:
            print("Okunan veri: ", line)
            del line['yas']
            csv_writer.writerow(line)
