import random

class Level: #level class to account for difficulty and maximum number of guesses allowed
    def __init__(self, difficulty, maxguess):
        self.difficulty = difficulty
        self.maxguess = maxguess

leveldict = { #a dictionary to store level using range and number of guesses,g, allowed: g-1
    "e" : Level(10, 5),
    "m" : Level(20, 3),
    "h" : Level(50, 2),
    }

def get_number(level): #Random variable generator between 1 and selected level
    return random.randint(1, leveldict[level].difficulty)

def select_level(): #Level select
    print("Would you like to play on easy, medium, or hard?\nType 'e' for easy, 'm' for medium, or 'h' for hard!")
    level = str(input())
    while level not in leveldict.keys(): #check for errors in select_level not in get_number
        print ("There are three levels: easy medium and hard")
        level = str(input("Type 'e' for easy, 'm' for medium, or 'h' for hard!"))
    return level

def guess_number(level): #guess entered
    print("Guess a number between 1 and {0}:\n".format(leveldict[level].difficulty))
    try:
        n = int(input())
    except ValueError:
        print("There are 3 levels: easy, medium and hard")
        n = guess_number(level)
    return n


def check_guess(guess, number): #comparing guess and random number
    if guess > number:
        print("That was wrong!")
    elif guess < number:
        print("That was wrong!")
    else:
        print("You got it right!")

def maxcount(level): #Guess range with level select
    return leveldict[level].maxguess

def mainloop():
    level = select_level()

    number = get_number(level)
    guess = guess_number(level)
    check_guess(guess, number)
    guesslevel = maxcount(level)
    num_guesses = 0

    while guess != number:
        guess = guess_number(level)
        check_guess(guess, number)
        num_guesses += 1

        if num_guesses == guesslevel:
            break
        else:
            print("Guess(es) left are {0}".format(guesslevel-num_guesses))
    print("Game Over!")
    play_again = str(input("To play again type 'yes'. To exit type 'no'. \n"))
    if play_again == "yes":
        mainloop()

mainloop()