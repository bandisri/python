# print('Hello World!! Python Programming')
# def adding2Numbers(arg1, arg2):
#     return arg1 + arg2
#
# print(__name__)
# print(__package__)
#
# print(adding2Numbers(10,20))
#
# ages = [12,20,30,12,50]
#
# for age in ages:
#     print age
#
#
# for (counter, age) in enumerate(ages):
#     print(counter, age)

from datetime import date
from datetime import time
from datetime import datetime

def main():
    currentDate = date.today()
    print("Current Date", currentDate)
    print("Day", currentDate.day)
    print("Month", currentDate.month)
    print("Year", currentDate.year)

if __name__ == '__main__':
    main()
