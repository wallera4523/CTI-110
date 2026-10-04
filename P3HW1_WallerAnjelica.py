# Anjelica Waller
# 9/26/26
# P3HW1
# Debugging


# This program takes a number grade , determines average and displays letter grade for average.

# Correct names of variables 

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# calculate lowest, highest, sum and average of grades in list
low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)

# determine letter grade for average using if/elif/else statements


if avg >= 90:
    letter_grade = 'A'
elif avg >= 80:
    letter_grade = 'B'
elif avg >= 70:
    letter_grade = 'C'
elif avg >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'


# Print results to user

print("------------Results------------")
print(f'{"Lowest Grade:":<18} {low:>5.2f}')
print(f'{"Highest Grade:":<18} {high:>5.2f}')
print(f'{"Sum of Grades:":<18} {sum:>5.1f}')
print(f'{"Average Grade:":<18} {avg:>5.2f}')
print('-'*31)
print(f'{"Your grade is:":<18} {letter_grade:>1}')