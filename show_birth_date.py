import tkinter as tk
from tkinter import messagebox

def show_birth_date():
    day = day_spinbox.get()
    month = month_spinbox.get()
    year = year_spinbox.get()
    
    birth_date = f"{day}/{month}/{year}"
    messagebox.showinfo("تاریخ تولد", f"تاریخ تولد: {birth_date}")

root = tk.Tk()
root.title("نمایش تاریخ تولد")

day_label = tk.Label(root, text="روز:")
day_label.pack()
day_spinbox = tk.Spinbox(root, from_=1, to=31)
day_spinbox.pack()

month_label = tk.Label(root, text="ماه:")
month_label.pack()
month_spinbox = tk.Spinbox(root, from_=1, to=12)
month_spinbox.pack()

year_label = tk.Label(root, text="سال:")
year_label.pack()
year_spinbox = tk.Spinbox(root, from_=1900, to=2024)
year_spinbox.pack()

show_button = tk.Button(root, text="نمایش تاریخ تولد", command=show_birth_date)
show_button.pack()

root.mainloop()
#وصل باشه ؟؟؟؟؟