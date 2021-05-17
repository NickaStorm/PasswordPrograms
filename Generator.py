import random


# this will be our list of all of wanted characters
allcharlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
               "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
               "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#",
               "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "|", ";",
               ":", "'", ",", ".", "<", ">", "?", "/"]

# this list helps us with generating the combination of words later on
numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# this function will help us with user readability and accessiblity
def syntaxerror():
    print("* * * * * * * * * * * * * * * * * * * * * * *")
    print("Please try to answer with one of the prompts.")

# this breaks the blocks of text up for readability
def astline():
    print("* * * * * * * * * * * * * * * * * * * * * * *\n")

# this function asks the user if they want to repeat the script
def askagain():
    useagain = input("Would you like to use this script again?\n[Yes/No]\n>")
    if useagain.lower() == "yes":
        welcome()
    elif useagain.lower() == "no":
        astline()
        print("Thank you for using this password generator.\nHave a good day!")
    else:
        syntaxerror()
        astline()
        askagain()

# the starting script that gathers most of the needed input and information
def welcome():
    astline()
    choice = input("Do you want to: \nGenerate a password \nOR \nCheck the security of a existing password \nAnswers: [Generate/Check] \n>")
    if choice.lower() == "generate":
        astline()
        word_or_rand = input("Would you like your password to be\nRandomly generated\nOR\nA combination of words?\n[Random/Word]\n>")
        if word_or_rand.lower() == "random":
            astline()
            generator(input("What security level would you like your password? \n[Easy, Medium, Hard]\n>"))
        elif word_or_rand.lower() == "word":
            astline()
            word_generator()
        else:
            syntaxerror()
            welcome()
    elif choice.lower() == "check":
        astline()
        inputpassword = input("Please enter a password, so I can check the security.\n>")
        check(inputpassword)
    else:
        syntaxerror()
        welcome()

# this function takes the words from a txt file, and concatenate them
def word_generator():
    word_password = ""
    with open("1000mostcommonwords", "r") as text_file:
        text_read = text_file.read()
        seperate_lines = text_read.split()
        for num in range(0, random.randint(3, 6)):
            word_password = word_password + seperate_lines[random.randint(0, len(seperate_lines) - 1)]
        print("Your password is " + word_password)
        astline()
        askagain()

# this function just takes random letters from the list, and adds them together
def simple_generator(difficulty, min, max):
    password = ""
    astline()
    print("Your " + difficulty.lower() + " level password is:")
    for num in range(0, random.randint(min, max)):
        password = password + allcharlist[random.randint(0, len(allcharlist) - 1)]
    print(password)
    askagain()

# this function established the difficulty of password the user wants, and relays this info to the function above
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

# this function works by checking the occurence of each letter, and the length of the password, and assigns it to a number value
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
        astline()
        print("You probably need to change your password.")
    elif password_value <= 90:
        astline()
        print("This is a good password, very difficult to bruteforce.")
    elif password_value > 90:
        astline()
        print("This is a great password\nJust remember it, so you don't forget it.")
    askagain()


# this starts the entire script
welcome()