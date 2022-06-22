##
# lang_game.py
# Sebastian Pratt
# 10/06/2022 -> PRESENT ___________________________


# import any necessary functions
import random

# define the constants
WORDS = {"easy": {"hi": "hei", "good": "god", "thanks": "takk", "and": "og",
                  "one": "en", "yes": "ja", "no": "nei", "i": "jeg",
                  "you": "du", "maybe": "kanskje"},
         "medium": {"bye": "ha det", "bread": "brød", "sorry": "unnskyld",
                    "welcome": "velkommen", "eats": "spiser",
                    "good morning": "god morgen", "good night": "god kveld",
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

# define the variables


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
    input("\nHei og velkommen. This is the Norwegian language game. It is a \n"
          "great fun and exciting way to practice your Norwegian skills. \n"
          "To play simply translate the words on screen, if you get a \n"
          "question right you have the option to double your points if \n"
          "you get the next question right or you can play it safe and \n"
          "bank the points. You only have three wrong guesses before the \n"
          "game is over though so be careful.")


def english_to_norwegian():
    """
    the game in e to n
    """
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
            print(heart_calc(lives))

        else:
            print(f"\nUnlucky, '{word}' in Norwegian is "
                  f"'{WORDS[difficulty][word]}'")
            lives -= 1
            print(heart_calc(lives))


    # 💔❤


def norwegian_to_english():
    """
        the game in n to e
    """


def study():
    """
    study
    """


def teacher_menu():
    """
    menu for the teachers
    """


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
    elif hearts == 0:
        picture = "💔💔💔"
    return f"Lives: {picture}\n"



def quit_game():
    """
    quits
    """
    # quit the whole program
    exit()


MENU_OPTIONS = {1: instructions,
                2: english_to_norwegian,
                3: norwegian_to_english,
                4: study,
                5: teacher_menu,
                6: quit_game}

# call the main function
main()

"""
What is "Hello" in Norwegian? 
"""
