# loop 
for num in range(0, 501, 2):
    print(num)

# BMI calculator
from week1assign import bmi
def cal_bmi():

    if bmi < 18.5:
        result = "Underweight"
    elif 18.5 <= bmi < 25:
        result = "Normal weight"
    elif 25 <= bmi < 30:
        result = "Overweight"
    elif 30 <= bmi < 35:
        result = "Obese"
    else:
        result = "Clinically obese"
    return bmi, result 

bmi, result = cal_bmi()
print(f"Your BMI is: {bmi:2f}")
print(f"Interpretation: {result}")
cal_bmi()