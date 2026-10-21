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
    print(letters)
    return letters

def get_guess():
    player_guess = input("Guess a five letter word: ")
    player_guess = player_guess.lower()
    player_letters = list(player_guess)
    print(player_letters)
    return player_letters

def evaluate_guess(letters, player_letters):
    feedback = ""
    for i in range(5):
        if letters[i] == player_letters[i]:
            feedback += "G"
        elif player_letters[i] in letters:
            feedback += "Y"
        else:
            feedback += "-"
    print(feedback)
    return(feedback)

def display_guess(letters, feedback):
    print("".join(letters).upper())
    print(feedback)

def has_won(feedback):
    while feedback == "GGGGG":
        


    

letters = choose_word()
player_letters = get_guess()
feedback = evaluate_guess(letters, player_letters)
display_guess(letters, feedback)