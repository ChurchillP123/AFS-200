from flask import Flask, render_template, request
import requests
import html
from triviagame import TriviaGame
from triviaquestion import TriviaQuestion

app = Flask(__name__)

def getData(category, number, difficulty):
  try:
    response = requests.get(f'https://opentdb.com/api.php?amount={number}&category={category}&difficulty={difficulty}&type=multiple', timeout=5)
    response.raise_for_status()
    response_JSON = response.json()
    return response_JSON
  except requests.exceptions.HTTPError as errh:
    print(f"HTTPError - {errh}")
  except requests.exceptions.ConnectionError as errc:
    print(f"Connection Error - {errc}")
  except requests.exceptions.Timeout as errt:
    print(f"Timeout - {errt}")
  except requests.exceptions.RequestException as err:
    print(f"Request Exception - {err}")

triviaQuestions = TriviaGame()

def generateTriviaQuestions(category, number, difficulty):
  questions = getData(category, number, difficulty)
  for question in questions["results"]:
    triviaQ = question["question"]
    category = question["category"]
    difficulty = question["difficulty"]
    correctAnswer = question["correct_answer"]
    incorrectAnswers = question["incorrect_answers"]
    triviaQuestion = TriviaQuestion(triviaQ, category, difficulty, correctAnswer, incorrectAnswers)
    triviaQuestions.addTriviaQuestion(triviaQuestion)
       
generateTriviaQuestions(9, 5, 'easy')
allTriviaQuestions = triviaQuestions.getTriviaQuestions()

@app.route("/")
def triviaGame():
  return render_template('questions.html', questions = allTriviaQuestions)

@app.route("/score", methods = ['POST'])
def triviaResults():
  answer1 = html.unescape(request.form['1'])
  answer2 = html.unescape(request.form['2'])
  answer3 = html.unescape(request.form['3'])
  answer4 = html.unescape(request.form['4'])
  answer5 = html.unescape(request.form['5'])
  answers = [answer1, answer2, answer3, answer4, answer5]
  return render_template('results.html', answers = answers, questions = allTriviaQuestions) 

if __name__ == "__main__":
  app.run()