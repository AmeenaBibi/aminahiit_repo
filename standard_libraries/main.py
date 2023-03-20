from employee_data import getEmployeeData
def main():
    totalOfStaffSalary = 0
    staff_data = getEmployeeData('name2.txt')
    for data in staff_data:
        totalOfStaffSalary += data.salary

    return totalOfStaffSalary/(len(staff_data))

print(main())