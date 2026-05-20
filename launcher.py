import tkinter as tk
from tkinter import filedialog
import subprocess
import sys
import os

def open_main_app():
    launcher.destroy()
    subprocess.Popen([sys.executable, "main_app.py"])

def open_code_helper():
    # Open file picker GUI
    file_path = filedialog.askopenfilename(
        title="Select Helper File",
        filetypes=[("LeScript Helper", "*.helper"), ("All Files", "*.*")]
    )

    if not file_path:
        return  # user cancelled

    launcher.destroy()
    subprocess.Popen([sys.executable, "code_helper.py", file_path])

def exit_launcher():
    launcher.destroy()

launcher = tk.Tk()
launcher.title("LeScript Launcher")
launcher.geometry("400x300")
launcher.configure(bg="#1e1e1e")
launcher.resizable(True, True)

title = tk.Label(
    launcher,
    text="LeScript",
    font=("Segoe UI", 20, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=20)

btn_main = tk.Button(
    launcher,
    text="Open Main App",
    font=("Segoe UI", 14),
    width=20,
    command=open_main_app,
    bg="#2d2d2d",
    fg="white",
    activebackground="#3a3a3a",
    activeforeground="white",
    relief="flat"
)
btn_main.pack(pady=10)

btn_helper = tk.Button(
    launcher,
    text="Open Code Helper",
    font=("Segoe UI", 14),
    width=20,
    command=open_code_helper,
    bg="#2d2d2d",
    fg="white",
    activebackground="#3a3a3a",
    activeforeground="white",
    relief="flat"
)
btn_helper.pack(pady=10)

btn_exit = tk.Button(
    launcher,
    text="Exit",
    font=("Segoe UI", 14),
    width=20,
    command=exit_launcher,
    bg="#2d2d2d",
    fg="white",
    activebackground="#3a3a3a",
    activeforeground="white",
    relief="flat"
)
btn_exit.pack(pady=10)

launcher.mainloop()