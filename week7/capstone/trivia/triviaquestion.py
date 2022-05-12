import random
import html

class TriviaQuestion:
    id = 0

    def __init__(self, question, category, difficulty, correctAnswer, incorrectAnswers):
        self.question = question,
        self.category = category, 
        self.difficulty = difficulty, 
        self.correctAnswer = correctAnswer,
        self.incorrectAnswers = incorrectAnswers,
        TriviaQuestion.id += 1
        self.id = TriviaQuestion.id
    def getQuestion(self):
        return html.unescape(''.join(self.question))
    def getCategory(self):
        return html.unescape(''.join(self.category))
    def getDifficulty(self):
        return self.difficulty
    def getCorrectAnswer(self):
        return html.unescape(''.join(self.correctAnswer))
    def getIncorrectAnswers(self):
        return self.incorrectAnswers
    def getID(self):
        return self.id
    def getShuffledAnswers(self):
        correctAnswer = list(html.unescape(self.correctAnswer))
        for answers in self.incorrectAnswers:
            for answer in answers:
                correctAnswer.append(html.unescape(answer))
        random.shuffle(correctAnswer)
        return correctAnswer