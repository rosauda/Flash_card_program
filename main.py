import pandas as pd
import openpyxl
from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"
df_words = pd.read_excel("german_words.xlsx")
dic_words = df_words.to_dict(orient="records")

# ---------------------------- READING DATA ------------------------------- #

def next_word():
    pass








# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Learning German")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=600, height=400)

# Creating Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=image_front)
canvas.grid(column=0, row=0, columnspan=2)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))


# Buttons

image_wrong = PhotoImage(file="wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0)
button_wrong.grid(row=1, column=0)


image_right = PhotoImage(file="right.png")
button_right = Button(image=image_right, highlightthickness=0)
button_right.grid(row=1, column=1)




window.mainloop()