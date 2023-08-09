def create_account():
    print(f"""
    =============================================
                 Create account
    =============================================
    """)
    user_input_firstname = input('Enter first name')
    user_input_lastname = input('Enter last name')
    user_input_phone_number = input('Enter phone number')
    user_input_PIN = input('set up PIN')
    print('you successfully create an account ')
    print(f"{user_input_firstname} + ")


def deposit():
    pass


def withdraw():
    pass


def transfer():
    pass


def check_balance():
    pass


def main_menu():
    print(f"""
    ========================================
            WELCOME TO SULTY BANK
    ========================================
    1. Create account
    2. Deposit
    3. Withdraw
    4. Transfer
    5. Check balance
    6. Exit
    """)
    user_input = input('select an option to proceed... ')
    if user_input == '1':
        create_account()
    elif user_input == '2':
        deposit()
    elif user_input == '3':
        withdraw()
    elif user_input == '4':
        transfer()
    elif user_input == '5':
        check_balance()
    elif user_input == '6':
        exit()
    else:
        main_menu()
