balance = 20000
cardPass = "0000"
attempt = 0

print("--------------------- Meezan Bank ---------------------")
print("")

while attempt < 3:
    print("If password is incorrect in 3 tries, your card will be captured.")
    print("-------------------------------------------------------")
    
    passw = input("Enter Your Card Pass : ")
    
    if passw == cardPass:
        print("-------------------------------------------------------")
        print("Login Successful!")
        print("-------------------------------------------------------")
        
        while True:
            print(" 1) Check Balance")
            print(" 2) Cash Withdrawal")
            print(" 3) Cash Transfer")
            print(" 4) Exit")
            print("-------------------------------------------------------")
            
            number = input("Select any given option : ")
            print("-------------------------------------------------------")
            
            if number == "1":
                print(f"Your account Balance is : Rs. {balance}")
                print("-------------------------------------------------------")
                
            elif number == "2":
                print("Available Withdrawal Amounts:")
                print(" 1)  1000 \n 2)  3000 \n 3)  5000 \n 4) 10000 \n 5) 15000 \n 6) 20000 \n 7) Other Amounts ")
                print("-------------------------------------------------------")
                
                choice = input("Select option : ")
                
                if choice == "1":
                    withdraw_amount = 1000
                elif choice == "2":
                    withdraw_amount = 3000
                elif choice == "3":
                    withdraw_amount = 5000
                elif choice == "4":
                    withdraw_amount = 10000
                elif choice == "5":
                    withdraw_amount = 15000
                elif choice == "6":
                    withdraw_amount = 20000
                elif choice == "7":
                    withdraw_amount = int(input("Enter custom amount : "))
                else:
                    print("Invalid option!")
                    print("-------------------------------------------------------")
                    continue
                               
                if withdraw_amount <= balance and withdraw_amount > 0:
                    remBal = balance - withdraw_amount
                    print(f"Collect your Cash : Rs. {withdraw_amount}")
                    print(f"Remaining Balance : Rs. {remBal}")
                    balance = remBal
                    print("-------------------------------------------------------")
                else:
                    print("Don't have enough amount or Invalid Amount")
                    print("-------------------------------------------------------")
                    
            elif number == "3":
                accNum = input("Enter Account number to transfer funds : ")
                amountToTransfer = int(input("Enter Amount to transfer : "))
                
                if amountToTransfer <= balance and amountToTransfer > 0:
                    remBal = balance - amountToTransfer
                    print(f"Amount Rs.{amountToTransfer} Transfered to AccNo: {accNum}")
                    print(f"Remaining Balance : Rs.{remBal}")
                    balance = remBal
                    print("-------------------------------------------------------")
                else:
                    print("Don't have enough amount or Invalid Amount")
                    print("-------------------------------------------------------")
                    
            elif number == "4":
                print("Thank you for using Meezan Bank ATM. Goodbye!")
                print("-------------------------------------------------------")
                break
                
            else:
                print("Please choose given options only (1-4)")
                print("-------------------------------------------------------")
                       
            if number != "4":
                continue_choice = input("Do you want to continue? (y/n): ").lower()
                if continue_choice != 'y':
                    print("Thank you for using Meezan Bank ATM. Goodbye!")
                    print("-------------------------------------------------------")
                    break
                    
        break  
        
    else:
        attempt += 1
        print("Wrong Password, Try again")
        print(f"Tries done : {attempt}/3")
        print("-------------------------------------------------------")

if attempt == 3:
    print("Too many wrong attempts. Your card has been captured.")
    print("-------------------------------------------------------")