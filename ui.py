def ui_print(map):
    for row in map:
        for column in row:
            print(column, end='')

        print('')

def ui_key():        
    return input()

def ui_msg_lost():
    print("Pacman died!")

def ui_msg_win():
    print("You won the game!")