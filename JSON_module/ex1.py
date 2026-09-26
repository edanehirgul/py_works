# ----JavaScript Object Notation---

# --Json Types--
# String -> "Hello"
# NUmber -> 10, 10.3
# Boolean -> true, false
# null -> null
# array -> [1,2,3], ["Hello","Word"]
# Object -> {"key":"value"}, {"age": 30}

# extension -> .json
# storing data
# most likely a list other than a table
# csv -> table(strict) , json -> list

"""
{
    "key": "value",
    "favNumb" : 3,
    "isProgrammer" : true,
    "hobbies": ["Weight lifting","Bowling"],
    "friends": [{
        "name": "Joey",
        "favNumb": 100,
        "isProgrammer": False,
        "friends": [...]
    }]
}


"""

import json

with open('ex2.json', 'r') as json_file:
    data = json.load(json_file)
# data has all the things in  ex2.json -> json_file
# so u can use for loop without opening the file everytime

print(data)
# [{'name': 'Big Corporation', 'numberOfEmployees': 1000, 'ceo': 'Mary', 'rating': 3.6},
#     {'name': 'Small Startup', 'numberOfEmployees': 3, 'ceo': None, 'rating': 4.3}]

for person in data:
    print(person['name'])
# Big Corporation
# Small Startup

for person in data:
    del person['rating']
# deleted the rating pairs

new_string = json.dumps(data, indent=2,  # sort_key: alfabetik sıralama
                        sort_keys=True)  # indent: satır başı

# .dumps => pyhton -> json (string)
# .load => json -> pyhton  (string)

print(new_string)
# [{"name": "Big Corporation", "numberOfEmployees": 1000, "ceo": "Mary"},
#     {"name": "Small Startup", "numberOfEmployees": 3, "ceo": null}]

# with indent= 2
#   {
#     "name": "Big Corporation",
#     "numberOfEmployees": 1000,
#     "ceo": "Mary"
#   },
#   {
#     "name": "Small Startup",
#     "numberOfEmployees": 3,
#     "ceo": null
#   }
# ]

# with sort_keys=True : alphabetic order
#   {
#     "ceo": "Mary",
#     "name": "Big Corporation",
#     "numberOfEmployees": 1000
#   },
#   {
#     "ceo": null,
#     "name": "Small Startup",
#     "numberOfEmployees": 3
#   }
# ]
