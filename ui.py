from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_text = Label(text=f"Score: 0", bg=THEME_COLOR, foreground="white", highlightthickness=0)
        self.score_text.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text='A wonderful story',
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        img_yes = PhotoImage(file="./images/true.png")
        img_no = PhotoImage(file="./images/false.png")
        self.yes_button = Button(image=img_yes, highlightthickness=0, command=self.yes)
        self.yes_button.grid(column=0, row=2)
        self.no_button = Button(image=img_no, highlightthickness=0, command=self.no)
        self.no_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def yes(self):
        self.get_feedback(self.quiz.check_answer("True"))
        self.score_text.config(text=f"Score: {self.quiz.score}")

    def no(self):
        self.get_feedback(self.quiz.check_answer("False"))
        self.score_text.config(text=f"Score: {self.quiz.score}")

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)