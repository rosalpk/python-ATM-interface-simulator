# A simple python script for an interface for a ATM machine

#data and info
def ATM_info():
    return [
        {
            "bank_name": "MyBank",
            "location": "123 Main St, Anytown, USA",
            "ATM_ID": "ATM001"
        }
    ]
#user data and info

def ATM_Accounts():
    return [
        {
            "account_number": "123456789",
            "account_holder": "John Doe",
            "balance": 1000.00,
            "Account_PIN": 1234
        },
        {
            "account_number": "987654321",
            "account_holder": "Jane Smith",
            "balance": 500.00,
            "Account_PIN": 5678
        }
    ]


ATM_ON = True

#Start Menu
def start_screen(ATM_ON):
    print("Welcome to MyBank ATM. Please choose an option:")
    print("1.)Login to your account")
    print("2.)ATM information")
    print("3.)Request help")
    USER_OPTION = int(input("Please select an option: "))
    return USER_OPTION

#accessed_acount menu
def user_interface(account_access):
    print("1. Check balance")
    print("2. Withdraw funds")
    print("3. Deposit funds")
    print("4. Exit")
    user_option = int(input("Please select an option:"))
    return user_option


if ATM_ON:
    USER_OPTION = start_screen(ATM_ON)

if USER_OPTION not in:
    print("Invalid option. Please try again.")
    USER_OPTION = start_screen(ATM_ON)

#account look up and pin verification 
while True:
    if USER_OPTION == 2:
        print("You have selected to view ATM information.")
        for atm in ATM_info():
            print("ATM ID:", atm['ATM_ID'])
            print("Location:", atm['location'])
        USER_OPTION = start_screen(ATM_ON)

    elif USER_OPTION == 1:
        print("You have selected to login to your account.")
        break

    elif USER_OPTION == 3:
        print("You have selected to request help. Please contact customer service for assistance.")
        print("Customer service can be reached at 1-800-555-1234 or via email at support@mybank.com")
        USER_OPTION = start_screen(ATM_ON)


if USER_OPTION == 1:
    user_inAccount = input("Please enter your account number: ")
    account_found = False
    for acc in ATM_Accounts():
        if user_inAccount == acc["account_number"]:
            account_found = True
            print("Account found. Please enter your PIN.")
            account_PIN = acc["Account_PIN"]
            break

    if not account_found:
        print("Account not found. Please check your account number and try again.")

    if account_found:
        user_inPin = int(input("Please enter your PIN: "))

        if user_inPin not in range(0000, 10000):
            print("Invalid PIN. Please try again.")
            user_inPin = int(input("Please enter your PIN: "))

        attempts = 1
        account_access = False
        while True:
            if user_inPin == account_PIN:
                print("Access granted. Welcome,", acc["account_holder"], "to MyBank ATM.")
                account_access = True
                break
            else:
                print("Incorrect PIN. Please try again.")
                user_inPin = int(input("Please enter your PIN: "))
                attempts = attempts + 1
            if attempts >= 3:
                print("Too many incorrect attempts. Your account has been locked.")
                break
#Logged in banking loop
        if account_access:
            user_option = user_interface(account_access)
            if user_option not in:
                print("Invalid option. Please try again.")
                user_option = user_interface(account_access)
            while True:
                if user_option == 1:
                    print("Your current balance is: $", acc["balance"])
                    user_option = user_interface(account_access)
                elif user_option == 2:
                    withdraw_amount = float(input("Enter the amount to withdraw: $"))
                    if withdraw_amount > acc["balance"]:
                        print("Insufficient funds. Please try again.")
                    else:
                        acc["balance"] -= withdraw_amount
                        print("Withdrawal successful. Your new balance is: $", acc["balance"])
                    user_option = user_interface(account_access)
                elif user_option == 3:
                    deposit_amount = float(input("Enter the amount to deposit: $"))
                    acc["balance"] += deposit_amount
                    print("Deposit successful. Your new balance is: $", acc["balance"])
                    user_option = user_interface(account_access)
                elif user_option == 4:
                    print("Thank you for using MyBank ATM. Come back soon!")
                    break
