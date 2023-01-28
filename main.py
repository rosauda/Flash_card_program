import random

import pandas
import pandas as pd
import openpyxl
from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"
TIME_TO_THINK = 3  # time to think in seconds
current_card = {}
dic_words = {}

try:
    data = pd.read_excel("data\words_to_learn.xlsx")
except FileNotFoundError:
    original_data = pd.read_excel("data\german_words.xlsx")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- READING DATA ------------------------------- #

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(TIME_TO_THINK * 1000, func=flip_card)


# ---------------------------- FLIP CARD ------------------------------- #

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


# ---------------------------- UPDATING DECK ------------------------------- #


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data\words_to_learn.csv", index=False)
    next_word()


# ---------------------------- UI SETUP ------------------------------- #

# Creating window
window = Tk()
window.title("Learning German")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=600, height=400)

flip_timer = window.after(TIME_TO_THINK * 1000, func=flip_card)

# Creating Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="card_front.png")
card_back_image = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# Buttons
image_wrong = PhotoImage(file="wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=next_word)
button_wrong.grid(row=1, column=0)

image_right = PhotoImage(file="right.png")
button_right = Button(image=image_right, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

next_word()

window.mainloop()
