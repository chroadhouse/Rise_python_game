board = [['', '', ''],
         ['', '', ''],
         ['', '', '']
         ]


def printBoard():
    #The method prints the board out
    print("X 0,1,2")
    print('Y')
    i = 0
    for row in board:
        print(i, row)
        i += 1


def checkWin():
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


def gameLoop():
    #The main game will be play in this
    xPlayer = True
    coordinateList = ['0', '1', '2']
    while True:
        printBoard()
        won, playerWon = checkWin()
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
                    print(board[intX][intY])
                    if board[intX][intY] == "":
                        if xPlayer:
                            board[intX][intY] = 'X'
                            xPlayer = False
                        else:
                            board[intX][intY] = 'Y'
                            xPlayer = True
                    else:
                        print('There is already a piece there')

                else:
                    print('Must be between 0 and 2')
            else:
                print('You must enter X,Y')
        else:
            print('You have not enetered anything')

def main():
    #Could add a menu here ? 
    gameLoop()


main()
