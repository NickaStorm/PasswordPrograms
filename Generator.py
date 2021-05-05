import random

allcharlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
               "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
               "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#",
               "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "|", ";",
               ":", "'", ",", ".", "<", ">", "?", "/"]

def syntaxerror():
    print("* * * * * * * * * * * * * * * * * * * * * * *")
    print("Please try to answer with one of the prompts.")
    print("* * * * * * * * * * * * * * * * * * * * * * *\n")

def askagain():
    useagain = input("Would you like to use this script again?\n[Yes/No]\n>")
    if useagain.lower() == "yes":
        welcome()
    elif useagain.lower() == "no":
        print("Thank you for using this password generator.\nHave a good day!")
    else:
        askagain()


def welcome():
    choice = input("Do you want to: \nGenerate a password \nOR \nCheck the security of a existing password \nAnswers: [Generate/Check] \n>")
    if choice.lower() == "generate":
        generator(input("What security level would you like your password? \n[Easy, Medium, Hard]\n>"))
    elif choice.lower() == "check":
        inputpassword = input("Please enter a password, so I can check the security.\n>")
        check(inputpassword)
    else:
        syntaxerror()
        welcome()

def simple_generator(difficulty, min, max):
    password = ""
    print("Your " + difficulty.lower() + " level password is:")
    for num in range(0, random.randint(min, max)):
        password = password + allcharlist[random.randint(0, len(allcharlist) - 1)]
    print(password)
    askagain()

def generator(security_lvl):
    if security_lvl.lower() == "easy":
        simple_generator(security_lvl.lower(), 7, 9)
    elif security_lvl.lower() == "medium":
        simple_generator(security_lvl.lower(), 10, 14)
    elif security_lvl.lower() == "hard":
        simple_generator(security_lvl.lower(), 15, 20)
    else:
        syntaxerror()
        generator(input("What security level would you like your password? \n[Easy, Medium, Hard]\n>"))

def check(input_password):
    password_value = len(input_password) * 3
    for letter in input_password:
        if input_password.count(letter) <= 2:
            password_value += 3
        elif input_password.count(letter) <= 3:
            password_value += 1
        elif input_password.count(letter) > 3:
            password_value -= 1
    if password_value <= 60:
        print("You probably need to change your password.")
    elif password_value <= 90:
        print("This is a good password, very difficult to bruteforce.")
    elif password_value > 90:
        print("This is a great password\nJust remember it, so you don't forget it.")
    askagain()

welcome()