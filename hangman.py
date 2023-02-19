import random as rng
import re

stages = [
"""    +----+
         |
         |
         |
         |
         |
  ============""", 


"""    +----+
    |    |
         |
         |
         |
         |
  ============""",


"""    +----+
    |    |
    O    |
         |
         |
         |
  ============""",


"""    +----+
    |    |
    O    |
    |    |
         |
         |
  ============""",


"""    +----+
    |    |
    O    |
   /|    |
         |
         |
  ============""",


"""    +----+
    |    |
    O    |
   /|\   |
         |
         |
  ============""",


"""    +----+
    |    |
    O    |
   /|\   |
   /     |
         |
  ============""",


"""    +----+
    |    |
    O    |
   /|\   |
   / \   |
         |
  ============"""]
guess_words = ['banana', 'computer', 'elephant', 'guitar', 'kangaroo', 'library', 
               'microphone', 'octopus', 'pizza', 'rainbow', 'saxophone', 'telephone', 
               'umbrella', 'volleyball', 'watermelon', 'xylophone', 'yogurt', 'zebra', 'airplane', 'basketball'
]


guesses = 0
wrong_guesses = []


word_index = rng.randrange(0, len(guess_words))
selected_word = guess_words[word_index]
word_to_guess = "_" * len(selected_word)

while True:
  print(stages[guesses])
  print(word_to_guess)
  guess = input("Enter your guess: ")
  if guess in selected_word:
      indexes = [m.start() for m in re.finditer(guess, selected_word)]
      word_to_guess_list = list(word_to_guess)
      for i in indexes:
          word_to_guess_list[i] = guess
      word_to_guess = "".join(word_to_guess_list)
      if "_" not in word_to_guess:
          print("Congratulations! You guessed the word.")
          break
  else:
      wrong_guesses.append(guess)
      print("Wrong guesses: ", wrong_guesses)
      guesses += 1
      if guesses == len(stages):
          print("You ran out of guesses. The word was:", selected_word)
          break