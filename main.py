from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- Switch Cards ------------------------------- #
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient='records')

def switch():
    the_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=the_card["French"])
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 300, image=flash_img)
title_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

correct_img = PhotoImage(file='images/right.png')
correct_button = Button(image=correct_img, highlightthickness=0, command=switch)
correct_button.grid(column=0, row=1)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=switch)
wrong_button.grid(column=1, row=1)

switch()

window.mainloop()
