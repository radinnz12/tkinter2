import tkinter as tk
import random

class GuessTheWord:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Word Game")

        self.words = ["python", "programming", "technology", "computer"]
        self.secret_word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts = 6

        self.label = tk.Label(master, text="Guess the word: " + self.get_display_word())
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.guess)
        self.guess_button.pack()

        self.reset_button = tk.Button(master, text="Play Again", command=self.reset_game)
        self.reset_button.pack()

        self.message = tk.Label(master, text="")
        self.message.pack()

    def get_display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.secret_word])

    def guess(self):
        if self.attempts <= 0:
            self.message.config(text="You cannot guess anymore. Please reset the game.")
            return

        letter = self.entry.get()
        self.entry.delete(0, tk.END)

        if letter in self.guessed_letters or len(letter) != 1:
            self.message.config(text="Please enter a new letter.")
            return

        self.guessed_letters.append(letter)

        if letter not in self.secret_word:
            self.attempts -= 1
            self.message.config(text=f"The letter '{letter}' is not in the word. Attempts left: {self.attempts}")
            if self.attempts == 0:
                self.label.config(text="You lost! The word was: " + self.secret_word)
                return

        self.label.config(text="Guess the word: " + self.get_display_word())

        if all(letter in self.guessed_letters for letter in self.secret_word):
            self.label.config(text="Congratulations! You've guessed the word: " + self.secret_word)

    def reset_game(self):
        self.secret_word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts = 6
        self.label.config(text="Guess the word: " + self.get_display_word())
        self.message.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheWord(root)
    root.mainloop()
