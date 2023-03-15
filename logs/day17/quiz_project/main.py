
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


for question in question_data:
    question = Question(question["text"], question["answer"])
    question_bank.append(question)


#question_bank is a list of objects, therefore print(question_bank[0]['text']) 
#will not work because the object is not subscriptable.
#print(question_bank[0].text)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
