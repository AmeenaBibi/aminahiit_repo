no_students = int(input("Enter the number of students: "))
highest_score = 0
for i in range(no_students):
    score = int(input("Enter the score for students {}: ".format(i + 1)))
    if score > highest_score:
        highest_score = score

print("The highest score is: ", highest_score)

