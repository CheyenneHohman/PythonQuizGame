# Step 1: Create a question model (Class)

# Create a Class that can be used as a constructor to build new questions 

class Question: 
    # Use dunder method __init__ to create a functioning class that is a constructor
    # Set up two attributes for the question: question text and answer 

    def __init__(self, q_text, q_answer):
        # be sure to use the "self" syntax to be able to refer back to the object to access the attributes later 
        self.text = q_text
        self.answer = q_answer

    # Test to make sure it is functioning properly
# new_q = Question("Are you ready for this quiz?!!!", "False, lol")
# print(new_q.text)
# print(new_q.answer)
