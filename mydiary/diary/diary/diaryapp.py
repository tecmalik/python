import sys
from mydiary.diary.diary import diaries
my_dairies = diaries.Diaries()
user_name = None
password = None
prompt = """
    1 -> Create Diary.
    2 -> Find Diary.
    3 -> List Diaries.
    4 -> Delete Diary.
    5 -> Exit program.
"""
def display(message):
    print(message)

def get_input(message):
    display(message)
    return input

prompt2 = """
    1-> view diary Entry.
    2-> view Entry title & ID.
    3-> Create New Entry.
    4-> Find Entry by Id.
    5-> Delete New Entry.
    6-> Update Entry.
    7-> Delete Entry.
    8-> Back to main menu.
    9-> Exit program.
"""


def delete_entry():
    pass


def update_entry():
    try:
        i_d = get_input("Please enter entry ID to update: ")
        new_title = get_input("Enter new title: ")
        new_body = get_input("Enter new body: ")
        my_dairies.find_by_username(user_name).update_entry(i_d, new_title, new_body)
        display("pin updated successfully")
    except Exception as e:
        print(e)
    finally:
        diary_menu()


def update_entry_by_body():
    try:
        i_d = get_input("Please enter entry ID to update: ")
        diary = my_dairies.find_by_username(user_name)
        title = diary.title
        new_body = get_input(f"Enter new body for {title}  ")
        display("pin updated successfully")
        diary.update_entry_by_body(i_d,title, new_body)
        display("updated successfully")
    except Exception as e:
        print(e)
    finally:
        diary_menu()


def create_new_entry():
    try:
        title = get_input("Enter new title: ")
        body = get_input("Enter title's body: ")
        my_diary = my_dairies.find_by_username(user_name)
        my_diary.create_new_entry(title, body)
        display("new entry created successfully")
    except Exception as e:
        print(e)
    finally:
        diary_menu()


def find_entry_by_id():
    try:
        get_input("Please enter entry ID: ")
        my_diary = my_dairies.find_by_username(user_name)
        my_entry = my_diary.find_by_id(my_diary.id)
        get_input(my_entry.__str__())
    except Exception as e:
        print(e)
    finally:
        diary_menu()


def view_entry_title_and_ID():
    try:
        my_diary = my_dairies.find_by_username(user_name)
        my_entry = my_diary.find_by_id(my_diary.id)
        title = my_entry.title
        id_number = my_entry.id_number
        display(f"title{title} : id_number : {id_number}")
    except Exception as e:
        print(e)
    finally:
        diary_menu()


def view_all_diary_entry():
    try:
        my_diary = my_dairies.find_by_username(user_name)
        for entry in my_diary._entries:
            display(entry.__str__())
    except Exception as e:
        print(e)
    finally:
        diary_menu()


def diary_menu():
    user_input= get_input(prompt2)
    match user_input:
        case "1":view_all_diary_entry()
        case "2":view_entry_title_and_ID()
        case "3":create_new_entry()
        case "4":find_entry_by_id()
        case "5":update_entry_by_body()
        case "6":update_entry()
        case "7":delete_entry()
        case "8":main_menu()
        case "9":sys.exit(0)
        case _ : display(" invalid input.")

def create_diary():
    try:
        user_name = input("Enter username: ")
        password = input("create Password: ")
        my_dairies.add(user_name, password)
    except Exception as e:
        print("Something went wrong.")
    finally:
        diary_menu()


def delete_diary():
    try:
        user_name = input("Enter username: ")
        password = input("create Password: ")
        my_dairies.delete(user_name, password)
    except Exception as e:
        print("invalid details")
    finally:
        diary_menu()


def find_diary():
    try:
        user_name = input("Enter username: ")
        password = input("create Password: ")
        found_diary = my_dairies.find_by_username(user_name)
        display(f" Welcome {found_diary.__str__()}")
        found_diary.unlock(password)
    except Exception as e:
        print(f"invalid input.{e}" )
    finally:
        diary_menu()


def list_diary():
    try:
        count = 0
        for diary in my_dairies:
            display(f"{count} {diary.__str__()}")
            count += 1
    except Exception as e:
        print(f"invalid input.{e}" )
    finally:
        main_menu()


def main_menu():
    user_input = get_input(prompt)
    match(user_input):
        case "1":create_diary()
        case "2":find_diary()
        case "3":list_diary()
        case "4":delete_diary()
        case "5":sys.exit(0)
        case _ : display("invalid input")


main_menu();