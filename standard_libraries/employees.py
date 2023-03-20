class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def displayEmployeeInfo(self):
        return f"Employee's name is {self.name}, department is {self.department}, salary is {self.salary}"
    
    def __str__(self):
        return f"Employee's name is {self.name}, department is {self.department}, salary is {self.salary}"
 