from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        right_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        self.button_right = Button(image=right_image, highlightthickness=0, command=self.checkmark_button_pressed)
        self.button_wrong = Button(image=wrong_image, highlightthickness=0, command=self.x_button_pressed)

        self.button_right.grid(row=2, column=0)
        self.button_wrong.grid(row=2, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Some question text", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text="Score: ", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_wrong.config(state="disabled")
            self.button_right.config(state="disabled")

    def x_button_pressed(self):
        if self.quiz.check_answer("False"):
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def checkmark_button_pressed(self):
        if self.quiz.check_answer("True"):
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def give_feedback(self, feedback):
        if feedback:
            self.canvas.config(bg="green")
            self.window.after(1000, self.next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.next_question)