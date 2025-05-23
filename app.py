import random
plays = [["","",""], ["","",""], ["","",""]]
def board(plays):
    for i in range(len(plays)):
        print(" | ".join(plays[i]))
        if i == len(plays) - 1:
            break
        print("------")

def play(position, player):
    row = position // 3
    column = position % 3
    if plays[row][column]:
        return False
    plays[row][column] = player
    return True

def check_winner():
    for row in plays:
        if row[0] and row[0] == row[1]  == row[2]:
            return True
    for i in range(3):
        if plays[0][i] and plays[0][i] == plays[1][i]  == plays[2][i]:
            return True
    if plays[0][0] and plays[0][0] == plays[1][1] == plays[2][2]:
        return True
    if plays[0][2] and plays[0][2] == plays[1][1] == plays[2][0]:
        return True
    return False

def tie_checker():
    for row in plays:
        if row[0] == "" or row[1] == "" or row[2] == "":
            return False
    return not check_winner()

def multiplayer_game():
    turn = 0
    while True:
        print(board(plays))
        player = "X" if turn % 2 == 0 else "O"
        try:
            position = int(input(f"Player {player} Choose your position (0-8): "))
        except ValueError:
            print("Please enter a number from 0 to 8.")
            continue
        if play(position, player):
            turn += 1
        if check_winner():
            print(board(plays))
            print(f"{player} won !!!")
            break
        if tie_checker():
            print(board(plays))
            print("Its a tie!")
            break

def play_against_computer():
    turn = 0
    while True:
        try:
            position = int(input(f"Player X, Choose your position (0-8): "))
        except ValueError:
            print("Please enter a number from 0 to 8")
            continue
        if not play(position, "X"):
            print("That spot is taken")
            continue
        turn += 1
        if check_winner():
            print(board(plays))
            print("You won !!!")
            break
        if tie_checker():
            print(board(plays))
            print("Its a tie!")
            break

        empty_positions = [i for i in range(9) if plays[i // 3][i % 3] == ""]
        if empty_positions:
            position = random.choice(empty_positions)
            play(position, "O")
            print(board(plays))
            print(f"Computer chose position{position}")
            turn += 1
        if check_winner():
            print(board(plays))
            print("Computer won !!!")
            break
        if tie_checker():
            print(board(plays))
            print("Its a tie!")
            break
        


mode = input("Play against Player (1) or Computer(2)?")
if mode == "1":
    multiplayer_game()
elif mode == "2":
    play_against_computer()
else:
    print("We don't have such mode yet")


