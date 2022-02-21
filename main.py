import random
import os


def clearConsole():
    command = "clear"
    if os.name in ("nt", "cls"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


clearConsole()
HANGMANPICS = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

clearConsole()
print(
    """888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"           \n\n"""
)
words_list = ["Titanic", "Avengers", "Lagaan", "Blue", "highway", "The Founder"]
chosen_word = random.choice(words_list).lower()
display = []
for i in chosen_word:
    if i != " ":
        display += "_"
    else:
        display += " "

chances = 0
while chances <= 6:

    user_guess = input("Enter your guess : ").lower()
    print(f"Remaining Guesses : {6-chances}")
    if user_guess not in chosen_word:
        print(HANGMANPICS[chances])
        chances += 1
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == user_guess:
                display[i] = user_guess
        if chances > 0:
            print(HANGMANPICS[chances - 1])
    word = "".join(display)
    print(word)
    if word == chosen_word:
        print("Congrats!!\nYou have won!!!")
        break

if chances == 7:
    print(f"The movie was {chosen_word}")
    print("You Lost!! Game Over")
