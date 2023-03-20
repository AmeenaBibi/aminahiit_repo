from employees import Employee

def getEmployeeData(filename):
    data = []
    with open(filename, "r") as f:
        for detail in f.readlines():
            a = detail.split(',')
            data.append(Employee(a[0], a[1], int(a[2].strip('\n'))))

    return data