#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
import tkinter.font as tkFont

# main window
root = tk.Tk()
root.wm_geometry("500x200")

# create empty frame (new window for components in root)
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)

frame_login.grid(column="0", row="0", sticky="news")
frame_auth.grid(column="0", row="0", sticky="news")

#Activate the grid in our new frame
frame_login.grid()

def login():
    frame_auth.tkraise()


# Widgets for frame_login
normal_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)
lbl_username = tk.Label(frame_login, text='Username:', font=normal_font, fg="red")
lbl_username.pack(padx=50)

# Text Box for username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()

# Widgets for frame_login
normal_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)
lbl_username = tk.Label(frame_login, text='Password:', font=normal_font, fg="red")
lbl_username.pack(padx=50)

# Text Box for username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()

button_login = tk.Button(frame_login, text="Login", command=login)
button_login.pack(pady=10)

lbl_authorized = tk.Label(frame_auth, text='Authorized Screen', font=('Times 14'))
lbl_authorized.pack(padx=50)

frame_login.tkraise()
root.mainloop()