import tkinter as tk
from tkinter import messagebox

def on_yes_click():
    messagebox.showinfo("Ответ", "Я так и знал")
    yes_button.config(state=tk.DISABLED)
    no_button.config(state=tk.DISABLED)

def on_no_click():
    pass

root = tk.Tk()
root.title("Ты гей?")

yes_button = tk.Button(root, text="Да", command=on_yes_click)
yes_button.pack()

no_button = tk.Button(root, text="Нет", command=on_no_click)
no_button.pack()

root.mainloop()