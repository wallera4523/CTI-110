# Anjelica Waller
# 9/23/2026
# P2Hw2 - List Basics
# A program that determines an average of a list of grades, as well as the highest and lowest grades in the list.

# Prompt the user to input a grade for each of the six modules

mod1_grade = float(input("Enter the grade for Module 1: "))
mod2_grade = float(input("Enter the grade for Module 2: "))
mod3_grade = float(input("Enter the grade for Module 3: "))
mod4_grade = float(input("Enter the grade for Module 4: "))
mod5_grade = float(input("Enter the grade for Module 5: "))
mod6_grade = float(input("Enter the grade for Module 6: "))

# Compile the inputs into a list of grades
module_grades = [mod1_grade, mod2_grade, mod3_grade, mod4_grade, mod5_grade, mod6_grade]

# Calculate the lowest and highest grades in the list using the min() and max() functions

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
grade_sum = sum(module_grades)
# Calculate the average of the grades by dividing the sum of the grades by the number of grades in the list.
grade_average = grade_sum / len(module_grades)

# Print the results to the user, including the lowest grade, highest grade, and average grade.

print("------------Results------------")
print(f'{"Lowest Grade:":<18} {lowest_grade:>5.2f}')
print(f'{"Highest Grade:":<18} {highest_grade:>5.2f}')
print(f'{"Sum of Grades:":<18} {grade_sum:>5.2f}')
print(f'{"Average Grade:":<18} {grade_average:>5.2f}')
print('-'*31)
