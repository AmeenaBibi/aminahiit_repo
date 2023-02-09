def main():
    x, y = "", ""
    while x <= "" and y <= "":
        x = input("Enter a number: ")
        y = input("Enter a second number: ")
    x, y = int(x), int(y)
    added(x, y)

def added(x, y):
    print(f"the sum of {x} + {y} = {x+y}")

main() 