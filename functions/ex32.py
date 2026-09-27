# Definiton and Return

def toplam():
    return 10+20

print(toplam())


def yil():
    import datetime
    return datetime.datetime.now().year
# sonra değineceğiz module lere

def saat():
    import datetime
    return datetime.datetime.now().hour


def yasHeapla():
    dogumYili = int(input("Dogdugunuz yil: "))
    return (yil() - dogumYili)

print(yasHeapla())

def sleamlama():
    if(saat() < 12):
        return "Günaydın"
    else:
        return "İyi Akşamlar"
print(sleamlama())