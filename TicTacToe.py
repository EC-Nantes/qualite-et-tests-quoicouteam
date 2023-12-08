def check_winner(plateau) :
    winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
            [0, 4, 8], [2, 4, 6] # diagonals
        ]
    for position in winning_positions :
        if plateau[position[0]] == plateau[position[1]] == plateau[position[2]] != 0:
            print(f"Player{plateau[position[0]]} wins !")
            return
        
