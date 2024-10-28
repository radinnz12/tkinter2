import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel

def add_book():
    book_name = simpledialog.askstring("کتاب جدید", "نام کتاب را وارد کنید:")
    author_name = simpledialog.askstring("نویسنده جدید", "نام نویسنده را وارد کنید:")
    if book_name and author_name:
        listbox.insert(tk.END, f"{book_name} - {author_name}")

def edit_book():
    selected_index = listbox.curselection()
    if selected_index:
        current_entry = listbox.get(selected_index)
        book_name, author_name = current_entry.split(" - ")

        # ایجاد پنجره جدید برای ویرایش
        edit_window = Toplevel(root)
        edit_window.title("ویرایش کتاب")
        edit_window.geometry("300x150")

        tk.Label(edit_window, text="نام کتاب:").pack(pady=5)
        book_entry = tk.Entry(edit_window)
        book_entry.insert(0, book_name)
        book_entry.pack(pady=5)

        tk.Label(edit_window, text="نام نویسنده:").pack(pady=5)
        author_entry = tk.Entry(edit_window)
        author_entry.insert(0, author_name)
        author_entry.pack(pady=5)

        def save_changes():
            new_book_name = book_entry.get()
            new_author_name = author_entry.get()
            if new_book_name and new_author_name:
                listbox.delete(selected_index)
                listbox.insert(selected_index, f"{new_book_name} - {new_author_name}")
                edit_window.destroy()
            else:
                messagebox.showwarning("هشدار", "لطفا نام کتاب و نویسنده را وارد کنید.")

        save_button = tk.Button(edit_window, text="ذخیره تغییرات", command=save_changes)
        save_button.pack(pady=10)

    else:
        messagebox.showwarning("هشدار", "لطفا یک کتاب را انتخاب کنید.")

def delete_book():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
    else:
        messagebox.showwarning("هشدار", "لطفا یک کتاب را انتخاب کنید.")

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("مدیریت کتابخانه")
root.geometry("400x250")
root.resizable(False, False)  # غیرقابل تغییر اندازه

# ایجاد لیست‌نمای خالی
listbox = tk.Listbox(root)
listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# دکمه‌های عملیاتی
btn_add = tk.Button(root, text="اضافه کردن کتاب", command=add_book)
btn_add.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

btn_edit = tk.Button(root, text="ویرایش کتاب", command=edit_book)
btn_edit.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

btn_delete = tk.Button(root, text="حذف کتاب", command=delete_book)
btn_delete.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

# تنظیم توزیع فضای خالی
root.grid_rowconfigure(0, weight=1)  # لیست باکس بزرگتر شود
root.grid_columnconfigure(0, weight=1)  # دکمه‌ها هم‌سطح باشند

# اجرای حلقه اصلی برنامه
root.mainloop()
