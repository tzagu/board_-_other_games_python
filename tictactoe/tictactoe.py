
import numpy as np

size = 3

board = np.empty((size, size), dtype=object)
moves = np.empty((size, size), dtype=object)

for i in range(size):
    for j in range(size):
        board[i][j]=str(((size*i)+j)+1)
        moves[i][j]='_'

isFilled = lambda x, y: x==y

def oneWon(moves):
    isMatched = False
    for i in range(size-2):
        for j in range(size-2):
            if (moves[i][j]==moves[i+1][j]==moves[i+2][j] or moves[i][j]==moves[i][j+1]==moves[i][j+2] or moves[i][j]==moves[i+1][j+1]==moves[i+2][j+2]) and moves[i][j]!='_':
                isMatched = True
                print(f'\n ---------------> Player {moves[i][j]} won! <---------------')
                break
            elif (moves[i+1][j]==moves[i+1][j+1]==moves[i+1][j+2] or moves[i][j+2]==moves[i+1][j+2]==moves[i+2][j+2]) and moves[i+1][j+2]!='_':
                isMatched = True
                print(f'\n ---------------> Player {moves[i+1][j+2]} won! <---------------')
                break
            elif (moves[i+2][j]==moves[i+2][j+1]==moves[i+2][j+2] or moves[i+2][j]==moves[i+1][j+1]==moves[i][j+2]) and moves[i+2][j]!='_':
                isMatched = True
                print(f'\n ---------------> Player {moves[i+2][j]} won! <---------------')
                break
            elif (moves[i][j+1]==moves[i+1][j+1]==moves[i+2][j+1]) and moves[i][j+1]!='_':
                isMatched = True
                print(f'\n ---------------> Player {moves[i][j+1]} won! <---------------')
                break
    return isMatched


filled = []
print('\n Welcome to Tic Tac Toe!')
print('\n Following are the selections you have. pick a number and hit enter to replace the game board position with your key')
print(board)
print('\n \n - Game Board -')
print(moves)
player = 'X'

while not isFilled(len(filled), size*size) and not oneWon(moves):
    print(f'\n Turn of player {player}')
    index = int(input())
    if index in filled:
        print('\n invalid selection')
    else:
        if 1 <= index <= size*size:
            if index%size==0:
                row = int(index/size) - 1
                col = size-1
            else:
                row = int(index/size)
                col = index%size - 1
            board[row][col]= '_'
            moves[row][col]=player
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print('\n invalid selection')    
        filled.append(index)
        print('\n \n Remaining moves')
        print(board)
        print('\n \n - Game Board - \n')
        print(moves)

print('\n Game over')
print(board)

