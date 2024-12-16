from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    new_question = Question(q["question"], q["correct_answer"])
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_question():
    new_quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {new_quiz.score}/{new_quiz.question_number}.")