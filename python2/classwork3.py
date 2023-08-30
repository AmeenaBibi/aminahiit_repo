# employee
def show_employee(employee_name, employee_salary):
    print(f"The name and salary of the employee is {employee_name}, {employee_salary}\n")
    
employeeName = input("Enter employee's name: ")
employeeSalary = float(input("Enter employee salary: "))
show_employee(employee_name = employeeName, employee_salary = employeeSalary)

# calculation
def calculation(x, y):
    add = x + y
    subtract = x - y
    return add, subtract

addition = int(input("Enter number: "))
subtraction = int(input("Enter number: "))
add_, subt_ = calculation(x = addition, y = subtraction)
print("Addition:", add_)
print("Subtraction:", subt_)