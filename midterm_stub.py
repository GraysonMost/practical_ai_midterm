import random

word_list = [
    "python", "hangman", "computer", "programming", "keyboard",
    "elephant", "calendar", "sunshine", "mountain", "basketball",
    "orchestra", "universe", "chemistry", "adventure"
]

HANGMAN_STAGES = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========='''
]

def select_random_word():
    return random.choice(word_list).lower()

def initialize_game_state(word):
    return {
        "word": word,
        "guessed_letters": [],
        "word_completion": ["_" for _ in word],
        "tries_remaining": 6
    }

def display_game_state(game_state):
    print(HANGMAN_STAGES[6 - game_state["tries_remaining"]])
    print("Word: " + " ".join(game_state["word_completion"]))
    print(f"Guessed letters: {', '.join(game_state['guessed_letters'])}")
    print(f"Tries remaining: {game_state['tries_remaining']}")

def get_valid_guess(game_state):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in game_state["guessed_letters"]:
            return guess
        print("Invalid guess. Try again.")

def update_game_state(game_state, guessed_letter):
    game_state["guessed_letters"].append(guessed_letter)
    if guessed_letter in game_state["word"]:
        game_state["word_completion"] = [
            letter if letter in game_state["guessed_letters"] else "_"
            for letter in game_state["word"]
        ]
    else:
        game_state["tries_remaining"] -= 1

def is_game_over(game_state):
    return game_state["tries_remaining"] == 0 or "_" not in game_state["word_completion"]

def player_won(game_state):
    return "_" not in game_state["word_completion"]

def play_hangman():
    word = select_random_word()
    game_state = initialize_game_state(word)
    print("Welcome to Hangman!")
    while not is_game_over(game_state):
        display_game_state(game_state)
        guessed_letter = get_valid_guess(game_state)
        update_game_state(game_state, guessed_letter)
    
    display_game_state(game_state)
    if player_won(game_state):
        print("Congratulations! You guessed the word.")
    else:
        print(f"Game over! The word was: {word}")

def main():
    while True:
        play_hangman()
        if input("Play again? (y/n): ").lower() != "y":
            break

if __name__ == "__main__":
    main()
