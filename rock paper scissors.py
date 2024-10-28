import tkinter as tk
import random
def play(choice):
    options = ["سنگ", "کاغذ", "قیچی"]
    computer_choice = random.choice(options)
    if choice == computer_choice:
        result.set("نتیجه: تساوی!")
    elif (choice == "سنگ" and computer_choice == "قیچی") or \
         (choice == "کاغذ" and computer_choice == "سنگ") or \
         (choice == "قیچی" and computer_choice == "کاغذ"):
        result.set("نتیجه: شما برنده شدید!")
    else:
        result.set("نتیجه: کامپیوتر برنده شد!")
    computer_label.config(text=f"انتخاب کامپیوتر: {computer_choice}")
root = tk.Tk()
root.title("بازی سنگ کاغذ قیچی")
result = tk.StringVar()
result.set("نتیجه: ")
tk.Button(root, text="سنگ", command=lambda: play("سنگ")).pack(pady=10)
tk.Button(root, text="کاغذ", command=lambda: play("کاغذ")).pack(pady=10)
tk.Button(root, text="قیچی", command=lambda: play("قیچی")).pack(pady=10)
computer_label = tk.Label(root, text="")
computer_label.pack(pady=10)
result_label = tk.Label(root, textvariable=result)
result_label.pack(pady=10)
root.mainloop()
