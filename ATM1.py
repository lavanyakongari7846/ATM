import time

print("")
print("")
print("")
print("=============================================")
print("\tWelcome to Bank of India")
print("=============================================")
print("")
time.sleep(2)
print("\tPlease insert your card .....")
time.sleep(2)
print("")
print("Card insert successfully, Do not remove card.")
print("")
time.sleep(2)
pwd = 9090
print("=============================================")
pin = int(input("\tPlease enter your pin :"))
print("----------------------------------------------")
balance = 50000
while (True):
  if pin == pwd:
    print("""
              TRANSACTION 
        ***********************
            Menu:
            1.Check Balance
            2.Account Details
            3.Withdraw Amount
            4.Deposite Balance
            5.Exit
        ***********************
        """)
   
    print("")
    try:
      option = int(input("\tPlease enter your choice :"))
      print("\t---------------------------")

    except:
      print("\tPlease enter the valid choice:")

    if option == 1:
      print(f"\n\tYour current balance is {balance}")
      print("=============================================")

    elif option ==2:
      print("\n\tAccount Holder   : Lavanya Kongari")
      print("\tAcccount Number. : 3345442679")
      print("=============================================")

    elif option == 3:
      withdraw_amount = int(input("\n\tplease enter withdraw amount :"))
      balance = balance - withdraw_amount
      print(f"\t{withdraw_amount} is debited from your account")
      print(f"\tYour updated current balance is {balance}")
      print("=============================================")

    elif option == 4:
      deposite_amount = int(input("\n\tplease enter withdraw amount :"))
      balance = balance + deposite_amount
      print(f"\t{deposite_amount} is credited in your account")
      print(f"\tyour updated current balance is {balance}")
      print("=============================================")

    elif option == 5:
         print(f"""
        printing receipt..............
                
  ------------------------------------------
      Transaction is now complete.                         
      Transaction Number: 23456789 
      Account Holder    : Lavanya Kongari                 
      Account Number    : 3345442679             
      Available Balance : {balance}                    
 
      Thanks for choosing us as your bank.                 
  ------------------------------------------
          """)
         print("\t\tVisit again...!")
         print("=============================================")
         break

  else: 
    print("")
    print("   Please enter the valid pin try again...!   ")
    print("=============================================")
    break