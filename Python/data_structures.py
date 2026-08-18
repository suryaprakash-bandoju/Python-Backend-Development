# Exercise 3.1: String Manipulation
email = " Alice.Smith@EXAMPLE.COM"

clean_email =  email.strip().lower()
print(clean_email)

Username = clean_email.split('@')[0]
print(Username)

ends_with_com = clean_email.endswith(".com")
print(ends_with_com)

# Exercise 3.2: List Operations
tasks = ["login", "register", "logout"]

tasks.append("delete_account")
tasks.insert(1,"Update_profile")
tasks.remove("register")
for task in tasks:
    print(task.upper())
    
    
# Exercise 3.3: Dictionary CRUD
diction = {"name" : "surya" ,"price" : 299,"quantity" : 2}
diction["category"] = "Electronics"
diction["price"] *= 1.10

for key, value in diction.items():
    print(f"{key}: {value}")
    
    
# Exercise 3.4: Nested Data
students = [
    {"name": "Alice", "marks": [85, 90, 78]},
    {"name": "Bob", "marks": [72, 88, 91]},
]
avg = 0
for student in students:
    name = student["name"]
    marks_list = student["marks"]
    l = len(marks_list)
    total = sum(marks_list)
    avg = total / l
    print(name,round(avg,2))
    
    
# # Exercise 3.5: Set Operations
# allowed_ips = {"192.168.1.1", "10.0.0.5", "172.16.0.1"}
# blocked_ips = {"10.0.0.5", "203.0.113.0"}

# print(allowed_ips.difference(blocked_ips))
