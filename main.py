from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
the_card = {}

# ---------------------------- Switch Cards ------------------------------- #
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient='records')

def switch():
    global the_card, flip_timer
    window.after_cancel(flip_timer)
    the_card = random.choice(to_learn)
    canvas.itemconfig(title_text, fill="black", text="French")
    canvas.itemconfig(word_text, fill="black", text=the_card["French"])
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- Flip Card ------------------------------- #
def flip_card():
    global the_card
    canvas.itemconfig(title_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=the_card["English"])
    canvas.itemconfig(canvas_image, image=back_img)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 300, image=front_img)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

correct_img = PhotoImage(file='images/right.png')
correct_button = Button(image=correct_img, highlightthickness=0, command=switch)
correct_button.grid(column=0, row=1)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=switch)
wrong_button.grid(column=1, row=1)

switch()

window.mainloop()
