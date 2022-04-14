secretWord = 'professor'
guessLetters = []
num_of_guesses = 0

wordBoard = []
for letter in range(len(secretWord)):
    wordBoard.append('_')

def showBoard():
    print(' '.join(wordBoard))

def checkGuess(guessL):
    guessL = guessL.lower()
    index = secretWord.find(guessL)
    
    if(index > -1):
        indices = [i for i in range(len(secretWord)) if secretWord[i] == guessL]
        for i in indices:
            wordBoard[i] = guessL
        if (secretWord.count(guessL) > 1):
            print(f"Yes there are {secretWord.count(guessL)} {guessL} ")
        else:
            print(f"Yes there is a {guessL}")
        guessLetters.append(guessL)
        return True
    else:
        print(f"Im sorry but there is no letter {guessL} in the word")
        guessLetters.append(guessL)
        return False

def split(word):
    return [char for char in word]

def guessingGame():
    print("Can you guess the secret password?")
    showBoard()
    global num_of_guesses
    while(num_of_guesses < 5):
        guessLetter = input("Guess a Letter: ").lower()
        
        while(guessLetter in guessLetters):
            guessLetter = input("Guess Another Letter: ")
        if (checkGuess(guessLetter)):
            showBoard()
            if (not '_' in wordBoard):
                print("Congratulations, You Won!")
                break
        else:
            num_of_guesses += 1
            print(f"You have {5 - num_of_guesses} chances left")
            showBoard()
            if(num_of_guesses > 4):
                print(f"Game Over! The secret word was...{secretWord}")

guessingGame()