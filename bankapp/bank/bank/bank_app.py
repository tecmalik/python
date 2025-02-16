import sys

from bankapp.bank.bank.bank import Bank
my_bank = Bank()
prompt = """
    welcome to BankApp
    
    1-> Create Account
    2-> Check Balance
    3-> Transfer
    4-> Update Pin
    5-> Delete Account
    6-> Exit program
    
"""

def display(message):
    print(message)

def user_choice(prompt):
    return input(prompt)


def create_account():
    try:
        firstname = user_choice("Enter your first name: ")
        lastname = user_choice("Enter your last name: ")
        pin = user_choice("Enter your pin: ")
        my_bank.create_account(firstname, lastname, pin)
        display("Account created Successfully.")
        display(f"your account number is {my_bank.get_account_number(firstname,lastname)}")
    except Exception as e :
        display(f" pin must be 4 digit {e}")
    finally:
        main_menu()


def check_balance():
    try:
        account_number = user_choice("Enter your account number: ")
        pin = user_choice("Enter your pin: ")
        display(f" your available balance is : {my_bank.check_account_balance(account_number, pin)}")

    except Exception as e :
        display(f" invalid details {e}")
    finally:
        main_menu()

def transfer():
    try:
        sender_number = int(user_choice("Enter your Account number: "))
        receiver_number = int(user_choice("Enter recipient's Account number: "))
        amount = int(user_choice("Enter amount you want to transfer: "))
        pin = user_choice("Enter your pin: ")
        my_bank.transfer(sender_number, receiver_number, amount, pin)
    except Exception as e :
        display(f" invalid credentials {e}")
    finally:
        main_menu()


def update_pin():
    try:
        account_number = user_choice("Enter your Account number: ")
        old_pin = user_choice("Enter your pin: ")
        new_pin = user_choice("Enter new pin number: ")
        my_bank.find_by_id(account_number).update_pin(old_pin, new_pin)
        display("PIN updated Successfully.")
    except Exception as e :
        display(f" pin must be 4 digit {e}")
    finally:
        main_menu()


def delete_account():
    try:
        account_number = user_choice("Enter your Account number: ")
        pin = user_choice("Enter your pin: ")
        my_bank.delete_account(account_number, pin)
        display("Account deleted Successfully.")
    except Exception as e :
        display(f" pin must be 4 digit {e}")
    finally:
        main_menu()


def main_menu():
    choice = user_choice(prompt)
    match choice:
        case "1" : create_account()
        case "2" : check_balance()
        case "3" : transfer()
        case "4" : update_pin()
        case "5" : delete_account()
        case "6" : sys.exit(0)
        case _ : display("invalid input")

main_menu()