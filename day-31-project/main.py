BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
ITALIC = "italic"
BOLD = "bold"

from tkinter import *
import pandas
import random

current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(410, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=(FONT, 40, ITALIC))
card_word = canvas.create_text(400, 263, text="Word", font=(FONT, 60, BOLD))
canvas.grid(row=0, column=0, columnspan=2)

x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=is_known)
correct_button.grid(row=1, column=1)

next_card()

window.mainloop()
