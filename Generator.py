import random

allcharlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
               "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
               "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#",
               "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "|", ";",
               ":", "'", ",", ".", "<", ">", "?", "/"]

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
        security_lvl = input("What security level would you like your password? \n[Easy, Medium, Hard]\n>")
        generator(security_lvl)
    elif choice.lower() == "check":
        inputpassword = input("Please enter a password, so I can check the security.\n>")
        check(inputpassword)
    else:
        print("* * * * * * * * * * * * * * * * * * * * * * *")
        print("Please try to answer with one of the prompts.")
        print("* * * * * * * * * * * * * * * * * * * * * * *\n")
        welcome()

def generator(security_lvl):
    password = ""
    if security_lvl.lower() == "easy":
        print("Your Easy level password is:")
        for num in range(0, random.randint(7,10)):
            password = password + allcharlist[random.randint(0, len(allcharlist)-1)]
        print(password)
        askagain()
    elif security_lvl.lower() == "medium":
        print("Your Medium level password is:")
        for num in range(0, random.randint(11,14)):
            password = password + allcharlist[random.randint(0, 85)]
        print(password)
        askagain()
    elif security_lvl.lower() == "hard":
        print("Your Hard level password is:")
        for num in range(0, random.randint(15,20)):
            password = password + allcharlist[random.randint(0, 85)]
        print(password)
        askagain()
    else:
        print("Please try to answer with one of the prompts.")
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