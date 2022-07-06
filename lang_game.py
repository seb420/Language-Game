##
# lang_game.py
# Sebastian Pratt
# 10/06/2022 -> PRESENT ___________________________


# import any necessary functions
import random
import maskpass

# define the constants
WORDS = {"easy": {"hi": "hei", "good": "god", "thanks": "takk", "and": "og",
                  "one": "en", "yes": "ja", "no": "nei", "i": "jeg",
                  "you": "du", "maybe": "kanskje"},
         "medium": {"bye": "ha det", "bread": "brød", "sorry": "unnskyld",
                    "welcome": "velkommen", "eats": "spiser",
                    "good morning": "god morgen", "good night": "god natt",
                    "thousand": "tusen", "bear": "bjørn", "beer": "øl"},
         "hard": {"the bread": "brødet", "please": "vær så snill",
                  "thank you very much": "tusen takk",
                  "cup of coffee": "kopp kaffe",
                  "what is your name": "hva heter du",
                  "what did you say": "hva sa du", "the ducks": "endene",
                  "tomato soup": "tomatsuppe",
                  "do you need it": "trenger du det",
                  "it is food": "det er mat"}}

MIN_LIVES = 0
PASSWORD = "1234"

# define the variables

instr_print = "\nHei og velkommen. This is the Norwegian language game. It " \
               "is a \ngreat fun and exciting way to practice your Norwegian "\
               "skills. \nTo play simply translate the words on screen, " \
               "if you get a \nquestion right you have the option to double " \
               "your points if \nyou get the next question right or you can " \
               "play it safe and \nbank the points. You only have three " \
               "wrong guesses before the \ngame is over though so be careful. "


def try_int(number):
    """
    This function will try to convert the input to an integer.
    If it is not an integer it will return False.
    """
    try:
        int(number)
        return True
    except ValueError:
        return False


def menu():
    """
    This function will print out the menu and return the option that the user
    selects.
    """
    print("\n     Norwegian Game")
    print("1.............Instructions")
    print("2.....English to Norwegian")
    print("3.....Norwegian to English")
    print("4....................Study")
    print("5.............Teacher Menu")
    print("6.....................Quit")
    option = input("Please select an option: ")
    while not try_int(option) or 1 > int(option) or int(option) > 6:
        option = input("Please select a number between 1 and 6: ")
    return int(option)


def main():
    """
    This is to run the main program and manage all the functions within it
    call the corresponding function based on the option selected in the menu.
    """
    # loop until the user quits
    while True:
        MENU_OPTIONS[menu()]()


def instructions():
    """
    This function will print out the instructions and return to the menu
    once it is done.
    """
    input(instr_print)


def english_to_norwegian():
    """
    the game in e to n
    """
    banked_points = 0
    round_points = 0
    lives = 3
    print("\n--- English to Norwegian ---\n")
    print(heart_calc(lives))
    question = 0
    while lives > MIN_LIVES:

        question += 1
        difficulty = random.randint(1, question)
        if difficulty <= 2:
            difficulty = "easy"
        elif difficulty == 3 or difficulty == 4:
            difficulty = "medium"
        elif difficulty >= 5:
            if difficulty % 3 == 0:
                difficulty = "hard"
            elif difficulty % 3 == 1:
                difficulty = "medium"
            elif difficulty % 3 == 2:
                difficulty = "hard"
        word = random.choice(list(WORDS[difficulty]))
        answer = input(f"What is '{word}' in Norwegian? ").lower().strip()
        if answer == WORDS[difficulty][word]:
            print("\nWell done!")
            round_points *= 2
            print(heart_calc(lives))
            if difficulty == "easy":
                print("Points +1")
                round_points += 1
            elif difficulty == "medium":
                print("Points +2")
                round_points += 2
            elif difficulty == "hard":
                print("Points +3")
                round_points += 3
            bank_risk = input(f"\nYou now have {round_points} point(s), "
                              f"do you "
                              "want to risk it for double or bank it? ("
                              "bank/risk) ").lower()
            while bank_risk != "bank" and bank_risk != "risk":
                bank_risk = input("Please enter 'bank' or 'risk': ").lower()
            if bank_risk == "bank":
                banked_points += round_points
                round_points = 0
                print(f"You now have {banked_points} points")
            elif bank_risk == "risk":
                print(f"Good Luck! You are risking {round_points} point(s)")
        else:
            print(f"\nUnlucky, '{word}' in Norwegian is "
                  f"'{WORDS[difficulty][word]}'")
            lives -= 1
            print(heart_calc(lives))
            print(f"You lost your {round_points} saved points :(")
            round_points = 0

    print(f"\nGame Over! You finished with {banked_points} points")


def norwegian_to_english():
    """
        the game in n to e
    """
    banked_points = 0
    round_points = 0
    lives = 3
    print("\n--- Norwegian to English ---\n")
    print(heart_calc(lives))
    question = 0
    while lives > MIN_LIVES:
        question += 1
        difficulty = random.randint(1, question)
        if difficulty <= 2:
            difficulty = "easy"
        elif difficulty == 3 or difficulty == 4:
            difficulty = "medium"
        elif difficulty >= 5:
            if difficulty % 3 == 0:
                difficulty = "hard"
            elif difficulty % 3 == 1:
                difficulty = "medium"
            elif difficulty % 3 == 2:
                difficulty = "hard"
        word = random.choice(list(WORDS[difficulty]))
        answer = input(f"What is '{WORDS[difficulty][word]}' in English? "
                       f"").lower().strip()
        if answer == word:
            print("\nWell done!")
            round_points *= 2
            print(heart_calc(lives))
            if difficulty == "easy":
                print("Points +1")
                round_points += 1
            elif difficulty == "medium":
                print("Points +2")
                round_points += 2
            elif difficulty == "hard":
                print("Points +3")
                round_points += 3
            bank_risk = input(f"\nYou now have {round_points} point(s), "
                              f"do you "
                              "want to risk it for double or bank it? ("
                              "bank/risk) ").lower()
            while bank_risk != "bank" and bank_risk != "risk":
                bank_risk = input("Please enter 'bank' or 'risk': ").lower()
            if bank_risk == "bank":
                banked_points += round_points
                round_points = 0
                print(f"You now have {banked_points} points")
            elif bank_risk == "risk":
                print(f"Good Luck! You are risking {round_points} point(s)")
        else:
            print(f"\nUnlucky, '{WORDS[difficulty][word]}' in English is "
                  f"'{word}'")
            lives -= 1
            print(heart_calc(lives))
            print(f"You lost your {round_points} saved points :(")
            round_points = 0

    print(f"\nGame Over! You finished with {banked_points} points")


def study():
    """
    study
    """


def teacher_menu():
    """
    menu for the teachers
    """
    password = maskpass.askpass(prompt="Password: ", mask="*")
    if password == PASSWORD:
        print("\nTeacher Menu")
        print("1....Edit Instructions")
        print("2...........View Words")
        print("3...........Edit Words")
        print("4...........Edit lives")
        option = input("Please select an option: ")
        while not try_int(option) or 1 > int(option) or int(option) > 4:
            option = input("Please select an option: ")
        TEACHER_MENU_OPTIONS[int(option)]()
    else:
        print("Incorrect password")


def heart_calc(hearts):
    """
    calculate and print the remaining hearts
    """
    if hearts == 3:
        picture = "❤❤❤"
    elif hearts == 2:
        picture = "❤❤💔"
    elif hearts == 1:
        picture = "❤💔💔"
    else:
        picture = "💔💔💔"
    return f"Lives: {picture}\n"


def quit_game():
    """
    quits
    """
    # quit the whole program
    exit()


def edit_instructions(old_instructions):
    """
    lets the teacher change the instructions
    """
    print(f"\nThe current instructions are:\n{instr_print}")
    instr_print = input("\nPlease enter new instructions: \n")



def view_words():
    """
    lets the teacher view the words
    """


def edit_words():
    """
    lets the teacher edit the words
    """


def edit_lives():
    """
    lets the teacher edit the lives
    """


# define menu options down here after function have been defined.
MENU_OPTIONS = {1: instructions,
                2: english_to_norwegian,
                3: norwegian_to_english,
                4: study,
                5: teacher_menu,
                6: quit_game}
TEACHER_MENU_OPTIONS = {1: edit_instructions,
                        2: view_words,
                        3: edit_words,
                        4: edit_lives, }

# call the main function
main()

"""
Password: ****

     Teacher Menu    
1....Edit Instructions
2...........View words
3...........Edit words
4...........Edit lives
"""
