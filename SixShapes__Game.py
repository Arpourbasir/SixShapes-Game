def print_board(board) :
    vals = []
    for i in range(5) :
        for j in range(5) :
            val = board[i][j]
            if val == "   " :
                val = ''
            vals.append(str(val).center(5))
    str_board = f'''
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |{vals[0]}|{vals[1]}|{vals[2]}|{vals[3]}|{vals[4]}|
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |{vals[5]}|{vals[6]}|{vals[7]}|{vals[8]}|{vals[9]}|
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |{vals[10]}|{vals[11]}|{vals[12]}|{vals[13]}|{vals[14]}|
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |{vals[15]}|{vals[16]}|{vals[17]}|{vals[18]}|{vals[19]}|
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    |     |     |     |     |     |
    |{vals[20]}|{vals[21]}|{vals[22]}|{vals[23]}|{vals[24]}|
    |     |     |     |     |     |
    +-----+-----+-----+-----+-----+
    '''
    print(str_board)

def move_ships(board , player_ships , player) :
    print_board(board)
    while True:
        try:
            move = int(input(f"Player {player}, enter ship number (1-3): "))
            if 1 <= move <= 3 :
                current_ship = player_ships[move - 1]
                new_position = (current_ship[0] + 1, current_ship[1])
                if board[new_position[0]][new_position[1]] == "   ":
                    board[current_ship[0]][current_ship[1]] = "   "
                    board[new_position[0]][new_position[1]] = f"P{player}"
                    player_ships[move - 1] = new_position
                    break
                else :
                    print("Invalid move. Destination is occupied.")
            else :
                print("Invalid move. Enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Enter a number.")

def main() :
    rows, cols = 5, 5
    board = [["   " for _ in range(cols)] for _ in range(rows)]
    player1_ships = [(1, 1), (2, 1), (3, 1)]
    player2_ships = [(1, 1), (1, 2), (1, 3)]
    current_player = 1
    while True:
        move_ships(board, player1_ships, current_player)
        if all(board[ship[0]][ship[1]] == "   " for ship in player1_ships):
            print("Player 1 wins!")
            break
        current_player = 3 - current_player
   
    print_board(board)

if __name__ == "__main__":
    main()
