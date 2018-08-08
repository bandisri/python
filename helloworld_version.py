#!/usr/bin/env python3

import platform

print("This is Python version {}".format(platform.python_version()))


if 1 == 2:
    print("This is insane")
else:
    print("There is still some sanity")

counter = 10
while(counter >= 0):
    print(counter)
    counter -= 1

inputName = "John Doe"
def writeName():
    print("My Name is {}".format(inputName))


writeName()


x = 'some string'
print(x.find('ring',0))

#Sequence type
# Lists
# natNumbers = [1,2,3,4,5]
# for number in natNumbers:
#     print(number)

# Ranges
# for value in range(10):
#     if value % 2 == 0:
#         print(value)

# Tuples
# someTuple = (1,2,3,4,5)
# for value in someTuple:
#     print(value)

# Dictionary
someDict = {'x':1, 'y':2}
print('Dictonary Value {}'.format(someDict['x']))
for k, v in someDict.items():
    print(k)

# pw = input("Enter your name: ")
# print(pw)
