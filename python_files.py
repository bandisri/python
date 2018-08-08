import python_print

def main():
    f = open('IBCMU7_20180709170030.txt')
    for line in f:
        python_print.smartprint(line.rstrip())
        # print(line.rstrip())

if __name__ == '__main__':
    main()
