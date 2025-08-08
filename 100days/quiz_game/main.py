from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

if __name__ == "__main__":

    # Create a list of questions
    question_bank = []
    for item in question_data:
        question_bank.append(Question(**item))
    
    # Create quiz
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()

    # Show final score
    print("You've completed the quiz")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}\n")