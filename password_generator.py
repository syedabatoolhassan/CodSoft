import random
import string #to grab all upper and lowercase letter, special characters and numbera

def generate_password(min_length, number=True, speical_characters=True):
    letter = string.ascii_letters
    digit= string.digits
    special= string.punctuation

    characters=letter  #Start with letters add digits and special characters based on the user choice
    if number:
        characters+=digit
    if speical_characters:
        characters += special
    password =""
    meet_critera = False   #to check if the generated password meets all criteria
    has_number = False     #to check if the password contains at least one number
    has_special = False    #to check if the password contains at least one special character

    while not meet_critera or len(password) < min_length: #continueing loop until password meet critera
        new_char = random.choice(characters)
        password += new_char

        if new_char in digit:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_critera = True
        if number:
            meet_critera = has_number   #Check if the password has at least one number
        if speical_characters:
            meet_critera = meet_critera and has_special   #Check if the password has at least one special character
    return password
min_length = int(input("Enter the minimum length :"))
has_number= input("Do you want to have numbers in your password (y/n)? ").lower()=='y'
has_special = input("Do you want to have special charachters in your password? (y/n)? ").lower()=='y'

password = generate_password(min_length, has_number, has_special) #generate password based on user input
print("The generated password is :", password)