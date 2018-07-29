from required_functions import *


# Take names from user
print('Welcome to TIC TAC TOE 1.0')
player_1 = input('Enter the name of First player: ').upper()
player_2 = input('Enter the name of Second player: ').upper()
clear()

# Take user's prefference for 'X' or 'O'
player_1_case = input('{}, what do you preffer ( X or O ): '.format(player_1)).upper()
while player_1_case != 'X' and player_1_case != 'O':
    print('Invalid Entry. Please try again.')
    player_1_case = input('{}, what do you preffer ( X (as in Xerox) or O (as in Orange) ): '.format(player_1)).upper()
#set other player's prefference automatically
if player_1_case == 'X':
    player_2_case = 'O'
else:
    player_2_case = 'X'
clear()

cases = '{} you are {} and {} you are {}. Lets Begin.'.format(player_1, player_1_case, player_2, player_2_case)
print(cases)



# check if they are ready
# if ready, then start game
# else quit
ready = input('Press YES to start the game and NO to quit: ').upper()

while ready != 'YES' and ready != 'NO':
    print('Invalid Entry. Please try again.')
    ready = input('Press YES to start the game and NO to quit: ').upper()

if ready == 'NO':
    print('Thanks for trying this game.\nWe hope to see you soon.')
else:
    # users are ready
    # start the game
    clear()
    while ready == 'YES':

        board_data = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        count = 1
        win = False
        while count<=9 :
            # it will run 9 times if no user will win
            print(cases,end='\n\n')
            board_print(board_data)
            valid_input = False
            while not valid_input:
                if count%2 == 1:
                    player_turn = input('{}, Enter a number according to reference board: '.format(player_1))
                else:
                    player_turn = input('{}, Enter a number according to reference board: '.format(player_2))

                # check for valid input
                # continue if invalid input
                if not correct_input(player_turn, board_data):

                    if count%2 == 1:
                        print('\n{}, either you have entered a wrong number or the number you entered is already take.\nPlease try again.\n'.format(player_1))
                        continue
                    else:
                        print('\n{}, either you have entered a wrong number or the number you entered is already take.\nPlease try again.\n'.format(player_2))
                        continue
                else:
                    valid_input = True

            # correct input is passed by user
            # place user's input and check if it wins
            player_turn = int(player_turn)
            if count%2 == 1:
                board_data[int((player_turn-1)/3)][(player_turn-1)%3] = player_1_case
                if win_check(board_data,player_turn,player_1_case):
                    clear()
                    print(cases,end='\n\n')
                    board_print(board_data)
                    print('Game Over.\nAnd the winner is {}.'.format(player_1))
                    win = True
                    break
                count += 1
                clear()
            else:
                board_data[int((player_turn - 1) / 3)][(player_turn - 1) % 3] = player_2_case

                if win_check(board_data, player_turn, player_2_case):
                    clear()
                    print(cases, end='\n\n')
                    print('Game Over.\nAnd the winner is {}.'.format(player_2))
                    win = True
                    break
                count += 1
                clear()

        if not win:
            print(cases,end='\n\n')
            board_print(board_data)
            print('Its a Draw.')

        ready = input('Press YES to start the game again and NO to quit: ').upper()

        while ready != 'YES' and ready != 'NO':
            print('Invalid Entry. Please try again.')
            ready = input('Press YES to start the game again and NO to quit: ').upper()

        if ready == 'YES':
            clear()

    else:
        clear()
        print('Thanks for trying this game.\nWe hope to see you soon.')




