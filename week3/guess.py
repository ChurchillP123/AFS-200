secretWord = 'justice'
guessLetters = []
num_of_guesses = 0

wordBoard = []
for letter in range(len(secretWord)):
    wordBoard.append('_')

def showBoard():
    print(wordBoard)

def checkGuess(guessL):
    index = secretWord.find(guessL)
   
    if(index.isdigit() and index != -1):
        indices = [i for i in range(len(secretWord)) if secretWord[i] == guessL]
        for i in indices:
            wordBoard.replace(i, guessL)
        guessLetters.append(guessL)
        return True
    else:
        return False

print(wordBoard)

def guessingGame():
    guessLetter = input("Guess a Letter: ")
    while(wordBoard.index(guessLetter) > 1):
        guessLetter = input("Guess Another Letter: ")
    if (checkGuess(guessLetter)):
        showBoard()
    else:
        num_of_guesses += 1
        if(num_of_guesses > 5):
            print(f"Game Over! The secret word was...{secretWord}")








