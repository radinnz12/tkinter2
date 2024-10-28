import tkinter as tk
from tkinter import ttk
import time
import random

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("ساعت دیجیتال")

previous_minute = -1  # نگهداری دقیقه قبلی برای تشخیص تغییر دقیقه

# پوسته‌های مختلف
themes = {
    "روز": {"bg": "white", "fg": "black"},
    "شب": {"bg": "black", "fg": "white"},
    "تابستان": {"bg": "#ffef96", "fg": "#ff5722"},
    "زمستان": {"bg": "#bbdefb", "fg": "#0d47a1"},
    "پاییز": {"bg": "#ffcc80", "fg": "#d84315"},
    "بهار": {"bg": "#c8e6c9", "fg": "#388e3c"}
}

# فونت‌ها
fonts = ["Helvetica", "Courier", "Times", "Arial"]

# تابعی برای به‌روزرسانی زمان و پس‌زمینه
def update_time():
    global previous_minute
    
    current_time = time.strftime("%H:%M:%S")
    current_day = time.strftime("%A, %B %d, %Y")
    hour, minute, second = current_time.split(':')

    # تغییر رنگ پس‌زمینه بر اساس پوسته انتخابی
    theme = theme_var.get()
    bg_color = themes[theme]["bg"]
    fg_color = themes[theme]["fg"]

    root.configure(bg=bg_color)
    hour_label.config(bg=bg_color, fg=fg_color)
    minute_label.config(bg=bg_color)
    second_label.config(bg=bg_color, fg=fg_color)
    colon_label1.config(bg=bg_color, fg=fg_color)
    colon_label2.config(bg=bg_color, fg=fg_color)
    day_label.config(bg=bg_color, fg=fg_color)

    # تغییر رنگ دقیقه با هر تغییر دقیقه
    if int(minute) != previous_minute:
        new_color = random_color()
        minute_label.config(fg=new_color, bg=bg_color)
        previous_minute = int(minute)

    hour_label.config(text=hour)
    minute_label.config(text=minute)
    second_label.config(text=second)
    day_label.config(text=current_day)
    
    root.after(1000, update_time)  # به‌روزرسانی هر 1 ثانیه

# تابعی برای تولید رنگ تصادفی
def random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)

# تغییر فونت بر اساس انتخاب کاربر
def change_font(event):
    selected_font = font_var.get()
    hour_label.config(font=(selected_font, 72))
    minute_label.config(font=(selected_font, 72))
    second_label.config(font=(selected_font, 72))
    colon_label1.config(font=(selected_font, 72))
    colon_label2.config(font=(selected_font, 72))
    day_label.config(font=(selected_font, 36))

# ایجاد لیبل‌ها برای نمایش ساعت، دقیقه و ثانیه با رنگ‌های مختلف
hour_label = tk.Label(root, font=('Helvetica', 72))
hour_label.pack(side='left')

colon_label1 = tk.Label(root, text=":", font=('Helvetica', 72))
colon_label1.pack(side='left')

minute_label = tk.Label(root, font=('Helvetica', 72))
minute_label.pack(side='left')

colon_label2 = tk.Label(root, text=":", font=('Helvetica', 72))
colon_label2.pack(side='left')

second_label = tk.Label(root, font=('Helvetica', 72))
second_label.pack(side='left')

day_label = tk.Label(root, font=('Helvetica', 36))
day_label.pack(anchor='center')

# منو برای انتخاب پوسته
theme_var = tk.StringVar(value="روز")
theme_menu = ttk.OptionMenu(root, theme_var, "روز", *themes.keys())
theme_menu.pack(anchor='ne')

# منو برای انتخاب فونت
font_var = tk.StringVar(value="Helvetica")
font_menu = ttk.OptionMenu(root, font_var, "Helvetica", *fonts, command=change_font)
font_menu.pack(anchor='nw')

# فراخوانی تابع برای نمایش اولیه زمان و به‌روزرسانی
update_time()

# اجرای حلقه اصلی برنامه
root.mainloop()
