import random
import math

def main():
    print("Hit 'E' to exit")
    gussedNumber = input("Guess Number between 1 - 100: ")

    while gussedNumber.upper() != 'E':
        if gussedNumber.isdigit() and ( int(gussedNumber) > 0 and int(gussedNumber) <= 100 ):
            generatedNumber = random.randint(1,10)
            if int(gussedNumber) == generatedNumber:
                print("Guess is correct!!!!!")
            else:
                print("Wrong Guess, number is {}".format(generatedNumber))
        else:
            print('XXXXXXX - Check your input - XXXXXXX')

        gussedNumber = input("Guess another number?")

    else:
        print("Exiting program...........")

if __name__ == '__main__':
    main()
