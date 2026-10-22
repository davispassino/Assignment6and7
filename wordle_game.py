#Here is where my program imports the functions from wordlefunctions.py:

from wordlefunctions import choose_word, get_guess, evaluate_guess, display_guess, has_won

#Welcome the player and begin the main game loop:

print("\nWelcome to Wordle!")

play_again = "y"
while play_again in ["y","yes"]:
    print("\nYou have 6 tries to guess the correct 5 letter word.")
    print("\n G = correct letter and position")
    print(" Y = correct letter but wrong position")
    print(" - = the letter is not in the word\n")

    #Defined game variables, select a secret word, and begin the six-attempt loop:

    round_counter = 1
    previous_guess = []
    letters = choose_word()

    for i in range(6):
        
        print(f"Round {round_counter} of 6")

        #Get and evaluate the player's guess, display feedback, and check for a win:

        player_letters = get_guess(previous_guess)
        feedback = evaluate_guess(letters, player_letters)
        display_guess(player_letters, feedback)

        if has_won(feedback):
            print("Congratulations! You guessed the word!")
            break

        round_counter += 1
        
    if not has_won(feedback):
        print("Sorry, the word was " + "".join(letters).upper() + ".")

    #Here is where the program will ask you to play again. It will either loop or exit the code.

    print("Would you like to play again?")
    play_again = input("Type y/n: ").lower()

    while play_again not in ["y", "n", "yes", "no"]:
        print("Invalid input, try again!")
        play_again = input("y/n: ").lower()

print("Thanks for playing!")

