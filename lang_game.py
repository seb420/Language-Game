##
# lang_game.py
# Sebastian Pratt
# 10/06/2022 -> PRESENT ___________________________


# import any necessary functions


# define the constants
MENU_OPTIONS = {1: "instructions",
                2: "english_to_norwegian",
                3: "norwegian_to_english",
                4: "study",
                5: "teacher_menu",
                6: "quit"}
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
    This function will print out the menu and return the option that the user selects.
    """
    print("      Norwegian Game")
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
    This is to run the main program and manage all the functions within it.
    call the corresponding function based on the option selected in the menu function.
    """
    print(menu())


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


# call the main function
main()
"""
      Norwegian Game      
1.............Instructions
2.....English to Norwegian
3.....Norwegian to English
4....................Study
5.............Teacher Menu
6.....................Quit
"""
