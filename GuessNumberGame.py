import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("بازی حدس عدد")

        self.start_game()

        self.guess_button = tk.Button(master, text="حدس بزن", command=self.check_guess)
        self.guess_button.pack()

        self.restart_button = tk.Button(master, text="Restart", command=self.reset_game, state=tk.DISABLED)
        self.restart_button.pack()

    def start_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.guesses_taken = 0

        self.label = tk.Label(self.master, text="یک عدد بین 1 تا 100 حدس بزنید:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.guesses_taken += 1

            if guess < self.number_to_guess:
                self.result_label.config(text="عدد بزرگتر است.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="عدد کوچکتر است.")
            else:
                self.result_label.config(text=f"تبریک! عدد را در {self.guesses_taken} تلاش حدس زدید.")
                self.restart_button.config(state=tk.NORMAL)  
                self.guess_button.config(state=tk.DISABLED) 
        except ValueError:
            self.result_label.config(text="لطفاً یک عدد صحیح وارد کنید.")

    def reset_game(self):
        self.label.destroy()
        self.entry.destroy()
        self.result_label.destroy()
        self.start_game()
        self.restart_button.config(state=tk.DISABLED)  
        self.guess_button.config(state=tk.NORMAL) 

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
