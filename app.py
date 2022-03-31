board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]   
]

# take board as parameter
# slot a variable

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")   
        print()    

print_board(board)


def quit(usser_input):
    if user_input == "q":reture True
    else:return False

while True:
    user_input = input("Please enter the position from 1 to 9 or enter \"q\" to quit the game")
    