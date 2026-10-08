# Anjelica Waller
# 10/7/26
# P3HW2
# Calculating an employee timesheet

"""
PSEUDOCODE
Prompt the user to input the employee's name, hours worked, and pay rate.
If the hours worked is greater than 40, calculate the regular pay for 40 hours and
calculate the overtime pay for the hours worked beyond 40 at 1.5 times the pay rate.
If the hours worked is less than or equal to 40, calculate the regular pay for the hours worked.
If the hours worked is negative, display an error message indicating that the input is invalid.
Print the results in the specified format/order
"""

employee_name = input("Enter the employee's name: ")
hours_worked = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the pay rate per hour: "))

if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    total_pay = regular_pay + overtime_pay
if hours_worked < 0:
    print("Invalid input. Hours worked cannot be negative.")
if hours_worked <= 40:
    regular_hours = hours_worked
    overtime_hours = 0
    regular_pay = regular_hours * pay_rate
    overtime_pay = 0
    total_pay = regular_pay
if pay_rate < 0:
    print("Invalid input. Pay rate cannot be negative.")

print()
print("-" * 90)
print(f'Employee Name: {employee_name}')
print()
print(f"{'Hours Worked':<15} {'Pay Rate':<15} {'Overtime':<15} {'Overtime Pay':<15} {'Regular Pay':<15} {'Gross Pay':<15}")
print(f"{hours_worked:<15} ${pay_rate:<14.2f} {overtime_hours:<15} ${overtime_pay:<14.2f} ${regular_pay:<14.2f} ${total_pay:<14.2f}")

