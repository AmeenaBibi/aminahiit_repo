# question 1
def cal_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = cal_bmi(weight, height)
# print("Your BMI is: ", bmi)
print()

# question 2
# def character_count(name):
#     character_count = len(name) 
#     return character_count

# name = input("Your name: ")
# count = character_count(name)
# sentemce = f"The number of characters in the users name is {count}."
# print(sentemce)
