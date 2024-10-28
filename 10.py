import tkinter as tk
from tkinter import ttk

def update_units(event):
    if combo.get() == "وزن":
        from_combo['values'] = ["تن", "کیلوگرم", "گرم"]
        to_combo['values'] = ["تن", "کیلوگرم", "گرم"]
    else:  # اگر طول انتخاب شده باشد
        from_combo['values'] = ["متر", "سانتیمتر", "میلی‌متر"]
        to_combo['values'] = ["متر", "سانتیمتر", "میلی‌متر"]

def convert(value, from_unit, to_unit):
    # تبدیل وزن
    if combo.get() == "وزن":
        if from_unit == "تن":
            value *= 1000  # به کیلوگرم
        elif from_unit == "گرم":
            value /= 1000  # به کیلوگرم
        
        if to_unit == "تن":
            return value / 1000
        elif to_unit == "گرم":
            return value * 1000
    
    # تبدیل طول
    else:
        if from_unit == "متر":
            value *= 100  # به سانتیمتر
        elif from_unit == "میلی‌متر":
            value /= 10  # به سانتیمتر
        
        if to_unit == "متر":
            return value / 100
        elif to_unit == "میلی‌متر":
            return value * 10
            
    return value  # اگر همان واحد باشد

def show_selection():
    selection = combo.get()
    from_unit = from_combo.get()
    to_unit = to_combo.get()
    try:
        value = float(entry.get())
        converted_value = convert(value, from_unit, to_unit)
        result_label.config(text=f"نتیجه: {converted_value:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="لطفاً یک عدد معتبر وارد کنید.")

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("انتخاب وزن و طول")

# کمبو باکس نوع
combo = ttk.Combobox(root, values=["وزن", "طول"])
combo.set("نوع را انتخاب کنید")
combo.bind("<<ComboboxSelected>>", update_units)
combo.pack(pady=10)

# فیلد ورودی مقدار
entry = tk.Entry(root)
entry.pack(pady=10)

# کمبو باکس تبدیل از
from_label = tk.Label(root, text="تبدیل از:")
from_label.pack(pady=5)

from_combo = ttk.Combobox(root)
from_combo.pack(pady=10)

# کمبو باکس تبدیل به
to_label = tk.Label(root, text="تبدیل به:")
to_label.pack(pady=5)

to_combo = ttk.Combobox(root)
to_combo.pack(pady=10)

# دکمه نمایش انتخاب
select_button = tk.Button(root, text="نمایش انتخاب", command=show_selection)
select_button.pack(pady=10)

# برچسب نتیجه
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# اجرای حلقه اصلی
root.mainloop()
