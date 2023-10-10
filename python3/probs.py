numbers = input("Enter numbers separeated by commas: ")
user_input = numbers.split(",")
list_numbers = []
for _input in user_input:
    list_numbers.append(int(_input))

maximun_numbers = max(numbers)
minimum_numbers = min(numbers)

print(f"The maximum number is {maximun_numbers} and the minimun number is {minimum_numbers}")