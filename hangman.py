from random import choice

def choose_word():
    """randomizes a list of words"""
    secret_words = ["postcard", "icecream", "pencil", "hike", "almond", "laptop", "travel", "picture", "island", "adventure", "balloon", "elephant", "computer", "water", "paper", "backpack"]
    secret_word = choice(secret_words)
    secret_word = secret_word.lower()
    return secret_word
    
def get_fruits():
    """randomizes a list of fruits"""
    fruits = ["apple", "banana", "blackberry", "blueberry", "avocado", "watermelon", "cantaloupe", "honeydew", "orange", "pear", "peach", "strawberry", "cherry", "pineapple", "kiwi", "mango", "grape", "grapefruit", "guava"]
    fruit = choice(fruits)
    fruit = fruit.lower()
    return fruit

def get_colors():
    """randomizes a list of colors"""
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "violet", "cyan", "indigo", "brown", "black", "white", "pink", "beige", "burgundy", "turquoise", "teal"]
    color = choice(colors)
    color = color.lower()
    return color
    
def get_sports():
    """randomizes a list of sports"""
    sports = ["basketball", "soccer", "baseball", "tennis", "football", "badminton", "golf", "hockey", "volleyball", "rugby", "cricket", "fencing", "wrestling", "track", "gymnastics"]
    sport = choice(sports)
    sport = sport.lower()
    return sport
    
def get_blanks(random_word):
    """prints spaces(_) for each letter in word"""
    blanks = '_ ' * len(random_word)
    print blanks


def check_if_match(guess_word, guesses, guess_letter):
    """Checks if letter matches word, Prints how many letters in word with blanks. Prints list of guesses"""
    blanks = ""
    match = 0
    for letter in guess_word:
        if letter in guesses:
            blanks += letter
        else:
            blanks += "_ "
        if letter == guess_letter:
            match += + 1
    if match == 1:
        print "Yea! The word has the letter {}".format (guess_letter)
    elif match > 1:
        print "Yea! The word has {} {}'s".format(match, guess_letter)
    else:
        print "Sorry, the word does not have the letter {}".format(guess_letter)
    print guesses
    return blanks
    
def player_guess(guess_word):
    """player guesses a letter, if letter in list of guesses, try a different letter
    if not, add to guesses list, if guess is the word, print word and how many tries"""

    guesses = []

    while True:
        guess_letter= raw_input("Guess a letter or the word: ")
        guess_letter = guess_letter.lower()
        guess_letter.isalpha()
        
        if guess_letter.isalpha():
            
            if guess_letter in guesses:
                print "You have already guess {}. Please try a different letter".format(guess_letter)
            elif len(guess_letter) == 1:
                guesses.append(guess_letter)
                answer = check_if_match(guess_word,guesses,guess_letter)
                if answer == guess_word:
                    break
                else:
                    print answer
            elif len(guess_letter) == len(guess_word):
                guesses.append(guess_letter)
                if guess_letter == guess_word:
                     break
                else: 
                    print "Sorry, not the word, please try again."
            else:
                print "Sorry, please enter one letter or the whole word"
        else:
            print "Please enter letters only"
            
    print "Yes, the word is {}! You guessed it in {} tries".format(guess_word, len(guesses)) 
    
    
def ask_play_again():
    """askes if player wants to play again"""
    play_again = True
    while  play_again:
        play = raw_input("Do you want to play again? (y/n) ")
        play = play.lower()
        if play == "y":
            play_game()
        elif play == "n":
            play_again = False
        else:
            print "This is not one of the options, please try again."
            
            
def play_game():
    """plays the game and asks if player wants to play again"""
    print "Hi! Welcome to Hangman!"
    while True:
        print "What category would you like?"
        print "1. Fruits"
        print "2. Colors"
        print "3. Sports"
        print "4. Random"
        
        category_choice = raw_input(">>")
       
        if category_choice == "1":
            word = get_fruits()
            break
        elif category_choice == "2":
            word = get_colors()
            break
        elif category_choice == "3":
            word = get_sports()
            break
        elif category_choice == "4":
            word = choose_word()
            break
        else:
            print "Sorry, that is not an option"
    get_blanks(word)
    player_guess(word)


play_game() 
ask_play_again()