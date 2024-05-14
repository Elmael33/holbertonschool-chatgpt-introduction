#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Changer la longueur de la ligne pour correspondre à la taille du tableau

def check_winner(board):
    # Vérifier les lignes et colonnes
    for i in range(3):
        # Vérifier la ligne i
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        # Vérifier la colonne i
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    
    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == " ":
                        board[row][col] = player
                        break
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid input. Row and column must be between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        if player == "X":
            player = "O"
        else:
            player = "X"

    print_board(board)
    print("Player " + player + " wins!")

tic_tac_toe()
