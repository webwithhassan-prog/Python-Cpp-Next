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
            print(" 1) Check Balance \n 2) Cash Withdrawal \n 3) Cash Transfer ")
            print("-------------------------------------------------------")            
            number = input("Select any given option : ")
            print("-------------------------------------------------------")            
            if number == "1":
                print(f"Your account Balance is : Rs. {balance}")
                print("-------------------------------------------------------")                
            elif number == "2":
                print("Available Amounts:")
                print("  1000     3000     5000")
                print(" 10000    15000    20000")
                print("-------------------------------------------------------")                               
                withdrawlAmount = int(input("Enter Amount : "))                
                if withdrawlAmount <= balance and withdrawlAmount > 0:
                    remBal = balance - withdrawlAmount
                    print("Collect your Cash")
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
            else:
                print("Please choose given options only (1-3)")
                print("-------------------------------------------------------")           
                continue_choice = input("Do you want to continue? (y/n): ").lower()
                if continue_choice != 'y':
                    print("Thank you for using Meezan Bank ATM. Goodbye!")
                    print("-------------------------------------------------------")
                    break
        break          
    else:
        attempt += 1
        print("Wrong Password, Try again")
        print(f"Tries done : {attempt}")
        print("-------------------------------------------------------")
if attempt == 3:
    print("Too many wrong attempts. Your card has been captured.")
    print("-------------------------------------------------------")