#Here is my function file

#Here is my choose word function:

def choose_word():
    
    import random

    words = [ "grape", "chair", "bread", "house",
    "tiger", "plant", "cloud", "stone", "brick",
    "flame", "crisp", "drink", "beach", "smile",
    "world", "ghost", "train", "sword", "light",
    "dance", "proud", "mouse", "black", "green",
    "brown", "shirt", "piano", "fruit", "sugar",
    "ocean", "field", "horse", "snake", "dream",
    "quick", "zebra", "watch", "storm", "bland",
    "crown", "paint", "lunch", "frost", "glove",
    "charm", "swing", "money", "flash", "round"]

    word = random.choice(words)
    letters = list(word)
    return letters

#Here is my function that gets the player's guess and adds it to a list:

def get_guess(previous_guess):
    player_guess = input("Guess a five letter word: ").lower()
    while len(player_guess) != 5 or not player_guess.isalpha() or player_guess in previous_guess:
        print("Invalid guess! Try again!")
        player_guess = input("Guess a five letter word: ").lower()

    previous_guess.append(player_guess)
    
    player_letters = list(player_guess)
    return player_letters

#Here is my function that will evaluate the player's guess and give feedback:

def evaluate_guess(letters, player_letters):
    feedback = ""
    for i in range(5):
        if letters[i] == player_letters[i]:
            feedback += "G"
        elif player_letters[i] in letters:
            feedback += "Y"
        else:
            feedback += "-"
    return(feedback)

#Here is the function where the player's guess is displayed as well as the feedback is displayed:

def display_guess(player_letters, feedback):
    print("Guess: " + "".join(player_letters).upper())
    print(f"Feedback: {feedback}")

#Here is the function that determines if the player has guessed the word:

def has_won (feedback):
    if feedback == "GGGGG":
        return(True)
    else:
        return(False)