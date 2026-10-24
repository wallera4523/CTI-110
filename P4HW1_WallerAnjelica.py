# Anjelica Waller
# 10/21/26
# P4HW1
# A program that uses while and for loops to calculate an average from a list of scores.

"""
Create a program that calculates an average of a list of scores input by the user.
The program will prompt the user to enter how many scores they would like to input.
The program will then prompt the user to input the scores, using a loop.
Each time a score is input, the program will verify that the input is valid.
If the input is valid, the program will add the number to a list. If the number is invalid, the program will
display an error message and prompt the user to input a valid number to continue.
Once all the numbers have been input, the program will find the lowest grade, print a modified list omitting the lowest grade,
the average grade, as well as a letter grade.
"""

grades = []
run_again = 'yes'
while run_again != 'no':
    total_scores = int(input("How many scores do you want to enter? "))
    if total_scores <= 0:
        print("Invalid input")
        
    
    while run_again != 'no':
        for i in range (1, total_scores+1):
            grade = float(input(f"Enter grade for module {i}: "))
            grades.append(grade)

            if grade < 0:
                print()
                print(f"Invalid input. Enter grade for module {i} again.")
                grades.remove(min(grades))
                grade_correction = float(input(f"Score is invalid! Reenter score for module {i}: "))
                grades.append(grade_correction)
            
    
        lowest_grade = min(grades)
        grades.remove(min(grades))
        modified_sum = sum(grades)
        modified_average = modified_sum / len(grades)


        if modified_average >= 90:
            letter_grade = 'A'
        elif modified_average >= 80:
            letter_grade = 'B'
        elif modified_average >= 70:
            letter_grade = 'C'
        elif modified_average >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'


        print()
        print("----------Results----------")
        print(f'{"Lowest Grade:":<18} {lowest_grade}')
        print(f'{"Modified List:":<18}', grades)
        print(f'{"Scores Average:":<18} {modified_average}')
        print(f'{"Grade: ":<18} {letter_grade}')
        print('-'*27)

        run_again = 'no' 
