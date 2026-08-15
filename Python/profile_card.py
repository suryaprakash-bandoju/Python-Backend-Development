'''
A program that collects user information and displays a formatted personal profile card.
'''
name = input("Enter Your Name: ") # asking user name
age = int(input("Enter Your Age: ")) # asking user age
language = input("Enter your Favorite Programming Language: ") # asking favorite language from user
experience = int(input("Enter your Experience: ")) # asking experience of the user
goal = input("Enter your goal: ") # asking Goal of the user
current_year = 2026
started_year = current_year - experience

print("====================================================")
print("PERSONAL PROFILE CARD")
print("====================================================")

print("Name:         "+name)
print("Age:          "+age)
print("Language:     "+language)
print("Experience:   "+experience)
print("Goal:         "+goal)
print("Started:      "+str(started_year))


print("====================================================")
print("Motivation Level: HIGH")
print("====================================================")