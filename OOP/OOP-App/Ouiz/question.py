
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("Answer is not in Choices!")
        if(self.answer == answer):
            print("True")
            return True
        else:
            print("False")
            return False
        

q1 = Question("What is the most beautiful program language?",["Python","C#","Java","Dart"],"Python")
q2 = Question("What is the most popular program language?",["C#","Java","Python","Dart"],"Python")
q3 = Question("What is the most dynamic program language?",["C#","Java","Dart","Python"],"Python") 


questions = [q1,q2,q3]