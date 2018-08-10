import sys
import datetime
import random

def exercise1():
    name = input("Your Name: ")
    if name is '' or name.isspace():
        print("Name is blank")
        exit()

    age = input("Your Age: ")
    if not age.isdigit():
        print("Age should be numbers")
        exit()

    copies = input("Enter copies of output: ")
    if not copies.isdigit():
        print("Copies should be numeric value")
        exit()

    currentYear = datetime.datetime.now().year
    centuryYear = currentYear + (100 - int(age))

    for value in range(int(copies)):
        print("You will turn 100 years old in the year, {}".format(centuryYear))

def exercise2():
    userInput = input("Enter a number: ")
    if not userInput.isdigit():
        print("Enter a number")
        exit()

    if int(userInput) % 2 == 0:
        print("Its an Even number")
    else:
        print("Entered an Odd Number")

def exercise3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print("Sample List {}".format(a))

    userSelecton = input("Enter a number from list: ")
    # for x in a:
    #     if x < 5:
    #         print(x)

    newList = [x for x in a if x < int(userSelecton) and int(userSelecton) in a]
    print(newList)

def exercise4():
    userInput = input("Enter a number: ")
    if not userInput.isdigit():
        print("Input should be a number")
        exit()

    divisorList = []
    for i in range(2, int(userInput)):
        if int(userInput) % i == 0:
            divisorList.append(i)
    print(divisorList)
    return divisorList

def exercise5():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # aset = set(a)
    # bset = set(b)
    #
    # newset = aset.intersection(bset)
    newset = set(a).intersection(set(b))
    print(newset)

def exercise6():
    userInput = input("Enter a string: ")
    # iset = set(userInput)
    # print(iset)

    ilist = list(userInput)
    ipal = list(userInput)

    ipal.reverse()
    isPalindrome = True

    print(ilist, ipal)

    for (index,i) in enumerate(ilist):
        # print(index,i)
        if ilist[index] == ipal[index]:
            continue
        else:
            isPalindrome = False

    print(isPalindrome)

def exercise7():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print("Current List {}".format(a))

    evens = [x for x in a if x % 2 == 0]
    print("New List, only evens {}".format(evens))

def exercise8():
    seq = ['rock', 'paper', 'scissors']

    play = True
    while play:
        # print('1.Rock', '2.Paper', '3.Scissors')
        for (index,value) in enumerate(seq):
            print("{}.{}".format(index+1, value))

        # userChoice = input(str(seq)+':')
        userChoice = input("Your choice enter number: ")
        if not userChoice.isdigit() or int(userChoice) > 3:
            play = False
            exit()

        userChoice = seq[int(userChoice)]
        randChoice = random.choice(seq)

        print("=====================================================")
        print("Your choice: {}".format(userChoice))
        print("My Choice: {}".format(randChoice))

        # if userChoice.upper() == 'EXIT':
        #     play = False
        #     exit()

        userWins = False
        if userChoice == randChoice:
            print('Go Again...')
            # exit()
        else:
            if userChoice == 'rock' and randChoice == 'scissors':
                userWins = True
            elif userChoice == 'scissors' and randChoice == 'paper':
                userWins = True
            elif userChoice == 'paper' and randChoice == 'rock':
                userWins = True

            if userWins:
                print("You Win!!!")
            else:
                print("I win!!!")
        print("=====================================================")

def exercise9():
    playGame = True
    totalGusses = 0

    while playGame:
        print("Enter 0 anytime to EXIT")
        userGuess = input("Guess number between 1 - 9: ")
        if not userGuess.isdigit() or int(userGuess) == 0:
            playGame = False
        else:
            randomGuess = random.randint(1,9)

            print("Your guess {}".format(userGuess))
            print("System {}".format(randomGuess))

            diff = int(userGuess) - int(randomGuess)
            if diff == 0:
                print("Correct guess")
            elif diff > 0:
                print("Guess too high {}".format(diff))
            else:
                print("Guess too low {}".format(diff))

            totalGusses+=1
    else:
        print("Total Number of Gusses {}".format(totalGusses))

def exercise11():
    divList = exercise4()
    if len(divList) > 0:
        print("Not prime")
    else:
        print("Prime number")

def exercise12():
    listLength = random.randint(10,20)
    randomList = random.sample(range(100),listLength)
    print(randomList)

    newList = []
    newList.append(randomList[0])
    newList.append(randomList[len(randomList)-1])

    print(newList)

def main():
    exercise12()

if __name__ == '__main__':
    main()
