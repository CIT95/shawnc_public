import dice
import shelve
import re
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Dungeon Dice")


def button_d4():
    d4 = dice.roll('d4')
    messagebox.showinfo("Result", "You rolled a " + str(d4))
    Label(root, text=d4)
    return


def button_d6():
    d6 = dice.roll('d6')
    messagebox.showinfo("This is my Popup!", "You rolled a " + str(d6))
    Label(root, text=d6)
    return


def button_d8():
    d8 = dice.roll('d8')
    messagebox.showinfo("This is my Popup!", "You rolled a " + str(d8))
    Label(root, text=d8)
    return


def button_d12():
    d12 = dice.roll('d12')
    messagebox.showinfo("This is my Popup!", "You rolled a " + str(d12))
    Label(root, text=d12)
    return


def button_d20():
    d20 = dice.roll('d20')
    messagebox.showinfo("This is my Popup!", "You rolled a " + str(d20))
    Label(root, text=d20)
    return


def button_d100():
    d100 = dice.roll('d100')
    messagebox.showinfo("This is my Popup!", "You rolled a " + str(d100))
    Label(root, text=d100)
    return

# Define Buttons

button_d4 = Button(root, text="d4", padx=42, pady=20, command= button_d4)
button_d6 = Button(root, text="d6", padx=42, pady=20, command= button_d6)
button_d8 = Button(root, text="d8", padx=42, pady=20, command= button_d8)
button_d12 = Button(root, text="d12", padx=40, pady=20, command= button_d12)
button_d20 = Button(root, text="d20", padx=40, pady=20, command= button_d20)
button_d100 = Button(root, text="d100", padx=36, pady=20, command= button_d100)

# Put the buttons on the screen

button_d4.grid(row=2, column=0)
button_d6.grid(row=2, column=1)
button_d8.grid(row=2, column=2)
button_d12.grid(row=3, column=0)
button_d20.grid(row=3, column=1)
button_d100.grid(row=3, column=2)


root.mainloop()
