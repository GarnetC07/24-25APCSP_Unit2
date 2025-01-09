#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
import tkinter.font as tkFont

# main window
root = tk.Tk()
root.wm_geometry("200x200")

# create empty frame (new window for components in root)
frame_login = tk.Frame(root)

#Activate the grid in our new frame
frame_login.grid()

# Widgets for frame_login
normal_font = tkFont.Font(family="Arial", size=12, weight=tkFont.BOLD)
lbl_username = tk.Label(frame_login, text='Username:', font=normal_font, fg="red")
lbl_username.pack(padx=50, pady=50)

# Text Box for username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()


root.mainloop()