# Variable number of parameters: Kwargs (Key word argument) dictionary type


def display_user(*args):
    print(type(args))  # <class 'tuple'>
    print(args)


display_user()


def display_user(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)

    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")

# username: edagul
# email: abcd


display_user()
# {'username': 'edagul', 'email': 'abcd'}
display_user(username="edagul", email="abcd")


def myFunc(a, b, c, *args, **kwargs):
    print(a, b, c, args, kwargs)


myFunc(10, 20, 30, 40, 50, 60, key1="value1", key2="value2")
# 10 20 30 (40, 50, 60) {'key1': 'value1', 'key2': 'value2'}
