import tkinter as tk
import random

# لیست رنگ‌ها
colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"]

class ColorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Game")

        self.score = 0
        self.current_color = ""
        self.time_remaining = 30  # زمان باقی‌مانده

        self.label = tk.Label(root, text="Guess the color!", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Helvetica", 18))
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(root, text=f"Time: {self.time_remaining}", font=("Helvetica", 18))
        self.timer_label.pack(pady=10)

        self.color_button = tk.Button(root, text="Show Color", command=self.show_color, font=("Helvetica", 18))
        self.color_button.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 18))
        self.entry.pack(pady=20)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_color, font=("Helvetica", 18))
        self.submit_button.pack(pady=20)

        self.restart_button = tk.Button(root, text="Restart Game", command=self.restart_game, font=("Helvetica", 18))
        self.restart_button.pack(pady=20)
        self.restart_button.config(state=tk.DISABLED)

        self.is_timer_running = False

    def show_color(self):
        self.current_color = random.choice(colors)
        random_color = self.current_color
        while random_color == self.current_color:
            random_color = random.choice(colors)

        # به‌روزرسانی برچسب با رنگ جدید
        self.label.config(text=self.current_color, fg=random_color)
        self.entry.delete(0, tk.END)

        if not self.is_timer_running:  # شروع تایمر اگر در حال اجرا نیست
            self.start_timer()

    def start_timer(self):
        self.is_timer_running = True
        self.time_remaining = 30
        self.update_timer()

    def update_timer(self):
        if self.time_remaining > 0:
            self.timer_label.config(text=f"Time: {self.time_remaining}")
            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()  # پایان بازی اگر زمان تمام شود

    def check_color(self):
        # بررسی اینکه آیا رنگ متن با حدس کاربر مطابقت دارد
        if self.entry.get().lower() == self.label.cget("fg"):  # مقایسه با رنگ متن
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.label.config(text="Correct! Guess the color again!")
            
            if self.score >= 5:
                self.end_game()
        else:
            self.label.config(text="Wrong! Try again!")

    def end_game(self):
        self.label.config(text="Game Over! Final Score: {}".format(self.score))
        self.color_button.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.NORMAL)
        self.is_timer_running = False  # غیرفعال کردن تایمر

    def restart_game(self):
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.label.config(text="Guess the color!")
        self.timer_label.config(text="Time: 30")  # ریست تایمر
        self.color_button.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)
        self.is_timer_running = False  # غیرفعال کردن تایمر

if __name__ == "__main__":
    root = tk.Tk()
    game = ColorGame(root)
    root.mainloop()
