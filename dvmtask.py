# Made by - Harpreet Singh Anand, BITS ID- 2021A7PS2416P
'''In this program we have taken the balance of all the existing customers as 8000 
while the new customers have to register and have zero balance.'''


import csv
import logging
import time
logging.basicConfig(filename='atm.log', level=logging.DEBUG)
with open('name_pins.csv') as csvfile:
    data_1 = csv.reader(csvfile)
    
print("Welcome !!!")
print("Please insert your card")
time.sleep(2) # to show the time taken to read the card
print("Card inserted....")
logging.debug("Card inserted")
response1 = input("Are you an existing customer? (y/n)")


class ATM():
    
    def __init__(self):
        
        def CheckYourBalance():
            print(f"Your current balance is {self.balance}")
        
        def Withdraw():
            withdraw_amount = int(input("Please enter withdrawal amount "))
            if withdraw_amount <= self.balance:

                self.balance = self.balance - withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your updated balance is {self.balance}")
            else:
                print("You cannot withdraw amount greater than the deposited money")
                logging.debug("Failed to withdraw due to insufficient balance")
    
        def Deposit():
            deposit_amount = int(input("Please enter deposit_amount"))
            self.balance = self.balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your updated balance is {self.balance}")
        
        self.balance = 8000
        self.name = input("Enter your name: ")
        self.pin = int(input("Enter the four digit pin: "))
        
        with open('name_pins.csv') as csvfile:
            data = list(csv.reader(csvfile))
            print(data[2])   
            n = len(data)
            
        for i in range (1,n):
                
            if [self.name, str(self.pin)] == data[i]:
                self.balance = 8000
                print("Authentication successsful...")
                print(f"The current balance is {self.balance}")
                print('''Choose the services:
                    1 = Check Your Balance
                    2 = Withdraw
                    3 = Deposit
                    4 = Exit
                                  ''')
                
                option = int(input("Please enter your choice :"))
               
                if option == 1:
                    CheckYourBalance()
                    logging.debug("Checked the account balance")  
                elif option == 2:
                    Withdraw()
                    logging.debug("Withdrew  from the ATM")
                elif option == 3:
                    Deposit()
                    logging.debug("Deposited in the account")
                elif option == 4:
                    logging.debug("Exited the ATM service")
                    break
                else:
                    logging.debug("Invalid option entered")
                    print("Please enter a valid option")
            
            
            elif [self.name, str(self.pin)] != data[i]:
                print ('..')
                if i==n-1 and [self.name, str(self.pin)] != data[n-1]:
                    print("The name or pin is incorrect!! Please try again.")
                    logging.debug("Entered incorrect name or ping")
            
   
    
class New_Member():
    
    def __init__(self):
        
        def CheckYourBalance():
            print(f"Your current balance is {self.balance}")
        
        def Withdraw():
            withdraw_amount = int(input("please enter withdraw_amount "))
            self.balance = self.balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your updated balance is {self.balance}")
    
        def Deposit():
            deposit_amount = int(input("Please enter deposit_amount"))
            self.balance = self.balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your updated balance is {self.balance}")
        
        
        self.name = input("Enter your name: ")
        pin1 = int(input("Kindly set a four digit pin for your atm services: "))
        pin2 = int(input("Kindly re-enter the pin : "))
        
        if pin1 == pin2:
            print("Account has been successfully created")
            with open("name_pins.csv", "a", newline="") as File:
                writer = csv.writer(File)
                writer.writerow([self.name, pin1])
            
            logging.debug("Configured new name and pin in the machine")

            print("Now, enter your details again to access our services")
            self.name = input("Enter your name: ")
            self.pin = int(input("Enter the four digit pin: "))
            logging.debug("Logged into the machine with the updated name and pin ")
            with open('name_pins.csv') as csvfile:
                data = list(csv.reader(csvfile))
                print (data)
                n = len(data)
                
    
            
                for i in range (1,n) :
                

                
                    if [self.name, str(self.pin)] == data[i]:
                        self.balance = 0
                        print("authentication successsful...")
                        print(f"The current balance is {self.balance}")
                        print('''Choose the services:
                       1 = Check Your Balance
                       2 = Withdraw
                       3 = Deposit
                       4 = Exit
                                  ''')
                        try:
                    
             
                            option = int(input("Please enter your choice "))
                        except:
                            print("Please enter valid option")
        
                
                        if option == 1:
                            CheckYourBalance()
                            logging.debug("Checked the account balance")
                                        
                        elif option == 2:
                            print("Kindly deposit some amount of money before withdrawing")
                        
                            logging.debug("Failed in withdrawing due to inadequate balance")
                
                        elif option == 3:
                            Deposit()
                            logging.debug("Deposited  in the account")

                        elif option == 4:
                            logging.debug("Exited the ATM service")
                            break
                        else:
                            print("Please enter a valid option")
                            logging.debug("Invalid option entered ")
                    elif [self.name, str(self.pin)] != data[n-1]:
                        print("Invalid name or pin entered")
                        logging.debug("Entered incorrect name or pin")
                        break
    
    
        else:
            logging.debug("Failed in configuring his name and pin in the machine")
            print("The pins do not match. Kindly redo the process")
            

if response1 == 'y':
    logging.debug("An existing customer")
    ATM()

    
elif response1 == 'n':
    logging.debug("A new customer")
    New_Member()

else:
    print("Invalid response!!")
    logging.debug("Invalid response!!")
    
print("Thank You for availing our services. Have a Good Day!!!")