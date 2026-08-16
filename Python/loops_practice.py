# # printing numbers from 1 to 10
# for i in range(1, 11):
#     print(i)

# # printing even numbers from 2 to 20
# for i in range(2, 21, 2):
#     print(i)

# # printing numbers from 10 to 1
# for i in range(10,0,-1):
#     print(i)

# # print 1 to 5 using while loop
# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# # Use a while loop that asks the user to enter a number. Keep asking until they enter 0. Then print "Done"


# while True:
#     n = int(input("Enter a number: "))
#     if n == 0:
#         print("Done")
#         break

# # Ask the user for a positive integer n. Use a for loop to calculate the sum of all numbers from 1 to n. Print the result.

# n = int(input("Enter a positive number: "))
# if n >=0:
#     total = 0
#     for i in range(1,n+1):
#         total += i
#     print("Sum:",total)
# else:
#     print("Invalid input. number must be positive.")


# # Ask the user for a number. Calculate its factorial using a loop.
# n = int(input("Enter a number: "))
# if n >= 0:
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
# else:
#     print("Number must be greater than zero.")


# # Set a correct password ("python123"). Ask the user to enter a password. Give them 3 attempts. If they get it right, print "Access granted" and break. If they fail 3 times, print "Account locked".

# password = "python123"
# attempt = 0
# while attempt < 3:
    
#     usrpasswd = input("Enter your Password: ")
#     if password == usrpasswd:
#         print("Access granted")
#         break
#     else:
#         attempt += 1
# else:
#     print("Account blocked")
        
    
# # Ask the user for a number. Determine if it's prime.

# n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not prime")
# elif n == 2:
#     print("Prime")
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")

n = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
    
for i in range(3,10,2):
    print(i)