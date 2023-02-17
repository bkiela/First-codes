def draw_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    
    
def player_move(player, board):
    while True:
        n = int(input(f"Gracz {player} wybierz swoj ruch (1-9): "))
        if board[n-1] == " ":
            board[n - 1] = player
            break
        else:
            print("Miejsce jest juz zajete. Wybierz inne.")


def winning_moves(board):
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for player in ["X", "O"]:
        for positions in win:
            if all(board[p] == player for p in positions):
                return player
    return None

board = [" " for x in range(9)]
draw_board(board)

winner = None
current_player = "X"
while not winner:
    player_move(current_player, board)
    draw_board(board)
    winner = winning_moves(board)
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    if " " not in board and not winner:
        winner = "Tie"
    
if winner == "Tie":
    print("Gra zakonczyla sie remisem. Nikt nie wygral.")
else:
    print(f"Gratulacje {winner}, wygrales!")
