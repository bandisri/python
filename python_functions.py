class Employee:
    empNo: int
    empName: str
    empDept: str

    def __init__(self, no, name, dept):
        self.empNo = no
        self.empName = name
        self.empDept = dept

    def getEmployee(self):
        return self.empNo, self.empName, self.empDept

def main():
    # someDictionary = dict(x = 1, y = 2, z = 3)
    # for value in someDictionary:
    #     print(someDictionary[value])

    employees = []
    employees.append(Employee(1234,'John','IT'))
    employees.append(Employee(2345,'Doe','IT'))
    # print(type(employees))
    print(len(employees))

    for employee in employees:
        print(employee.empNo)

if __name__ == '__main__':
    main()
