import math;
import random;

def main():
    answer = 'Y'
    while answer.upper() == 'Y':
        answer = input("Do you want to roll dice again (Y/N)?")
        if answer.upper() == 'Y':
            print(random.randint(1,6))

if __name__ == '__main__':
    main()
