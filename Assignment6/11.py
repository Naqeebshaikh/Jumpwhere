# 11. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks = float(input("Enter your marks: "))

if marks < 25:
    grade = 'F'
elif 25 <= marks < 45:
    grade = 'E'
elif 45 <= marks < 50:
    grade = 'D'
elif 50 <= marks < 60:
    grade = 'C'
elif 60 <= marks < 80:
    grade = 'B'
else:
    grade = 'A'

print("Your grade is:", grade)
