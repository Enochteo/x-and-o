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


