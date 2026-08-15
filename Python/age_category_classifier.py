'''
A program to categorize the ages from the User input
'''

age = int(input("Enter your Age: "))
if age < 0:
    print("Invalid input. Age cannot be negative.")
elif age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")