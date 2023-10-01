class Employee:
    # constructor
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name

    # if we need to define function to pass self argument first
    def getsalary(self):
        return self.name + " " + str(self.salary)


obj = Employee(89776, "Abdul")
print(obj.getsalary())
