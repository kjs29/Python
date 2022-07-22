def draw_board(spot):
    board = f"\t\t|{spot[1]}|{spot[2]}|{spot[3]}|\n\t\t|{spot[4]}|{spot[5]}|{spot[6]}|\n\t\t|{spot[7]}|{spot[8]}|{spot[9]}|"
    print(board)

def check_turn(turn):
    if turn % 2 == 0: return "O"
    else: return "X"

def check_for_win(spot):
    if     (spot[1] == spot[2] == spot[3]) \
        or (spot[4] == spot[5] == spot[6]) \
        or (spot[7] == spot[8] == spot[9]) :
        return True
    elif   (spot[1] == spot[4] == spot[7]) \
        or (spot[2] == spot[5] == spot[8]) \
        or (spot[3] == spot[6] == spot[9]) :
        return True
    elif   (spot[1] == spot[5] == spot[9]) \
        or (spot[3] == spot[5] == spot[7]) :
        return True
    else:
        return False

def revert(spots, choice, turn):
    revert_choice = input("Do you want to revert? (Y/N) : ").lower()
    if revert_choice == "y":
        spots[int(choice)] = str(int(choice))
        print("reverted completed !")
        draw_board(spots)
        revert_choice = int(input("Pick a new number : "))
        spots[revert_choice] = check_turn(turn)
        draw_board(spots)
    elif revert_choice == "n":
        pass
