game = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]              #2d array that stores all the players' moves ("-" means that nothing has been placed there yet)

def print_game_board():
    print("\n|" + "-" * 11 + "|")
    for row in game:
        print("| " + " | ".join(row) + " |")
        print("|" + "-" * 11 + "|")
    print("\n")                                     #prints game board nicely (like a normal X and O board but in ascii)

def check_draw():
    draw = False
    for row in game:
        if "-" in row:
            return False
        else:
            draw = True
    return draw

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
    if game[0][0] == sign and game[1][0] == sign and game[2][0] == sign:
        return True
    elif game[0][1] == sign and game[1][1] == sign and game[2][1] == sign:
        return True
    elif game[0][2] == sign and game[1][2] == sign and game[2][2] == sign:
        return True
    else:
        return False
 
def no_space(row, column):
    if game[row][column] == "O" or game[row][column] == "X":
        return True
    else:
        return False                    #checks if there is already a "X" or a "O" on the spot entered by the player

def player(sign):
    while True:
        player = input(f"Where do you want to place (you are {sign}), format: \"0,0\": ")
        player = player.split(",")
        if no_space(int(player[0]), int(player[1])):
            print("There is already another X or O placed on there, choose another location on the board!\n")
        else:
            break
    game[int(player[0])][int(player[1])] = sign
    print_game_board()                              #this function lets the player enter where they want to place the X or the O, and assigns it to that spot on the game board

while True:
    print_game_board()
    while True:
        try:
            player("X")
            break
        except IndexError:
            print("\nYou did not respect the format or you entered an out of bounds spot!\n")
        except ValueError:
            print("\nYou can only enter a location on the board, not anything else!\n")                 #error handling
    if check_row("X"):
        print("\nPlayer X won!\n")
        break                                   #win check
    elif check_col("X"):
        print("\nPlayer X won!\n")
        break
    elif check_across("X"):
        print("\nPlayer X won!\n")
        break
    elif check_draw():
        print("\nIt's a draw!\n")
        break
    while True:
        try:
            player("O")
            break
        except IndexError:
            print("\nYou did not respect the format or you entered an out of bounds spot!\n")
        except ValueError:
            print("\nYou can only enter a location on the board, not anything else!\n")                 #error handling
    if check_row("O"):
        print("\nPlayer O won!r\n")
        break                                   #win check
    elif check_col("O"):
        print("\nPlayer O won!c\n")
        break
    elif check_across("O"):
        print("\nPlayer O won!a\n")
        break
    elif check_draw():
        print("\nIt's a draw!\n")
        break
