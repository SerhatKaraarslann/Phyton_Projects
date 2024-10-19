# Quiz App

#Questin Class
#   Instance Attributes
#       -text, choices, answer
#   Instance Methods
#       -checkAnswer("python") => True or False


#Quiz Class
#   Instance Attributes
#       -question, questionIndex, score
#   Instance Methods
#       - getquestion()         => Get question according to questionIndex 
#       - displayQuestion()     => Show the instance of getQuestion()
#       - loadQuestion()        => Start test
#       - displayScore()        => Show score 
#       -displayProgress()      => show the progress


import quiz,question


quiz = quiz.Quiz(question.questions)
quiz.loadQuestion()
    