import time
from data import question_data
from tkinter import Tk, Canvas, PhotoImage, Label, Button
import random


win = Tk()
win.title("Quizler App")
win.config(padx=50, pady=50, bg="gray", width=300, height=400)
count = 3
score = 0

question_number = random.choice(question_data)
question_text = question_number["question"]
question_answer = question_number["correct_answer"]
print(question_number)

canvas = Canvas(width=275, height=300, highlightthickness=0, bg="white")
canvas.grid(column=1, row=1, columnspan=2, pady=30)
label_question = canvas.create_text(137.5, 150, text=question_text, width=250, font=("Arial", 15, "normal"))
score_label = Label(text=f"Score: {score}", font=("Arial", 10, "bold"), bg="yellow")
score_label.grid(column=2, row=0, sticky="e")


def check_answer():
    global score
    global question_number
    if question_answer == 'True':
        canvas.config(bg="green")
        score += 1
        score_label.config(text=f"Score: {score}")
        win.after(2000, lambda: update_question())
    else:
        canvas.config(bg="red")
        win.after(2000, lambda: update_question())


def false_answer():
    global score
    global question_number
    if question_answer == 'False':
        canvas.config(bg="green")
        score += 1
        score_label.config(text=f"Score: {score}")
        win.after(2000, lambda: update_question())
    else:
        canvas.config(bg="red")
        win.after(2000, lambda: update_question())


def update_question():
    global question_number
    global question_answer
    question_number = random.choice(question_data)
    question_answer = question_number["correct_answer"]
    canvas.itemconfig(label_question, text=question_number["question"])
    canvas.config(bg="white")


tru_img = PhotoImage(file="../quizler/images/true.png")
true_button = Button(image=tru_img, highlightthickness=0, padx=20, command=check_answer)
true_button.grid(column=1, row=3)

false_img = PhotoImage(file="../quizler/images/false.png")
false_button = Button(image=false_img, highlightthickness=0, command=false_answer)
false_button.grid(column=2, row=3, rowspan=2)

win.mainloop()
