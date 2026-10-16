
# with open("markalar.txt", "a") as file:
#     file.write("6-BMW")


# En başa eleman eklemek için tüm listeyi öteliyoruz

# with open("markalar.txt","r+",encoding="utf-8") as file:
#     markalar = file.read()
#     markalar = "1-Toyata\n" + markalar
#     file.seek(0)
#     file.write(markalar)

with open("markalar.txt", "r+", encoding="utf-8") as file:
    markalar = file.readlines()
    markalar.insert(2, "3-Renault")
    file.seek(0)
    for marka in markalar:
        print(marka, end="")
    print("")
#  -> file.writelines(marka)


# with open("markalar.txt", "r", encoding="utf-8") as file:
#     print(file.read())
