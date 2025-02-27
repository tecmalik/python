from collections import Counter


def get_number_of_characters(user_input:str):
    return dict(Counter(user_input))

def swapFirstCharacters(first_input:str, second_input:str):
    temporary = first_input [:2:]
    temporary2 = second_input[:2:]
    temporary3 = first_input[2::]
    temporary4 = second_input[2::]
    return f"{temporary2+temporary3} {temporary+temporary4}"

def add_ce(input:str):
    if len(input) % 2 == 0:
        split_at = (len(input)//2)
        temporary1 = input[:split_at :]
        temporary2 = input[split_at::]
        return f"{temporary1}ce{temporary2}"
    else:
        return f"{input}ce"


def arrange_case(input):
    uppercase_letters = ""
    lowercase_letters = ""
    for character in input:
        if character.isupper() :
            uppercase_letters += character
        else:
            lowercase_letters += character
    return f"{uppercase_letters + lowercase_letters}"


def removeCharacter(word:str):
    result = ""
    for character in word:
        if character.isalpha() :
            result+=character
    return result
