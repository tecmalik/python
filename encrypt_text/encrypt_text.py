def get_encrypt_text(text):
    alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabetList2 =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    encrypted_text = ""
    encrypted_alphabet = ""
    for character in text:
        if character in alphabetList:
            for count in range(len(alphabetList)):
                if character == alphabetList[count]:
                    if count < 40 :
                        encrypted_alphabet += alphabetList[count+13]
                    else :
                        encrypted_alphabet += alphabetList2[count%13]
        else:
            encrypted_alphabet += character
    encrypted_text += encrypted_alphabet
    return encrypted_text
'''
collect the text
create an empty string
if the string is an alphabetic character it should have a shift in 13th position
else if its character it should remain 
append the characters 
and return the encrypted string string  
'''
