game = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]              #2d array that stores all the players' moves ("-" means that nothing has been placed there yet)

def print_game_board():
    print("\n|" + "-" * 11 + "|")
    for row in game:
        print("| " + " | ".join(row) + " |")
        print("|" + "-" * 11 + "|")
    print("\n")                                     #prints game board nicely (like a normal X and O board but with ascii borders)

def check_draw():
    for row in game:
        if "-" in row:
            return False
    return True

def check_across(sign):
    if game[0][0] == sign and game[1][1] == sign and game[2][2] == sign:
        return True
    elif game[0][2] == sign and game[1][1] == sign and game [2][0] == sign:
        return True
    else:
        return False

def check_row(sign):
    for i in range(len(game) - 1):
        if game[i][0] == sign and game[i][1] == sign and game[i][2] == sign:
            return True
        else:
            return False

def check_col(sign):
    for i in range(len(game) - 1):
        column = [row[i] for row in game]
        if column[0] == sign and column[1] == sign and column[2] == sign:
            return True
        else:
            column.clear()
    return False
 
def check_space(row, column):
    if game[row][column] == "O" or game[row][column] == "X":
        return True
    else:
        return False                    #checks if there is already a "X" or a "O" on the spot entered by the player, but if there's "-" it will return false

def player(sign):
    while True:
        player = input(f"Where do you want to place (you are {sign}), format: \"0,0\": ")
        player = player.split(",")
        if check_space(int(player[0]), int(player[1])):
            print("There is already another X or O placed on there, choose another location on the board!\n")
        else:
            break
    game[int(player[0])][int(player[1])] = sign
    print_game_board()                              #this function lets the player enter where they want to place the X or the O, and assigns it to that spot on the game board

print_game_board()

while True:
    while True:
        player_turn = "X"
        try:
            player(player_turn)
            break
        except IndexError:
            print("\nYou did not respect the format or you entered an out of bounds spot!\n")
        except ValueError:
            print("\nYou can only enter a location on the board, not anything else!\n")                 #error handling
    if check_row(player_turn):
        print("\nPlayer X won!\n")
        break
    elif check_col(player_turn):
        print("\nPlayer X won!\n")
        break
    elif check_across(player_turn):
        print("\nPlayer X won!\n")
        break                                   #win check
    elif check_draw():
        print("\nIt's a draw!\n")
        break
    while True:
        player_turn = "O"
        try:
            player(player_turn)
            break
        except IndexError:
            print("\nYou did not respect the format or you entered an out of bounds spot!\n")
        except ValueError:
            print("\nYou can only enter a location on the board, not anything else!\n")                 #error handling
    if check_row(player_turn):
        print("\nPlayer O won!r\n")
        break
    elif check_col(player_turn):
        print("\nPlayer O won!c\n")
        break
    elif check_across(player_turn):
        print("\nPlayer O won!a\n")
        break                                   #win check
    elif check_draw():
        print("\nIt's a draw!\n")
        break
