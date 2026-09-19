# ---DICTIONARY---

# key-value info
#!! tekrarlanmaz
# sıralanabilir
# güncellenebilir

# plakalar = {'kocaeli': 41,
#            'istanbul': 34
#             }

sehirler = ["kocaeli", "istanbul"]
plakalar = [41, 34]

print(plakalar[0], sehirler[0])
print(plakalar[1], sehirler[1])

# no need its too long

print(plakalar[sehirler.index('istanbul')])
print(plakalar[sehirler.index('kocaeli')])

# still long and no needed

plakalar = {'kocaeli': 41,
            'istanbul': 34
            }

print(plakalar)  # {'kocaeli': 41, 'istanbul': 34}
print(plakalar['kocaeli'])  # 41
print(plakalar['istanbul'])  # 34
