
my_first_game = ['  - ',' - ',' - ',
                 '  - ',' - ',' - ',
                 '  - ',' - ',' - '  ]

#first create a game bord
# switsh turn of the user and input the value
# select the winner of the game
#
game_is_going = True
num = '  X '
def the_board():

    print(my_first_game[0] +'|'+ my_first_game[1]+'|'+my_first_game[2]+
        '\n'  +my_first_game[3]+'|'+ my_first_game[4]+'|'+my_first_game[5]+
         '\n' +my_first_game[6]+'|'+ my_first_game[7]+'|'+my_first_game[8])
    return

def input_number():
    global num
    global game_is_going

    while game_is_going:

        user_input = input('To run the game...\nTo exit enter "q" or "quit"....\ninput number from 1-9:')
        if user_input == 'q' or 'quit' :
            quit()


        # check wether user input between 1-9

        user_in = int(user_input)-1
        if user_in in [0,1,2,3,4,5,6,7,8]:
            if my_first_game[user_in] == '  O ' or my_first_game[user_in] == '  X ':
                print("\n\tThe number u entered has already a value.......select another number.......\n")
                # if number has already a value
                input_number()
            else:
                my_first_game[user_in] = num

        elif user_in not in [0,1,2,3,4,5,6,7,8]:
            print('\n\tThe value u entered not found........select another value.........\n')
            input_number()

        the_board()
        switch_user()
        check_if_win()
    return


# switch the turn of users.......
def switch_user():
    global num
    if num == '  X ':
        num = '  O '
    elif num == '  O ':
        num = '  X '
    return


def check_if_win():
    global game_is_going
# =============================================================================
#
# =============================================================================
    column =[ my_first_game[0] == my_first_game  [1] == my_first_game[2] !=' - ',
              my_first_game[3] == my_first_game[4]== my_first_game[5] !=' -' ,
               my_first_game[6] == my_first_game  [7] == my_first_game[8] !=' - ' , ]

    row = [ my_first_game[0] == my_first_game[3] == my_first_game[6] !=' - ' ,
            my_first_game[1] == my_first_game[4] == my_first_game[7] !=' - ',
              my_first_game[2] == my_first_game[5] == my_first_game[8] !=' - ', ]

    diagonal = [my_first_game[0] == my_first_game[4] == my_first_game[8] !=' - ' ,
                my_first_game[2] == my_first_game[4] == my_first_game[6] !=' - ' ]
# =============================================================================
#
# =============================================================================
    # find the winner name
    if num == '  X ':
        winner = '  O '

    elif num == '  O ':
        winner = '  X '
    # just for finding winnner of the game above 5 lines
# =============================================================================
#
# =============================================================================
    for column_ in column :
        if column_ == True:
            print('\n', winner ,'winner.',)
            game_is_going = False

    for row_ in row :
        if row_ == True:
            print('\n', winner ,'winner.',)
            game_is_going = False

    for diagonal_ in diagonal :
        if diagonal_ == True :
            print('\n', winner ,'winner.',)
            game_is_going = False

    return

def check():
    return




def run_game():

   the_board()
   input_number()

   return

run_game()
