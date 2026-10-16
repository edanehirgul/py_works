"""

file = open("log.txt",encoding="utf-8")

# For turkish letters "utf-8"

print(file.read())

file.close()

"""

# Same operetions (dont need to delete manually)
# open(file, mode, encoding)

with open("log.txt", "w+", encoding="utf-8") as file:
    file.write("Hello World!")
    file.seek(0)  # dosyanın başına(0) döner
    print(file.read())
