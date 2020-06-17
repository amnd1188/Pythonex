#reading and converting
name = input('Enter:')
print(name)

x = input('Enter:')
x = int(x) - 10
print(x)

#string
fruit = "banana"
letter = fruit[0]
print(letter)
y = 5
x = fruit[y - 1]
print(x)

#length of string
color = "yellow"
c = len(color)
print(c)

#looping through string
fruit = "apple"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
