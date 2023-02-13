def main():
    x, y, op = "", "", ""
    while x <= "" and y <= "" and op != "+" and op != "-" and op != "*" and op != "/" and op != "%":
        x = input("Enter a number: ")
        y = input("Enter a second number: ")
        op = input("Enter operator: ")
   
    x, y = int(x), int(y)    
    if op == "+":
        added(x, y)
    elif op == "-":
        subed(x, y)
    elif op == "/":
        print("pass in your div finction")

def added(x, y):
    print(f"the sum of {x} + {y} = {x+y}")

def subed(x, y):
    print(f"the sum of {x} - {y} = {x-y}")
    

main() 