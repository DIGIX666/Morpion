import tkinter


# Winner
def display_winner():
    # print("Winner is", player)
    winner.config(text="Winner is " + player)

# Player turn
def player_turn():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


# Check winner
def check_winner(clicked_row, clicked_column):
    
    # Check rows
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]
        
        if current_button["text"] == player:
            count += 1
    if count == 3:
        display_winner()
        return
    
    
    # Check columns
    count = 0
    for i in range(3):
        current_button = buttons[clicked_column][i]
        
        if current_button["text"] == player:
            count += 1
    if count == 3:
        display_winner()
        return
    
    
    # Check diagonals
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        
        if current_button["text"] == player:
            count += 1
    if count == 3:
        display_winner()
        return
    


# Place Symnols in the grid
def place_symbol(row, column):

    clicked_button = buttons[column][row]
    if clicked_button["text"] == "":
        clicked_button.config(text=player)

    check_winner(row, column)
    player_turn()

# Create the grid for the game
def draw_grid():
    for  column in range(3):
        buttons_in_grid = []
        for row in range(3):
            button = tkinter.Button(
                root, 
                font=("Arial", 50),
                width=5, height=3,
                command=lambda r=row, c=column: place_symbol(r, c)
                )
            button.grid(row= row, column= column)
            buttons_in_grid.append(button)
        buttons.append(buttons_in_grid)

# Stock
buttons = []
player = "X"

# Create the window for game
root = tkinter.Tk() 

# Personalize the window
root.title("Morpion")
root.minsize(500, 500)
winner = tkinter.Label(root, text="", font=("Arial", 20))
winner.grid(row=3, column=1)
draw_grid()
root.mainloop()