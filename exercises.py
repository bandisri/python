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

def exercise13():
    userInput = input("Enter Fibonnaci series length: ")
    fibSeries = []
    fibSeries.append(1)
    fibSeries.append(1)
    if userInput.isdigit():
        for n in range(2,int(userInput)):
            fibSeries.append(fibSeries[n-2] + fibSeries[n-1])

    print(fibSeries)

def exercise14():
    a = [1, 1, 2, 3, 5, 8, 8, 13, 21, 21, 34, 55, 89]
    print('Actual list {}'.format(a))

    # b = list()
    # for i in a:
    #     if not i in b:
    #         b.append(i)

    b = set(a)
    print('Unique list {}'.format(b))

def exercise15():
    someStr = "My name is Michele"
    outList = someStr.split(sep=" ")
    print(outList)
    outList.reverse()
    print(outList)

def exercise16():
    ualphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lalphabets = []
    numerics = [0,1,2,3,4,5,6,7,8,9]
    specials = ['#','!','@','$','%','&','(',')']

    for value in ualphabets:
        lalphabets.append(value.lower())

    # print(lalphabets)
    random.shuffle(lalphabets)
    # print(lalphabets)

    counter = 0
    password = ''
    passwordList = []
    passwordList.append(random.choice(specials))
    passwordList.append(random.choice(numerics))

    while counter < 6:
        passwordList.append(random.choice(ualphabets))
        passwordList.append(random.choice(lalphabets))
        counter+=1

    # print(passwordList)
    random.shuffle(passwordList)
    # print(passwordList)
    for value in passwordList:
        password = password + str(value)

    print('password {}'.format(password))

def exercise18():
    # Get user details..
    kidsmode = False
    newGame = False
    userName = ""

    while not newGame:
        # if userName.isspace() or len(userName)==0:
        #     # print("Your name")
        #     userName = input("Who is playing?")
        # elif userName.upper() == "DHANNUSH" or userName.upper() == "AARUSHI":
        #     print("Welcome {}".format(userName))
        #     kidsmode = True
        #     newGame = True
        #     numberofDigits = 3
        #     divisor = 100
        # else:
        #     numberofDigits = input("Choose number of digits, should be more than 1: ")
        #     if not numberofDigits.isdigit() or int(numberofDigits) < 2:
        #         print("Number of digits should be more than 1")
        #     else:
        #         newGame = True
        #         divisor = 10**(int(numberofDigits)-1)

        numberofDigits = input("Choose number of digits, should be more than 1: ")
        if not numberofDigits.isdigit() or int(numberofDigits) < 2:
            print("Number of digits should be more than 1")
        else:
            newGame = True
            divisor = 10**(int(numberofDigits)-1)

    while newGame:
        # Generate Random Number
        low = 10**(int(numberofDigits)-1)-1
        high = 10**int(numberofDigits)

        # Get Random Number in list
        randomNumber = random.randint(low,high)
        randomList = list()
        randomList = numberToList(randomNumber,divisor)

        # Play Game
        playGame = True
        userInputList = list()
        userGuess = input("Guess a {} digit number: ".format(numberofDigits))
        while playGame:
            cows = 0
            bulls = 0
            userList = list()

            # Get User input
            # userGuess = input("Guess a {} digit number: ".format(numberofDigits))
            if not userGuess.isdigit():
                playGame = False
                newGame = False

                print("System Generated Number {}: ".format(randomNumber))
                print("Your Gusses: ")
                print(userInputList)

                # if kidsmode:
                #     newGameInput = input("Do you want to play new game Y/N?")
                #     if newGameInput.upper()=="Y":
                #         newGame = True
                #         numberofDigits = 3
                #         divisor = 100
                #     else:
                #         newGame = False
            elif not int(userGuess)>low and int(userGuess)<high:
                print("Number should be between {} {}".format(low, high))
                userGuess = input("Try again, numbers between ({} {}): ".format(low, high))
            else:
                userGuessNumber = int(userGuess)
                userInputList.append(userGuessNumber)

                userList = numberToList(userGuessNumber,divisor)
                for (index,value) in enumerate(userList):
                    if value in randomList:
                        if randomList[index] == value:
                            cows+=1
                        else:
                            bulls+=1

                # Let user know..
                cowString = ""
                bullString = ""
                if cows==1:
                    cowString = "{} Cow".format(cows)
                else:
                    cowString = "{} Cows".format(cows)

                if bulls==1:
                    bullString = "{} Bull".format(bulls)
                else:
                    bullString = "{} Bulls".format(bulls)

                print("{}, {}".format(cowString,bullString))

                # Quit when user gussess correctly..
                if cows==int(numberofDigits):
                    playGame = False
                    newGame = False

                    print("You got the number right.......")
                    print("System Generated Number {}: ".format(systemGenNumber))
                    print("Your Gusses: ")
                    print(userInputList)

                    # if kidsmode:
                    #     newGameInput = input("Do you want to play new game Y/N?")
                    #     if newGameInput.upper()=="Y":
                    #         newGame = True
                    #         numberofDigits = 3
                    #         divisor = 100
                    #     else:
                    #         newGame = False
                else:
                    userGuess = input("Try again, numbers between ({} {}): ".format(low, high))


def numberToList(number,divisor):
    numberList = list()
    inputNumber = number
    inputDivisor = divisor

    while inputDivisor > 1:
        numberList.append(int(inputNumber/inputDivisor))
        inputNumber = inputNumber%inputDivisor
        inputDivisor/=10
    else:
        numberList.append(int(inputNumber/inputDivisor))

    return numberList

def main():
    exercise18()

if __name__ == '__main__':
    main()
