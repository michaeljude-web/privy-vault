from tkinter import *

def show_content(section):
    for widget in content_frame.winfo_children():
        widget.destroy()

    Label(
        content_frame,
        text=f"{section}",
        font=("TkFixedFont", 20),
        bg="#1e1e1e",
        fg="white"
    ).pack(pady=30)

def logout():
    exit()

def dashboard():
    root = Tk()
    root.title("Vault Dashboard")
    root.geometry("1280x720")
    root.configure(bg="#1e1e1e")
    root.resizable(False, False)

    sidebar = Frame(root, width=240, bg="#121212", height=720)
    sidebar.pack(side=LEFT, fill=Y)

    global content_frame
    content_frame = Frame(root, bg="#1e1e1e")
    content_frame.pack(side=RIGHT, expand=True, fill=BOTH)

    Label(
        sidebar,
        text=" PRIVY VAULT",
        bg="#121212",
        fg="white",
        font=("TkFixedFont", 20),
        pady=30
    ).pack()

    buttons = [
        ("  Picture", "Picture"),
        ("  Video", "Video"),
        ("  File", "File"),
        ("  Settings", "Settings"),
        ("  Logout", "Logout")
    ]

    for text, section in buttons:
        if section == "Logout":
            btn = Button(
                sidebar,
                text=text,
                font=("TkFixedFont", 13),
                bg="#1e1e1e",
                fg="white",
                activebackground="#333333",
                activeforeground="white",
                bd=0,
                padx=20,
                pady=12,
                anchor="w",
                command=logout
            )
        else:
            btn = Button(
                sidebar,
                text=text,
                font=("TkFixedFont", 13),
                bg="#1e1e1e",
                fg="white",
                activebackground="#333333",
                activeforeground="white",
                bd=0,
                padx=20,
                pady=12,
                anchor="w",
                command=lambda s=section: None
            )
        btn.pack(fill=X, padx=20, pady=4)

    show_content("Picture")

    root.mainloop()

if __name__ == "__main__":
    dashboard()

