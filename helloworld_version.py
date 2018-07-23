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
# [1,2,3,4,5]
# Ranges
# range(10)
# Tuples
# (1,2,3,4,5)
# Dictionary
# ("x":1, "y":2)


pw = input("Enter your name: ")
print(pw)
