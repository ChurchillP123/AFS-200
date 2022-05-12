class TriviaGame():
    def __init__(self):
        self.triviaQuestions = []
    def addTriviaQuestion(self, triviaQ):
        self.triviaQuestions.append(triviaQ)
    def getTriviaQuestions(self):
        return self.triviaQuestions