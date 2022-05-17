"""tictactoe game for 2 players"""

choices=[]
for x in range (1, 10) :
    choices.append(str(x))

playerOneTurn = True
winner = False


def printBoard() : #creates the board with print statements
    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')


while winner == False : #game continues if condition is met
    printBoard()

    if playerOneTurn : #prints next player's turn
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input(">> ")) #player enters number to play their X or O
    except ValueError:
        print("please enter a valid field") #if input is not a number, it notifies the player
        continue

    if choices[choice - 1] == 'X' or choices [choice - 1] == 'O': #if spot already has an X or 0, it notifies the player
        print("illegal move, please try again")
        continue

    if playerOneTurn :
        choices[choice - 1] = 'X' #player 1 is X
    else :
        choices[choice - 1] = 'O' #player 2 is 0

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) : #determines winner if 3 Xs or 0s are in a row
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) : #if all conditions are true, there is a winner
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) : #if all conditions are true, there is a winner
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or #checks diagonals
       (choices[2] == choices[4] and choices[4] == choices[6])) : #if all conditions are true, there is a winner
        winner = True
        printBoard()

# segment added for ties
    tie = 0
    for i in range(9):
        if choices[i] == 'O' or choices[i] == 'X':
            tie += 1 #each 'O' or 'X' on the board adds one to the counter
        if tie == 9: #if there are 9 'X's and 'O's on the board, the game must be a tie
            print("It is a tie.") #tie output
            exit()


print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n") #winner output