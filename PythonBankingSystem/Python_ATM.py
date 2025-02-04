# Importing Libraries
import os

# Main menu function
def MainMenu(Balance):
    print("****************************")
    print("*  Python Banking System   *")
    print("*                          *")
    print("*  1. Check Balance        *")
    print("*  2. Deposit              *")
    print("*  3. Withdrawal           *")
    print("*  4. Transfer             *")
    print("*  5. Credit               *")
    print("*  6. Loan                 *")
    print("*  7. Easy-Pay             *")
    print("*                          *")
    print("*  8. Exit                 *")
    print("*                          *")
    print("****************************")
    # Prompting the user for an option
    option = input("Enter option: ")
    
    # Checking if the user input is an integer
    try:

        # Converts the user's input into an integer "user_option".
        user_option = int(option)

        # Conditional statement to check if the user's input is 
        # in the interval 0 < user_option <= 8.
        if 0 < user_option <=8:
            pass
        else:
            print("WARNING: Option not valid!")
    except:
        print(":: WARNING! :: Wrong Values Entered!")
        MainMenu(Balance)
    
    # Conditional statements to orderly call upon 
    # the function of each respective transaction.
    if(option =="1"):
        CheckingBalance(Balance)
    elif(option =="2"):
        Deposit(Balance, "Deposit")
    elif(option =="3"):
        Withdrawal(Balance, "Withdrawal")
    elif(option =="4"):
        Transfer(Balance, "Transfer")
    elif(option =="5"):
        Voucher(Balance, "Voucher")
    elif(option =="6"):
        print("Unavailable atm :(")
    elif(option =="7"):
        print("Unavailable atm :(")
    elif(option =="8"):
        ThankYouMessage()

# Menu function for both Withdrawal and Deposit functions.
def MenuFunction(Balance, Transaction, code):

    if code == "The Transaction Menu":   
        print("*******************************")
        print("*    Python Banking System    *")
        print(f"*   {Transaction} Menu       *")
        print("*                             *")
        print("*    1. $20         4. $150   *")
        print("*    2. $50         5. $250   *")
        print("*    3. $100        6. $500   *")
        print("*        7. Other amount      *")
        print("*       8. Back     9. Exit   *")
        print("*******************************")

    elif code == "The New Balance Display":
        print("******************************************")
        print("*      Python Banking System             *")
        print("*                                        *")
        print(f"*      New Balance: ${Balance}          *")
        print("******************************************")


# Another Transaction function
def AnotherTransaction(Balance):
    print("\n")
    print("**********************************")
    print("*   Python Banking System        *")
    print("*                                *")
    print("*   Would You Like To Perform    *")
    print("*   Another Transaction? (y/n)   *")
    print("*                                *")
    print("**********************************")
    
    answer = input("Enter answer (yes -> y, no -> n): ")
    if(answer == "y" or answer == "n"):    
        if(answer == "y"):
            MainMenu(Balance)
        elif(answer == "n"):
            ThankYouMessage()
    else:
        print("\nWARNING: You Entered Other Characters!")
        AnotherTransaction(Balance)

# Thank You Message function
def ThankYouMessage():
    print("\n")
    print("**********************************")
    print("*   Python Banking System        *")
    print("*                                *")
    print("*   Thank You For Banking With   *")
    print("*   Us :)  :)                    *")
    print("**********************************")
#=======================================================================================
#
#
#
#
#
#=======================================================================================
# LISTED BELOW ARE THE TRANSACTION FUNCTIONS
#=======================================================================================
#
#
#
#
#
#=======================================================================================
# 1. Check Balance function: To check current balance or available balances.
def CheckingBalance(Balance):
    os.system('cls')
    print("***************************************")
    print("*   Python Banking System             *")
    print("*                                     *")
    print(f"*  Current Balance: ${Balance}.00    *")
    print("***************************************")
    AnotherTransaction(Balance)
#=======================================================================================
#
#
#
#
#
#=======================================================================================
# 2. Deposit function: For Deposit Transactions
def Deposit(Balance, Transaction):

    # Calling the menu function
    MenuFunction(Balance, Transaction, "The Transaction Menu")

    # Prompting the user to enter an option
    option = input("Enter option: ")

    # Error-handling to check if the input entered:
    # 1. Is an Integer.
    # 2. Is within the range of 1 to 8 ONLY.
    try:
        
        # Converts the "option" variable into an integer
        user_option = int(option)

        # Conditional statement to check if the integer 
        # entered is in the interval 0 < user_optoin <= 9.
        if 0 < user_option <= 9:
            # Passes if proves true
            pass
        
        # If the above conditional statement does not prove 
        # true, then it defaults to the action below.
        else:
            print("WARNING:: Integer Entered must be from 1 to 8!")
            Deposit(Balance)
    except:
        print("::WARNING:: Option Entered Isn't An Integer!")
        Deposit(Balance)
    
    # Conditional statements for each option. 
    # There are nine conditional statements.
    if option == "1":
        Balance +=20
    elif option == "2":
        Balance +=50    
    elif option == "3":
        Balance +=100    
    elif option == "4":
        Balance +=150    
    elif option == "5":
        Balance +=250    
    elif option == "6":
        Balance +=500    
    elif option == "7":
        amount = input("Enter amount ($): ")

        # Error handling to ensure the user enters the correct input
        try:

            # Converting the user's input to an integer
            user_entered_amount = int(amount)

            # Conditional statement checks if the amount is within the expected
            # range, and less than the available balance.
            if 500 < user_entered_amount:
                print("Processing Transaction :)")
                
                # Arithmetic to ensure the balance is incremented by the amount
                # entered by the user.
                Balance+=user_entered_amount
            else:
                
                # If the above condition is not met fails, 
                # it defaults to printing an error message then 
                print("::WARNING:: Amount either too small or too large to be withdrawn!")
                Deposit(Balance, Transaction)
        except:

            # If the above "Try" does not work, then it prints an error message
            # and afterwards the function calls itself.
            print(":: WARNING :: Value Entered Isn't/Aren't (An) Integer(s)!")
            Deposit(Balance, Transaction)

    elif option == "8":
        MainMenu(Balance)
    elif option == "9":
        ThankYouMessage()
    
    # At the end of the nine conditional statements, there's a function call
    # to MenuFunctionForWithdrawalAndDeposit to print a message that the 
    # transaction was complete and the displays the new available balance.
    MenuFunction(Balance, Transaction, "The New Balance Display")

    AnotherTransaction(Balance)
#=======================================================================================
#
#
#
#
#
#=======================================================================================
# 3. Withdrawal function
def Withdrawal(Balance, Transaction):
    # Calling the menu function
    MenuFunction(Balance, Transaction, "The Transaction Menu")

    # Prompting the user to enter an option
    option = input("Enter option: ")

    # Error-handling to check if the input entered:
    # 1. Is an Integer.
    # 2. Is within the range of 1 to 8 ONLY.
    try:
        
        # Converts the "option" variable into an integer
        user_option = int(option)

        # Conditional statement to check if the integer 
        # entered is in the interval 0 < user_optoin <= 9.
        if 0 < user_option <= 9:
            # Passes if proves true
            pass
        
        # If the above conditional statement does not prove 
        # true, then it defaults to the action below.
        else:
            print("WARNING:: Integer Entered must be from 1 to 8!")
            Withdrawal(Balance, Transaction)
    except:
        # If the above "Try" fails, then an error message 
        # is printed and the function calls itself.
        print("::WARNING:: Option Entered Isn't An Integer!")
        Withdrawal(Balance, Transaction)
    
    # Conditional statements for each option entered
    if option == "1":
        amount = 20 
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "2":
        amount = 50
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "3":
        amount = 100
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "4":
        amount = 150
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount
    
    elif option == "5":
        amount = 200
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount
    
    elif option == "6":
        amount = 250
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "7":
        amount = input("Enter amount ($): ")
        
        # Error handling to make sure what 
        # the user enters is an integer.
        try:
            # Converts what the user entered into an integer.
            user_entered_amount = int(amount)

            # Conditional statement to  make sure the amount withdrawn isn't
            # out of the interval from 0 to 800.
            if user_entered_amount <= Balance:
                
                print("Successfully Processed Amount!")
                
                # Arithmetic, subtracting the amount the user entered from 
                # the balance/available balance.
                Balance-=user_entered_amount
            else:
                print("WARNING: Insufficient Funds!")
                Withdrawal(Balance, Transaction)
        except:
            print(":: WARNING :: Value Entered Isn't/Aren't (An) Integer(s)!")
            Withdrawal(Balance, Transaction)
    elif option == "8":
        MainMenu(Balance)
    elif option == "9":
        ThankYouMessage()
    MenuFunction(Balance, Transaction, "The New Balance Display")

    AnotherTransaction(Balance)
#=======================================================================================
#
#
#
#
#
#=======================================================================================
# 4. Transfer function
def Transfer(Balance, Transaction):
    #
    #
    #
    # Transfer Transaction Prompt for the user to enter their account to transfer money to
    print("*********************************************")
    print("*        Python  Banking  System            *")
    print("*                                           *")
    Account_Number = input("Enter Account number (8 digits/integers): ")
    print("*********************************************")

    # Error-handling to check if the user entered the correct amount.
    try:
        
        # Converting the user's input (account number) into an integer.
        IntegerCheck = int(Account_Number)

        # Checking if the user correctly entered eight digits
        if 9999999 < IntegerCheck < 100000000:
            print("\nInput Correct!\n")
        
        # if the user failed to enter eight digits or entered 0 first 
        # (minor working problem), the conditions default to this
        else:
            print("WARNING: Wrong Input! (Check if you entered a 0 first)")
    except:
        print("WARNING: Invalid Account Number!")
        Transfer(Balance, Transaction)
    #
    #
    #        
    # Displaying the Transaction Menu
    MenuFunction(Balance, Transaction, "The Transaction Menu")
    
    # Prompting the user to enter an option
    option = input("Enter option: ")

    # Error-handling to check if the input entered:
    # 1. Is an Integer.
    # 2. Is within the range of 1 to 8 ONLY.
    try:
        
        # Converts the "option" variable into an integer
        user_option = int(option)

        # Conditional statement to check if the integer 
        # entered is in the interval 0 < user_optoin <= 9.
        if 0 < user_option <= 9:
            # Passes if proves true
            pass
        
        # If the above conditional statement does not prove 
        # true, then it defaults to the action below.
        else:
            print("WARNING:: Integer Entered must be from 1 to 8!")
            Transfer(Balance, Transaction)
    except:
        # If the above "Try" fails, then an error message 
        # is printed and the function calls itself.
        print("::WARNING:: Option Entered Isn't An Integer!")
        Transfer(Balance, Transaction)
    #
    #
    #
    # Conditional statements for each amount 
    # entered per it's respective integer.
    if option == "1":
        amount = 20 
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "2":
        amount = 50
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "3":
        amount = 100
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "4":
        amount = 150
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount
    
    elif option == "5":
        amount = 200
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount
    
    elif option == "6":
        amount = 250
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "7":
        amount = input("Enter amount ($): ")
        
        # Error handling to make sure what 
        # the user enters is an integer.
        try:
            # Converts what the user entered into an integer.
            user_entered_amount = int(amount)

            # Conditional statement to  make sure the amount withdrawn isn't
            # out of the interval from 0 to 800.
            if user_entered_amount <= Balance:
                
                print("Successfully Processed Amount!")
                
                # Arithmetic, subtracting the amount the user entered from 
                # the balance/available balance.
                Balance-=user_entered_amount
            else:
                print("Amount either too small or too large to be deposited!")
                Transfer(Balance, Transaction)
        except:
            print(":: WARNING :: Value Entered Isn't/Aren't (An) Integer(s)!")
            Transfer(Balance, Transaction)
    elif option == "8":
        MainMenu(Balance)
    elif option == "9":
        ThankYouMessage()
    #
    #
    #
    MenuFunction(Balance, Transaction, "The New Balance Display")
    AnotherTransaction(Balance)
#=======================================================================================
#
#
#
#
#
#=======================================================================================
# 5. Phone-Voucher function
def Voucher(Balance, Transaction):
    
    # Displaying the voucher Menu by calling the Menu function.
    MenuFunction(Balance, Transaction, "The Transaction Menu")
    
    # Prompting the user to enter an option
    option = input("Enter option: ")

    # Error-handling to check if the input entered:
    # 1. Is an Integer.
    # 2. Is within the range of 1 to 8 ONLY.
    try:
        
        # Converts the "option" variable into an integer
        user_option = int(option)

        # Conditional statement to check if the integer 
        # entered is in the interval 0 < user_optoin <= 9.
        if 0 < user_option <= 9:
            # Passes if proves true
            pass
        
        # If the above conditional statement does not prove 
        # true, then it defaults to the action below.
        else:
            print("WARNING:: Integer Entered must be from 1 to 9!")
            Voucher(Balance, Transaction)
    except:
        # If the above "Try" fails, then an error message 
        # is printed and the function calls itself.
        print("::WARNING:: Option Entered Isn't An Integer!")
        Voucher(Balance, Transaction)
    #
    #
    #
    # Conditional statements for each amount 
    # entered per it's respective integer.
    if option == "1":
        amount = 20 
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "2":
        amount = 50
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "3":
        amount = 100
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "4":
        amount = 150
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount
    
    elif option == "5":
        amount = 250
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount
    
    elif option == "6":
        amount = 500
        if amount > Balance:
            print("WARNING: Insufficient Funds!")
        else:
            Balance-=amount

    elif option == "7":
        amount = input("Enter amount ($): ")
        
        # Error handling to make sure what 
        # the user enters is an integer.
        try:
            # Converts what the user entered into an integer.
            user_entered_amount = int(amount)

            # Conditional statement to  make sure the amount withdrawn isn't
            # out of the interval from 0 to 800.
            if user_entered_amount <= Balance:
                
                print("Successfully Processed Amount!")
                
                # Arithmetic, subtracting the amount the user entered from 
                # the balance/available balance.
                Balance-=user_entered_amount
            else:
                print("Amount either too small or too large to be deposited!")
                Voucher(Balance, Transaction)
        except:
            print(":: WARNING :: Value Entered Isn't/Aren't (An) Integer(s)!")
            Voucher(Balance, Transaction)
    elif option == "8":
        MainMenu(Balance)
    elif option == "9":
        ThankYouMessage()
    #
    #
    #
    MenuFunction(Balance, Transaction, "The New Balance Display")
    AnotherTransaction(Balance)
#=======================================================================================
#
#
#
#
#
#=======================================================================================
# 6. Loan function



#=======================================================================================
#
#
#
#
#
#=======================================================================================
# 7. Power Bill function

# START OF PROGRAM: Calling the Menu function.
Balance = int(1000)
MainMenu(Balance)

# Problems faced with the code:
# 1. || Exit Problem ||: When asking the user if they'd 
#    like to perform another transaction, the program
#    mistakenly displays the balance 
#    again and asks the user again if they'd 
#    like to perform another transaction. Looking for a solution.
#
# 2. || Spacing Problem ||: in printing things like Balances and Strings, there is
#    often uneven spacing between what is being printed. The goal is to have 
#    things printed evenly.
#
# 3. || Usage of Clear Names for Functions ||: Name the MenuFunction properly.
#
# 4. || Spacing in the Menus ||: Better presentation for the printouts.
#
# 5. || 