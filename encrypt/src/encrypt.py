from '.'
USER_DETAILS = 'user_details.txt'

password = input("Enter password: ")

def hashed_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def save_to_file(username , password):
    with open(USER_DETAILS, 'a') as user_file:
        user_file.write(f'{username} , {password.decode('utf-8')}\n')

def register_user():
    while True:
        username = input("Enter username: ")
        if not username:
            print("Username can't be empty")
            continue
        break

    while True:
        password = input("Enter password: ")
        if not password:
            print("Password can't be empty")
            continue
        break

    save_to_file(username , hashed_password(password))

    def validate_username(username , password):
        with open('user_details.txt', 'r') as user_file:
            details = user_file.read()
            for line in details.split('\n'):
                stored_username , stored_password = line.split(',')
                if username == stored_username:
                    return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))


    def login_user():
        username = input("Enter username: ")
        password = input("Enter password: ")
        validate_username(username,password)
    def main():
        menu = """
         1. to register user
         2. to lohin user
         3. to exit
         """
        choice = input(menu)
        match(choice):
            case 1 : register_user()
            case 2 : login_user()
            case 3 :print("thankyou")