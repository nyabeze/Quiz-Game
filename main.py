from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
print(len(question_data))
for i in range(0, len(question_data)):
    q_text = question_data[i]["text"]
    q_answer = question_data[i]["answer"]
    question_bank.append(Question(q_text, q_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("you've completed the quiz")
print(f"Your final score is{quiz.score}/{quiz.question_number}")
