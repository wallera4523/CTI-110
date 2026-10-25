# Anjelica Waller
# 10/24/26
# P4HW2
# Calculating an employee timesheet, this time with loops

"""
PSEUDOCODE

Set up the loop and main variables of the program
Use the first while loop for employee name/loop status. Entering a name continues the loop,
typing 'Done' ends the loop and prints the accumulative regular, overtime, and gross pay.
Use a second while loop for the case of an input other than 'Done'
Use the code from the previous assignment to calculate the hours worked, pay rate, overtime, and overtime pay.
Print the results using the same fortmatting as the previous assignment
"""

employee_name = 'placeholder'
total_overtimepay = []
total_regpay = []
total_grosspay = []

total_employees = 0

while employee_name != 'Done':
    employee_name = input("Enter an employee name or type 'Done' to terminate program: ")
    if employee_name == 'Done':
        print()
        print(f'{"Total number of employees entered: "} {total_employees}')
        print(f'{"Total amount paid for overtime: $"}{(sum(total_overtimepay))}')
        print(f'{"Total amount paid for regular hours: $"}{(sum(total_regpay))}')
        print(f'{"Total amount paid in gross: $"}{(sum(total_grosspay))}')
        break
    if employee_name != 'Done':
        total_employees +=1

        while employee_name != 'Done':
            hours_worked = float(input("Enter the number of hours worked: "))
            pay_rate = float(input("Enter the pay rate per hour: "))
            if hours_worked > 40:
                regular_hours = 40
                overtime_hours = hours_worked - 40
                regular_pay = regular_hours * pay_rate
                overtime_pay = overtime_hours * pay_rate * 1.5
                total_pay = regular_pay + overtime_pay
                total_overtimepay.append(overtime_pay)
                total_regpay.append(regular_pay)
                total_grosspay.append(total_pay)
                

            if hours_worked < 0:
                print("Invalid input. Hours worked cannot be negative.")
            if hours_worked <= 40:
                regular_hours = hours_worked
                overtime_hours = 0
                regular_pay = regular_hours * pay_rate
                overtime_pay = 0
                total_pay = regular_pay
                total_regpay.append(regular_pay)
                total_grosspay.append(total_pay)


            if pay_rate < 0:
                print("Invalid input. Pay rate cannot be negative.")

            print()
            print("-" * 90)
            print(f'Employee Name: {employee_name}')
            print()
            print(f"{'Hours Worked':<15} {'Pay Rate':<15} {'Overtime':<15} {'Overtime Pay':<15} {'Regular Pay':<15} {'Gross Pay':<15}")
            print(f"{hours_worked:<15} ${pay_rate:<14.2f} {overtime_hours:<15} ${overtime_pay:<14.2f} ${regular_pay:<14.2f} ${total_pay:<14.2f}")
            break



