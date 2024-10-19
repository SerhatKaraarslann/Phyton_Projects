import question,random
class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions,len(questions))
        self.questionIndex = 0
        self.score = 0
       
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question =  self.getQuestion()

        print(f"Question : {self.questionIndex + 1} : {question.text}")
    
        for q in question.choices:
            print("-" + q)

        answer = input("answer :")
        if((question.checkAnswer(answer))):
            self.score += 1


        self.questionIndex += 1
        self.loadQuestion()

    
    
    def loadQuestion(self):
        
         if len(self.questions) == self.questionIndex:
            self.displayScore()
         else:
            self.displayProgress()
            self.displayQuestion()
           
    
  
    def displayScore(self):
        point = 100/len(self.questions)
        totalPoint = round(self.score * point)
        print(f"You answered {self.score} questions correctly from {len(self.questions)}.")
        print(f"Score : {totalPoint}")

    def displayProgress(self):
       totalQuestion = len(self.questions)
       questionNumber = self.questionIndex + 1

       print(f"You are on the {questionNumber}. question out of {totalQuestion} questions!".center(100,"*"))
