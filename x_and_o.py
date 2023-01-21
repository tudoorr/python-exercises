game = [["", "", ""], ["", "", ""], ["", "", ""]]

def print_game_board():
    for row in game:
        print(str(row))
 
def check_row(row, sign):
    if game[row][0] == sign and game[row][1] == sign and game[row][2] == sign:
        return True
    else:
        return False
 
def check_col(column, sign):
    if game[column][0] == sign and game[column][1] == sign and game[column][2] == sign:
        return True
    else:
        return False
 
def no_space(row, column):
    if len(game[row][column]) != 0:
        return True
    else:
        return False

def player(sign):
    while True:
        player = input(f"Where do you want to place (you are {sign}), format: \"0,0\": ")
        player = player.split(",")
        if no_space(int(player[0]), int(player[1])):
            print("There is already another X or O placed on there, choose another location on the board!\n")
        break
    game[int(player[0])][int(player[1])] = sign
    print_game_board()

print_game_board()
while True:
    while True:
        try:
            player("X")
            break
        except IndexError:
            print("You did not respect the format so something went wrong!\n")
        except ValueError:
            print("You can only enter a location on the board, not anything else!\n")
    if check_row(0, "X") or check_row(1, "X") or check_row(2, "X"):
        print("Player X won!\n")
        break
    elif check_col(0, "X") or check_col(1, "X") or check_col(2, "X"):
        print("Player X won!\n")
        break
    while True:
        try:
            player("O")
            break
        except IndexError:
            print("You did not respect the format so something went wrong!\n")
        except ValueError:
            print("You can only enter a location on the board, not anything else!\n")
    if check_row(0, "O") or check_row(1, "O") or check_row(2, "O"):
        print("Player O won!\n")
        break
    elif check_col(0, "O") or check_col(1, "O") or check_col(2, "O"):
        print("Player O won!\n")
        break
#needs cross win checking and check win optimizing
