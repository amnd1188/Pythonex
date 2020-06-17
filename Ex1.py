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

#looping and counting
word = "coconut"
count = 0
for letter in word:
    if letter == 'o':
        count = count + 1
print(count)

#slicing string
s = "useful python"
print(s[0:3])

print(s[4:5])

print(s[:5])

print(s[7:])

print(s[:])

#string concatenation
x = "hello"
y = "python"
print(x + ' ' + y)

#logical operator
fruit = "banana"
'n' in fruit
'h' in fruit
'ban' in fruit

"""if 'nan' in fruit:
    print('found it!')"""

#string library,lower()
greeting = "Hello Bob"
x = greeting.lower()
print(x)
print('Hi There'.lower())

#searching string,find()
fruit = "banana"
position = fruit.find('na')
print(position)

c = fruit.find('z')
print(c)

#search and replace,replace()
greeting = "Hello Bob"
x = greeting.replace('Bob','Jane')
print(x)
nst = greeting.replace('o','y')
print(nst)
