board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]   
]

# take board as parameter
# slot a variable

def print_board(board):  #board input parameter internal variable as passed in as parameter
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")   
        print()    

print_board(board)


def quit(user_input):
    if user_input.lower() == "q":
        print("Thank you for playing")
        return True
    else:return False

def check_input(user_input):
    isnum(user_input)

def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not valid number!")
        return False
    else: return True    

while True:
    user_input = input("Please enter the position from 1 to 9 or enter \"q\" to quit the game: ")
    if quit(user_input):break
