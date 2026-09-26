import json

with open('ex2.json', 'r') as json_file:
    data = json.load(json_file)

for name in data:
    print(name)
# everything is listed

with open('new_names.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)

print(len(data))
# 2 every dict has one name value so it counts the dicts

# especially for name value

count = 0

for person in data:
    if 'name' in person:
        count += 1
print(count)
print(type(person))  # <class 'dict'>
print(type(data))  # <class 'list'>

# data
#  │
#  ▼
# ┌───────────────────────────────────┐
# │             LIST                  │
# │                                   │
# │   [0] ──► DICTIONARY             │
# │             │                     │
# │             ├─ name → Big Corp.   │
# │             ├─ employees → 1000   │
# │             ├─ ceo → Mary         │
# │             └─ rating → 3.6       │
# │                                   │
# │   [1] ──► DICTIONARY             │
# │             │                     │
# │             ├─ name → Small...    │
# │             ├─ employees → 3      │
# │             ├─ ceo → None         │
# │             └─ rating → 4.3       │
# └───────────────────────────────────┘
