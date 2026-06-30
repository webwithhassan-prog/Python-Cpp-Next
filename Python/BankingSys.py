balance = 20000
cardPass = "0000"
attempt = 0
tries = 0

print("--------------------- Meezan Bank ---------------------")
print("")

while attempt < 3:
    print("If password is incorrect in 3 tries, your card will be captured.")
    print("-------------------------------------------------------")
    
    passw = input("Enter Your Card Pass : ")
    
    if passw == cardPass:
        print("-------------------------------------------------------")
        print("1) Check Balance")
        print("2) Cash Withdrawal")
        print("3) Cash Transfer")
        print("-------------------------------------------------------")
        
        number = input("Select any given option : ")
        print("-------------------------------------------------------")
        
        if number == "1":
            print(f"Your account Balance is : Rs. {balance}")
            print("-------------------------------------------------------")
            break
            
        elif number == "2":
            print("Available Amounts:")
            print("  1000     3000     5000")
            print(" 10000    15000    20000")
            print("-------------------------------------------------------")
            
            withdrawlAmount = int(input("Enter Amount  : "))
            
            if withdrawlAmount < balance and withdrawlAmount > 0:
                remBal = balance - withdrawlAmount
                print(f"Collect your Cash")
                print(f"Remaining Balance : Rs. {remBal}")
                print("-------------------------------------------------------")
                break
            else:
                print("Don't have enough amount or Invalid Amount")
                print("-------------------------------------------------------")
                break
                
        elif number == "3":
            accNum = input("Enter Account number to transfer funds : ")
            amountToTransfer = int(input("Enter Amount to transfer : "))
            
            if amountToTransfer <= balance and amountToTransfer > 0:
                remBal = balance - amountToTransfer
                print(f"Amount Rs.{amountToTransfer} Transfered to AccNo: {accNum}")
                print(f"Remaining Balance : Rs.{remBal}")
                print("-------------------------------------------------------")
                break
            else:
                print("Don't have enough amount")
                print("-------------------------------------------------------")
                break
                
        else:
            print("Please choose given options only")
            print("-------------------------------------------------------")
            
    else:
        attempt += 1
        tries += 1
        print("Wrong Password , Try again")
        print(f"Tries done : {tries}/3")
        print("-------------------------------------------------------")

if attempt == 3:
    print("Too many wrong attempts. Your card has been captured.")
    print("-------------------------------------------------------")