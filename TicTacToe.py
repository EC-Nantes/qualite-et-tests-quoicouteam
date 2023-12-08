def check_winner(plateau) :
    winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
            [0, 4, 8], [2, 4, 6] # diagonals
        ]
    for position in winning_positions :
        if plateau[position[0]] == plateau[position[1]] == plateau[position[2]] != 0:
            print(f"Player{plateau[position[0]]} wins !")
            return(True)
    return(False)
        
def game() :
    game_over = False
    plateau = [0]*9
    i = 0
    while not game_over and i < 9 :
        for row in [plateau[j*3:(j+1)*3] for j in range(3)]:
            print("|".join(map(str, row)))
            print("-"*9)
        position = input(f"Player {i%2+1}, enter the position (1-9): ")
        position = int(position)
        while plateau[position-1] != 0 :
            position = input("Position invalide, enter new position (1-9) :")
            position = int(position)
        position = int(position)
        plateau[position-1] = i%2+1
        game_over = check_winner(plateau)
        i = i+1 
        
