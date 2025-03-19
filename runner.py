from tictactoe import *

def print_board(board):
    for row in board:
        print(" | ".join([cell if cell is not None else " " for cell in row]))
        print("-" * 9)

def play_game():
    board = initial_state()
    human = input("Do you want to play as X or O? ").upper()
    while human not in [X, O]:
        human = input("Invalid choice. Choose X or O: ").upper()
    
    ai = O if human == X else X

    while not terminal(board):
        print_board(board)
        if player(board) == human:
            print("Your turn! Enter row and column (0, 1, 2) separated by space:")
            while True:
                try:
                    i, j = map(int, input().split())
                    if (i, j) in actions(board):
                        board = result(board, (i, j))
                        break
                    else:
                        print("Invalid move. Try again.")
                except:
                    print("Invalid input. Enter two numbers (0, 1, 2).")
        else:
            print("AI is thinking...")
            move = minimax(board)
            board = result(board, move)

    print_board(board)
    if winner(board):
        print(f"Game Over! {winner(board)} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
