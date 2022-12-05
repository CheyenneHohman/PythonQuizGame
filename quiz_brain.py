#Step 4: Bring up question and ask the user to answer the question
#All of the quiz functionality will happen in this file. 

# 4a. Create another Class: QuizBrain 
class QuizBrain: 
    #4b. Create constructor to initialize the necessary attributes: question number and user score which will have default values and question list which will be passed to the constructor 
    def __init__(self, q_list):
        self.question_number = 0 
        self.score = 0
        self.question_list = q_list

    #4c. Create a Method that retrieves the question from the question_list (Created in main.py) 
    def next_question(self):
        current_question = self.question_list[self.question_number]
        #4d. Lists start at 0, so to display the correct question number for the next step, increase question number by 1 
        self.question_number += 1
        #4e. Show the number, text, and ask for the user's answer 
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        #8e. Advancing to next question, checks answer the user gave 
        self.check_answer(user_answer, current_question.answer)

    #Step 7: Create a methods that advances the question after the user has answered 
    def still_has_questions(self):
        #This method will return a Boolean true/false which advances it until there's no more questions
        return self.question_number < len(self.question_list)

    #Step 8: Create a Methods that will check the answer that the user gives 
    def check_answer(self, user_answer, correct_answer): 
        #8a. Create if/else that compares user & correct answer. Be sure to account for varying case ("true" and "TRUE" etc) in user's answers 
        if user_answer.lower() == correct_answer.lower(): 
            #8b. Increase score by 1
            self.score += 1 
            #8c. Let user know they were correct 
            print("Correct!!")
            #8d. Create else statement 
        else: 
            print("Dang. You got it wrong. :( ")

        #8f. display correct answer. 
        print(f"Correct answer was {correct_answer}.")
        #8g. displays user's score 
        print(f"Your current score is: {self.score}/{self.question_number} ")
        #8h. Create a space between the questions for readability 
        print("\n")