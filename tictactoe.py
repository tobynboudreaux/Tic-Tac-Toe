def display(game_list):
    print("Here is the current board: ")
    print(game_list['0'])
    print(game_list['1'])
    print(game_list['2'])

def row_choice():
    choice = 'wrong'

    while choice not in ['0', '1', '2']:
        choice = input("Pick a row (0, 1, 2): ")

        if choice not in ["0", '1', '2']:
            print("Sorry, invalid choice! ")

    return str(choice)

def replace_choice(game_list, row):
    choice = 'wrong'
    print("You Selected: ")
    print(game_list[row])

    while choice not in ['0', '1', '2']:
        choice = input("Pick a position (0, 1, 2): ")

        if choice not in ["0", '1', '2']:
            print("Sorry, invalid choice! ")

    return [row, int(choice)]

def replace(game_list, position):

    user_in = input("Type string to place (X or Y): ")

    game_list[position[0]][position[1]] = user_in

    return game_list

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice = input('Keep playing? (Y or N) ')

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, please choose Y or N ")

    if choice == 'Y':
        return True
    else: 
        return False

game_on = True
game_list = {
"0": [' ', ' ', ' '],
"1": [' ', ' ', ' '],
"2": [' ', ' ', ' ']
}

while game_on:
    display(game_list)

    row = row_choice()

    position = replace_choice(game_list, row)

    game_list = replace(game_list, position)

    display(game_list)

    game_on = gameon_choice()
