from tkinter import *
from tkinter import messagebox
import hashlib
import json
import os
import subprocess

CONFIG_FILE = "vault_config.json"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def save_password(hashed_pw):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"password": hashed_pw}, f)


def is_password_set():
    return os.path.exists(CONFIG_FILE)


def load_password():
    with open(CONFIG_FILE, "r") as f:
        data = json.load(f)
        return data.get("password", "")


def center_window(window, w, h):
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()
    x = (screen_w // 2) - (w // 2)
    y = (screen_h // 2) - (h // 2)
    window.geometry(f"{w}x{h}+{x}+{y}")


def set_password_screen():
    def save():
        pw = password_entry.get()
        confirm_pw = confirm_entry.get()
        if not pw or not confirm_pw:
            messagebox.showerror("Error", "Please fill both fields.")
            return
        if pw != confirm_pw:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        save_password(hash_password(pw))
        messagebox.showinfo("Success", "Password set!")
        window.destroy()
        login_screen()

    window = Tk()
    window.title("")
    center_window(window, 400, 300)
    window.configure(bg="#1e1e1e")

    frame = Frame(window, bg="#1e1e1e", padx=30, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(
        frame,
        text="Set your password",
        font=("TkFixedFont", 14),
        bg="#1e1e1e",
        fg="white",
    ).pack(pady=10)
    password_entry = Entry(frame, show="*", font=("TkFixedFont", 12))
    password_entry.pack(pady=5)

    Label(
        frame,
        text="Confirm password",
        font=("TkFixedFont", 14),
        bg="#1e1e1e",
        fg="white",
    ).pack(pady=(10, 0))
    confirm_entry = Entry(frame, show="*", font=("TkFixedFont", 12))
    confirm_entry.pack(pady=5)

    Button(
        frame,
        text="Save",
        command=save,
        bg="#4CAF50",
        fg="white",
        font=("TkFixedFont", 12),
        width=17,
    ).pack(pady=15)

    window.mainloop()


def login_screen():
    def check_login():
        entered = password_entry.get()
        if hash_password(entered) == load_password():
            messagebox.showinfo("Access Granted", "Welcome to your vault!")
            window.destroy()
            subprocess.Popen(["python3", "dashboard.py"])
        else:
            messagebox.showerror("Access Denied", "Wrong password.")

    window = Tk()
    window.title("Login")
    center_window(window, 400, 250)
    window.configure(bg="#2c2c2c")

    frame = Frame(window, bg="#2c2c2c", padx=30, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(
        frame,
        text="Enter your password",
        font=("TkFixedFont", 14),
        bg="#2c2c2c",
        fg="white",
    ).pack(pady=10)
    password_entry = Entry(frame, show="*", font=("TkFixedFont", 12))
    password_entry.pack(pady=10)

    Button(
        frame,
        text="Login",
        command=check_login,
        bg="#2196F3",
        fg="white",
        font=("TkFixedFont", 12),
        width=17,
    ).pack(pady=10)

    window.mainloop()


if is_password_set():
    login_screen()
else:
    set_password_screen()
