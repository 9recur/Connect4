#Created by Abhinav Arya (2015)
#This program simulates the popular game Connect Four
numRow = ' 0  1  2  3  4  5  6'
row0 = [' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' ]
row1 = [' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' ]
row2 = [' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' ]
row3 = [' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' ]
row4 = [' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' ]
row5 = [' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' , ' . ' ]
gameBoard = [row0, row1, row2, row3, row4, row5] # list of the entire connect four board

player1 = input('Player X, enter your name: ')
player2= input('Player O, enter your name: ')

def gameSetup(player):
    '''gameSetup(player) -> int
    asks player what column they want to play in
    returns the int'''
    if player is player1:
        playerTurnInput = input(player1 + ', you\'re X. What column do you want to play in? ')
    else:
        playerTurnInput = input(player2 + ', you\'re O. What column do you want to play in? ')
    while not playerTurnInput.isdigit() or int(playerTurnInput) < 0 or int(playerTurnInput) > 6:
        playerTurnInput = input('Please enter a valid column number (0 - 6): ')
    columnNumber = int(playerTurnInput) # the column that the player wants to put his coin
    return columnNumber

def playerTurn(player):
    '''playerTurn(player) -> (list, dict)
    plays a turn of either player
    modifies the gameboard and return a dictionary containing the position of the new piece'''
    rowCounter = 5
    if player is player1: 
        columnNumber = gameSetup(player1)
    else:
        columnNumber = gameSetup(player2)
    while ' . ' not in gameBoard[rowCounter][columnNumber]: # if the bottom row is full
        if rowCounter <= 0:
            print('This column is full. Please choose a different column')
            if player is player1:
                columnNumber = gameSetup(player1) # ask again
            else:
                columnNumber = gameSetup(player2)
            rowCounter = 5 # reset column number
        else:
            rowCounter = rowCounter - 1 # move up 1 row
    if player is player1:
        gameBoard[rowCounter][columnNumber] = 'X '
        positionP1 = {}
        positionP1['rowNum'] = rowCounter
        positionP1['columnNum'] = columnNumber
        return (gameBoard, positionP1)
    else:
        gameBoard[rowCounter][columnNumber] = 'O '
        positionP2 = {}
        positionP2['rowNum'] = rowCounter
        positionP2['columnNum'] = columnNumber
        return (gameBoard, positionP2)

def vertCheck(position, player, connect):
    '''vertCheck(position, player) -> bool
    checks for a connect 4 vertically'''
    if player is player1: # player 1
        for checker in range(1,4): # number 1 - 3
            # checking up and down
            if position['rowNum'] > 0 and position['rowNum'] - checker >= 0: # can't be at the top
                if 'X ' in gameBoard[position['rowNum'] - checker][position['columnNum']]:
                    connect = connect + 1
            if position['rowNum'] < 5 and position['rowNum'] + checker <= 5: # can't be at the bottom
                if 'X ' in gameBoard[position['rowNum'] + checker][position['columnNum']]:
                    connect = connect + 1
    else: # player 2
        for checker in range(1,4): # number 1 - 3
            # checking up and down
            if position['rowNum'] > 0 and position['rowNum'] - checker >= 0: # can't be at the top
                if 'O' in gameBoard[position['rowNum'] - checker][position['columnNum']]:
                    connect = connect + 1
            if position['rowNum'] < 5 and position['rowNum'] + checker <= 5: # can't be at the bottom
                if 'O' in gameBoard[position['rowNum'] + checker][position['columnNum']]:
                    connect = connect + 1
    if connect == 4:
        return True
    else:
        return False

def horizCheck(position, player, connect):
    '''horizCheck(position, player) -> bool
    checks for a connect 4 horizontally'''
    if player is player1: # player 1
        for checker in range(1,4): # number 1 - 3
            # checking left and right
            if position['columnNum'] > 0 and position['columnNum'] - checker >= 0: # can't be at the far left
                if 'X ' in gameBoard[position['rowNum']][position['columnNum'] - checker]:
                    connect = connect + 1
            if position['columnNum'] < 6 and position['columnNum'] + checker <= 6: # can't be at the far right
                if 'X ' in gameBoard[position['rowNum']][position['columnNum'] + checker]:
                    connect = connect + 1
    else: # player 2
        for checker in range(1,4): # number 1 - 3
            # checking left and right
            if position['columnNum'] > 0 and position['columnNum'] - checker >= 0: # can't be at the far left
                if 'O' in gameBoard[position['rowNum']][position['columnNum'] - checker]:
                    connect = connect + 1
            if position['columnNum'] < 6 and position['columnNum'] + checker <= 6: # can't be at the far right
                if 'O' in gameBoard[position['rowNum']][position['columnNum'] + checker]:
                    connect = connect + 1
    if connect == 4:
        return True
    else:
        return False

def rightDiagCheck(position, player, connect):
    '''rightDiagCheck(position, player) -> bool
    checks for a connect 4 diagonally right'''
    if player is player1: # player 1
        for checker in range(1,4):
            # checking right diagonal
            if position['rowNum'] > 0 and position['columnNum'] < 6 and position['rowNum'] - checker >= 0 and position['columnNum'] + checker <= 6: # no top right
                if 'X ' in gameBoard[position['rowNum'] - checker][position['columnNum'] + checker]:
                    connect = connect + 1
            if position['rowNum'] < 5 and position['columnNum'] > 0 and position['rowNum'] + checker <= 5 and position['columnNum'] - checker >= 0: # no bottom left
                if 'X ' in gameBoard[position['rowNum'] + checker][position['columnNum'] - checker]:
                    connect = connect + 1
    else: # player 2
        for checker in range(1,4):
            # checking right diagonal
            if position['rowNum'] > 0 and position['columnNum'] < 6 and position['rowNum'] - checker >= 0 and position['columnNum'] + checker <= 6: # no top right
                if 'O' in gameBoard[position['rowNum'] - checker][position['columnNum'] + checker]:
                    connect = connect + 1
            if position['rowNum'] < 5 and position['columnNum'] > 0 and position['rowNum'] + checker <= 5 and position['columnNum'] - checker >= 0: # no bottom left
                if 'O' in gameBoard[position['rowNum'] + checker][position['columnNum'] - checker]:
                    connect = connect + 1
    if connect == 4:
        return True
    else:
        return False

def leftDiagCheck(position, player, connect):
    '''leftDiagCheck(position, player) -> bool
    checks for a connect 4 diagonally left'''
    if player is player1: # player 1
        for checker in range(1,4):
            # checking right diagonal
            if position['rowNum'] > 0 and position['columnNum'] > 0 and position['rowNum'] - checker >= 0 and position['columnNum'] - checker >= 0: # no top left
                if 'X ' in gameBoard[position['rowNum'] - checker][position['columnNum'] - checker]:
                    connect = connect + 1
            if position['rowNum'] < 5 and position['columnNum'] < 6 and position['rowNum'] + checker <= 5 and position['columnNum'] + checker <= 6: # no bottom right
                if 'X ' in gameBoard[position['rowNum'] + checker][position['columnNum'] + checker]:
                    connect = connect + 1
    else: # player 2
        for checker in range(1,4):
            # checking right diagonal
            if position['rowNum'] > 0 and position['columnNum'] > 0 and position['rowNum'] - checker >= 0 and position['columnNum'] - checker >= 0: # no top left
                if 'O' in gameBoard[position['rowNum'] - checker][position['columnNum'] - checker]:
                    connect = connect + 1
            if position['rowNum'] < 5 and position['columnNum'] < 6 and position['rowNum'] + checker <= 5 and position['columnNum'] + checker <= 6: # no bottom right
                if 'O' in gameBoard[position['rowNum'] + checker][position['columnNum'] + checker]:
                    connect = connect + 1
    if connect == 4:
        return True
    else:
        return False

def updateBoard():
    # display blank board
    print('\n' + numRow)
    for rows in gameBoard:
        print(*rows)
    print()

    # initialize connect 4 player 1
    connectVertP1 = 1
    connectHorizP1 = 1
    conectRightDiagP1 = 1
    connectLeftDiagP1 = 1

    # initialize connect 4 player 2
    connectVertP2 = 1
    connectHorizP2 = 1
    conectRightDiagP2 = 1
    connectLeftDiagP2 = 1

    boardCounter = 0 # initialize number of coins in the board
    drawState = False

    # loop to play game
    while True:
        # Player 1
        (gameBoardP1, positionP1) = playerTurn(player1)
        print()
        print(numRow)
        # display board after player 1 input
        for rows in gameBoardP1:
            print(*rows) # prints out the individual elements of every row
        print()
        # connect 4 checks
        vertP1 = vertCheck(positionP1, player1, connectVertP1)
        horizP1 = horizCheck(positionP1, player1, connectHorizP1)
        rightDiagP1 = rightDiagCheck(positionP1, player1, conectRightDiagP1)
        leftDiagP1 = leftDiagCheck(positionP1, player1, connectLeftDiagP1)
        if vertP1 or horizP1 or rightDiagP1 or leftDiagP1 is True:
            winningPlayer = player1 # store winning player
            break
        boardCounter = boardCounter + 1 # increment number of positions filled in the board
        # check if the game is a draw
        if boardCounter == 42:
            drawState = True
            break
        
        # Player 2
        (gameBoardP2, positionP2) = playerTurn(player2)
        print()
        print(numRow)
        # display board after player 2 input
        for rows in gameBoardP2:
            print(*rows) # prints out the individual elements of every row
        print()
        # connect 4 checks
        vertP2 = vertCheck(positionP2, player2, connectVertP2)
        horizP2 = horizCheck(positionP2, player2, connectHorizP2)
        rightDiagP2 = rightDiagCheck(positionP2, player2, conectRightDiagP2)
        leftDiagP2 = leftDiagCheck(positionP2, player2, connectLeftDiagP2)
        if vertP2 or horizP2 or rightDiagP2 or leftDiagP2 is True:
            winningPlayer = player2 # store winning player
            break
        boardCounter = boardCounter + 1 # increment number of positions filled in the board
        # check if the game is a draw
        if boardCounter == 42:
            drawState = True
            break

    # end game decisions
    if drawState is True:
        print("The game is a draw.")
    else:
        print('Congratulations, ' + winningPlayer + ', you won!')
    
updateBoard()
