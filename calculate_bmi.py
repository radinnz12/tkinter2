import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  
        bmi = weight / (height ** 2)
        messagebox.showinfo("نتیجه BMI", f"BMI شما: {bmi:.2f}")
        messagebox.showinfo("پیام", "از محاسبه BMI شما خوشحالیم!")
    except ValueError:
        messagebox.showerror("خطا", "لطفاً وزن و قد معتبر وارد کنید.")

root = tk.Tk()
root.title("محاسبه BMI")

tk.Label(root, text="وزن (کیلوگرم):").grid(row=0, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

tk.Label(root, text="قد (سانتی‌متر):").grid(row=1, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="محاسبه BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2)

root.mainloop()
