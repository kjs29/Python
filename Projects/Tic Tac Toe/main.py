from help import check_for_win, check_turn, draw_board, revert
import os

spots = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9",}
turn = 0
playing = True

while playing:
    #os.system("cls" if os.name == "nt" else "clear")
    print("\nboard : ")
    draw_board(spots)
    print(f"< Turn {turn + 1} >")
    print(f"Player {(turn%2)+ 1}'s turn \nplayer 1: X\nplayer 2: O")
    choice = input("Enter your number or press 'q' to quit : ")
    if choice == "q":
        playing = False
    elif choice.isdigit() and int(choice) in spots:
        if spots[int(choice)] not in "XO":
            turn += 1
            spots[int(choice)] = check_turn(turn)
            draw_board(spots)
            if revert():
                spots[int(choice)] = str(int(choice))
                print("reverted completed !")
                draw_board(spots)
                revert_choice = input("Pick a new number : ")
                if int(revert_choice) in spots and spots[int(revert_choice)].isdigit():
                    spots[int(revert_choice)] = check_turn(turn)
                else:
                    print("Invalid input, please try again :)")
                    turn -= 1
        else:
            print("Invalid input, please try again :)")
    else:
        print("Invalid input, please try again :)")
    if check_for_win(spots):
        print(f"\t      Player {(turn%2)} win")
        draw_board(spots)
        break
    elif turn >= 8 and check_for_win(spots) == False:
        print("\t      Tied!")
        draw_board(spots)
        break
print("Thank you for playing")
