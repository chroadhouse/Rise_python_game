import random

def presenceCheckPass(data):
    if data != '':
        return True
    else:
        return False

def checkWin(board):
    #Method checks if there is a winner and returns true or false and the player that has won
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return True, board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return True, board[i][0]
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != '':
        return True, board[1][1]
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != '':
        return True, board[1][1]

    return False, ''

def printBoard(board):
    #The method prints the board out
    print("X 0,1,2")
    print('Y')
    i = 0
    for row in board:
        print(i, row)
        i += 1

def naughtsAndCrosses():
    board = [['', '', ''],
         ['', '', ''],
         ['', '', '']
         ]
    #The main game will be play in this
    xPlayer = True
    coordinateList = ['0', '1', '2']
    while True:
        printBoard(board)
        won, playerWon = checkWin(board)
        if won:
            print(f'{playerWon} has won the match ')
            break

        if xPlayer:
            userInput = input(
                'Please type where you want X to go giving x,y coordinates')
        else:
            userInput = input(
                'Please type where you want Y to go giving x,y coordinates')
        if userInput:
            if len(userInput) == 3:
                if userInput[0] in coordinateList and userInput[2] in coordinateList:
                    intX = int(userInput[0])
                    intY = int(userInput[2])
                    print(board[intY][intX])
                    if board[intY][intX] == "":
                        if xPlayer:
                            board[intY][intX] = 'X'
                            xPlayer = False
                        else:
                            board[intY][intX] = 'Y'
                            xPlayer = True
                    else:
                        print('There is already a piece there')

                else:
                    print('Must be between 0 and 2')
            else:
                print('You must enter X,Y')
        else:
            print('You have not enetered anything')
    
def answer(a,b):
    return a*b

def randomNumberMultiplier():
    score = 0
    print('This game is going to give you 5 random multiplication questions and you have to give the answer, at the end your score will be show to you')
    # Store the questions and answers in here for the question dictonary 
    questionDict = {}
    playerDict = {}
    for i in range(0,5):
        numOne = random.randint(0,10)
        numTwo = random.randint(0,10)
        questionDict[f'{numOne}x{numTwo}'] = answer(numOne,numTwo)

    for key, value in questionDict.items():
        print('Question: '+key)
        userAnswer = input('Please type your answer here:')
        playerDict[key] = userAnswer

    for key,value in questionDict.items():
        if playerDict[key]==str(questionDict[key]):
            score += 1

    print('You got a score of '+str(score))
    
def quizGame():
    print('You are going to be asked Mutliple Choice questions with the answer being A, B or C')
    quizDict = {
        'Which Musical instrument has 88 keys?,A. Piano,B. Organ,C. Accordian':'A',
        'What is the capital city of France?,A. Berlin,B. Rome,C. Paris':'C',
        'Which planet is closest to the sun?,A. Mercury,B. Venus,C. Earth':'A',
        'Which language is the most widely spoken in the world?,A. English,B. Manderin,C. Spanish':'B',
        'Which animal is the largest living on Earth?,A. Elephant,B. Whale,C. Crocodile':'B'
    }
    
    score = 0
    for key, value in quizDict.items():
        tempList = key.split(',')
        # 0 - Q, 1A, 2B, 3C
        for t in tempList:
            print(t)
        userAnswer = input('Please write which choice you think the answer is:')
        if userAnswer.capitalize() == value:
            score += 1

    print(f'At the end of the Quiz you got a score of :{score}')



def main():
    while True:
        print('This is a menu, enter number to interact with the program')
        print('1. Random number multiplier')
        print('2. Naughts and crosses')
        print('3. Quiz')
        print('4. Close program')
        userInput = input('Choose a number:')

        if presenceCheckPass(userInput):
            if userInput  in ['1','2','3','4']:
                if userInput=='1':
                    randomNumberMultiplier()
                elif userInput =='2':
                    naughtsAndCrosses()
                elif userInput =='3':
                    quizGame()
                elif userInput =='4':
                    break
            else:
                print('Please only enter a number you from the menu options')

        else:
            print('You have not entered anything')

main()