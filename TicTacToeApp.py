def draw_board(c_list):  # prints board
    print(f'\t Tic-Tac-Toe\n\t=============\n\t| {c_list[0]} | {c_list[1]} | {c_list[2]} |')
    print(f'\t-------------\n\t| {c_list[3]} | {c_list[4]} | {c_list[5]} |')
    print(f'\t-------------\n\t| {c_list[6]} | {c_list[7]} | {c_list[8]} |\n\t-------------')


def get_player_input(player, c_list):  # get players move
    while True:
        player_move = int(input(f'{player[0]}, Where would you like to place your '
                                f'symbol "{player[1]}" in (1-9): '))
        if 0 < player_move < 10:
            if c_list[player_move - 1] == '_':
                return player_move
            else:
                print('Sorry, that spot is already chosen.Try again.')
        else:
            print('That is not a valid spot on the board. Choose again.')


def place_char_on_board(player, player_move, c_list):  # Puts player symbol on the board
    c_list[player_move - 1] = player[1]


def is_winner(pChar, cList):  # Returns a bool if player is winner
    return ((cList[0] == pChar and cList[1] == pChar and cList[2] == pChar) or  # victory in 1st row
            (cList[3] == pChar and cList[4] == pChar and cList[5] == pChar) or
            (cList[6] == pChar and cList[7] == pChar and cList[8] == pChar) or
            (cList[0] == pChar and cList[3] == pChar and cList[6] == pChar) or
            (cList[1] == pChar and cList[4] == pChar and cList[7] == pChar) or
            (cList[2] == pChar and cList[5] == pChar and cList[8] == pChar) or
            (cList[0] == pChar and cList[4] == pChar and cList[8] == pChar) or
            (cList[2] == pChar and cList[4] == pChar and cList[6] == pChar))


def play_again():
    choice = input("Do you want to play again?(Yes/No): ").lower().strip()
    if choice.startswith('n'):
        return False
    else:
        return True


repeat = True
while repeat:
    player1 = ['Player1', 'X']
    player2 = ['Player2', 'O']
    char_list = ['_'] * 9
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    draw_board(num_list)  # Display the Numerical board
    draw_board(char_list)  # Display the empty T-T-T board

    while True:
        # Get Player1's and check if it won
        move = get_player_input(player1, char_list)  # Get Player1's move
        place_char_on_board(player1, move, char_list)  # Put move on board
        draw_board(num_list)  # Display the Num board
        draw_board(char_list)  # Display player's move on the T-T-T board
        # Check if player1 is winner or a tie
        if is_winner(player1[1], char_list):
            print('Player1 wins the board')
            break
        elif "_" not in char_list:
            print('The game is a tie..!')
            break
        # Get Player2's and check if it won
        move = get_player_input(player2, char_list)
        place_char_on_board(player2, move, char_list)  # Put move on board
        draw_board(num_list)  # Display the Num board
        draw_board(char_list)  # Display player's move on the T-T-T board
        # Check if player2 is winner or a tie
        if is_winner(player2[1], char_list):
            print('Player2 wins the board')
            break

    # elif "_" not in char_list:
    #     print('The game is a tie..!')
    #     break

    repeat = play_again()
