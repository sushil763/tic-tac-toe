
# import only system from os
from os import system, name

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')








# This will check if number is possible
# Returns True if possible
# Return False if number is invalid or position is already taken
def correct_input(num,data):
    try:
        num = int(num)
    except ValueError:
        return False
    #check for valid number
    if num>=1 and num<=9:
        # to check according to [[0,1,2],[3,4,5],[6,7,8]]
        # because it will give row when int(num/3) and column when num%3
        num -= 1
        d = int(num/3)
        r = num%3
        if data[d][r] == ' ':
            return True
        else:
            return False
    else:
        return False







# takes 3 arguments
# list in which you have to check
# number to check current position
# turn to match
# check if any player wins
def win_check(data, num, turn):
    r = int((num-1)/3)
    c = (num-1)%3

    if data[r][0] == turn and data[r][1] == turn and data[r][2] == turn:
        return True
    if data[0][c] == turn and data[1][c] == turn and data[2][c] == turn:
        return True
    count_1 = 0
    count_2 = 0
    for p in range(3):
        for q in range(3):
            if p+q == r+c:
                if data[p][q] == turn:
                    count_1 += 1
            if p-q == r-c:
                if data[p][q] == turn:
                    count_2 += 1
    if count_1 == 3 or count_2 == 3:
        return True
    else:
        return False







#print current board
def board_print(data):

    board = [['\t','\t',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','\t','\t','\t','\t',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
             ['\t','\t',' ', data[0][0], ' ', '|', ' ', data[0][1], ' ', '|', ' ', data[0][2], ' ', '\t', '\t', '\t', '\t', ' ', '1', ' ', '|', ' ','2', ' ', '|', ' ', '3', ' '],
             ['\t','\t',' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\t', '\t', '\t', '\t',' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
             ['\t','\t','-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '\t', '\t', '\t', '\t', '-', '-', '-', '|', '-','-', '-', '|', '-', '-', '-'],
             ['\t','\t',' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\t', '\t', '\t', '\t', ' ', ' ', ' ', '|', ' ',' ', ' ', '|', ' ', ' ', ' '],
             ['\t','\t',' ', data[1][0], ' ', '|', ' ', data[1][1], ' ', '|', ' ', data[1][2], ' ', '\t', '\t', '\t', '\t',' ', '4', ' ', '|', ' ', '5', ' ', '|', ' ', '6', ' '],
             ['\t','\t',' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\t', '\t', '\t', '\t', ' ', ' ', ' ', '|', ' ',' ', ' ', '|', ' ', ' ', ' '],
             ['\t','\t','-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '\t', '\t', '\t', '\t', '-', '-', '-', '|', '-','-', '-', '|', '-', '-', '-'],
             ['\t','\t',' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\t', '\t', '\t', '\t', ' ', ' ', ' ', '|', ' ',' ', ' ', '|', ' ', ' ', ' '],
             ['\t','\t',' ', data[2][0], ' ', '|', ' ', data[2][1], ' ', '|', ' ', data[2][2], ' ', '\t', '\t', '\t', '\t',' ', '7', ' ', '|', ' ', '8', ' ', '|', ' ', '9', ' '],
             ['\t','\t',' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\t', '\t', '\t', '\t', ' ', ' ', ' ', '|', ' ',' ', ' ', '|', ' ', ' ', ' ']
             ]
    print('Reference Board is shown on right.\n\n')
    for r in board:
        for c in r:
            print(c,end='')
        print()
    print('\n\n')