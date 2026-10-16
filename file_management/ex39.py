# local scope
# global scope

x = "global scope"


def myFunc():
    x = "local scope"
    print(x)  # local scope


myFunc()
print(x)  # global scope

name = "Eda"


def change_name(new_name):
    global name
    name = new_name
    print(new_name)
    name = "Nehir"
    print(name)  # Nehir


change_name("Gül")
print(name)  # global name has changed

name = "global string"


def greeting():
    name = "Emre"

    def hello():
        print("Hello", name)  # Hello Emre -> global string

    hello()


greeting()

x = 50


def test(x):
    x = 100
    print(f"x: {x}")  # x: 100


test(x)
print("x: " + str(x))  # x: 50
