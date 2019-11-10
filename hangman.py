import random

#function for hangman drawing in 10 incorrect attempts
def draw(missed):
    switcher = {
    1:  "  O ",
    2:  "  O \n"
        "  | ",
    3:  "  O \n"
        "  | \n"
        " /  ",
    4:  "  O  \n"
        "  |  \n"
        " / \ ", 
    5:  " \O  \n"
        "  |  \n"
        " / \ ",
    6:  " \O/ \n"
        "  |  \n"
        " / \ ",           
    7:  "      | \n"
        " \O/  | \n"
        "  |   | \n"
        " / \    ",  
    8:  "      | \n"
        " \O/  | \n"
        "  |   | \n"
        " / \ / \ ", 
    9:  "  ----- \n"
        "      | \n"
        " \O/  | \n"
        "  |   | \n"
        " / \ / \ ", 
    10: "  ----- \n"
        "  |   | \n"
        "  O   | \n"
        " /|\  | \n"
        " / \ / \ " 
    }
    return print(switcher.get(missed))

def hangman():
    wordlist = ["tiger", "badger", "beaver", "cougar", "eagle", "elephant", "flamingo", "gorilla", "lobster", "pokemon"]
    word = random.choice(wordlist)
    #validation for user input letters:
    valletters = "abcdefghijklmnopqrstuvwxyz"
    #create a duplicate of the word and mask letters with stars:
    letter = ""
    for i in word:
        letter += "*"
    #user attempts countdown:
    attempt = 10
    #incorrect attempts counter:
    missed = 0
    print(letter)
    #loop if wrong attempts<10 and have unopened letters in the world
    while (missed < 10) and ("*" in letter):
        print("Mistakes left: ", attempt)
        usrletter = input("\nPlease enter a letter: ")
        if usrletter.lower() not in valletters:
            print("Incorrect input! You need to enter a single letter")
        if usrletter in word:
            index = word.find(usrletter)
            letter = letter[:index]+usrletter+letter[index+1:]
            word = word[:index]+"-"+word[index+1:]
            print(letter)
        else:
            print(letter)
            attempt = attempt - 1
            missed += 1
            draw(missed)
    else:
        if ("*" not in letter):
            print("\nCongratulations! You win!")
        else:
            print("\nSorry, you are dead.")

name = input("Please enter your name: ")
print("Hi,", name)
print("Try to guess the word. After 10 mistakes you are dead.")
print("Every star is a letter.")
hangman()
