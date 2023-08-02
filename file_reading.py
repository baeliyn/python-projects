#r read
#r+ read and write
#w write
#rb read in binary
#a append

file = open('text.txt', mode = 'r')

data = file.readline()

print(data)

file.close()

with open('new.txt', 'w') as file:
    file.write("new file")

try:
    with open('exception.txt', 'w') as file:
        file.write("no errors")
except FileNotFoundError as e:
    print(e)

with open('new.txt', 'r') as file:
    print(file.readline())