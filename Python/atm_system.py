correct_pin=1234  # Original PIN
balance = 1000 # Current Balance
attempt=0 # No.of attempts

while attempt < 3: # Checking No.of attempts upto 3 time
    
    pin=int(input("Enter your PIN: ")) # asking user for enter PIN
    
    if correct_pin == pin: # checking the original PIN and entered PIN are same
        
        while True: # If PIN is correct Show the Menu page
            
                print("=====ATM MENU=====")
                print("1. Check Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Exit")
                
                choice = int(input("Enter choice: ")) # asking to choose a option from menu
                
                match choice:
                    
                    case 1: # check balance option
                        print(f"Current balance: {balance}")
                        
                    case 2: # withdraw option
                        withdraw_amount = int(input("Enter amount: "))  # asking user to enter the withdraw amount
                        
                        if balance < withdraw_amount: # checking that withdraw amount is less than the balance if not print insufficient balance
                            print("Insufficient funds")
                            
                        else:
                            balance = balance - withdraw_amount # subtracting the withdraw amount from balance and printing the remaining balance
                            if withdraw_amount <= 0:
                                print("Invalid amount")
                            else:
                                print(f"Withdraw successful. New balance: {balance}")
                            
                    case 3: # deposit option
                        deposit_amount = int(input("Enter amount: ")) # asking deposit amount
                        if deposit_amount <= 0:
                            print("Invalid amount")
                        else:
                            balance = balance + deposit_amount # adding deposit amount and printing balance amount
                            print(f"Deposit successful. New balance: {balance}")
                        
                    case 4: # exit option
                        print("Thank you. Goodbye!")
                        break# exit the program
                        
                    case _: # invalid option
                        print("Invalid choice.")
                        
    else:
        attempt+=1 # increasing attempt count when it is wrong
        
if attempt == 3: # checking no.of attempt and blocking the card if attempt equal to 3
    print("Card blocked")
