from ui import ui_print

# @ -> our hero
# G -> ghosts
# P -> pills
# . -> empety spaces
# | and - -> walls;

map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|"
]

def find_pacman(map):
    pacman_x = -1 
    pacman_y = -1

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y

def move_pacman(map, next_pacman_x, next_pacman_y):
    pacman_x, pacman_y = find_pacman(map)

    # the place where the pacman was is now empety
    everything_to_the_left = map[pacman_x][0:pacman_y]
    everything_to_the_right = map[pacman_x][pacman_y+1:]
    map[pacman_x] = everything_to_the_left + "." + everything_to_the_right

    # the new place has the pacman
    everything_to_the_left = map[next_pacman_x][0:next_pacman_y]
    everything_to_the_right = map[next_pacman_x][next_pacman_y+1:]
    map[next_pacman_x] = everything_to_the_left + "@" + everything_to_the_right

def play(map, key):
    next_x, next_y = next_position(map, key)

    #if it is a invalid key
    is_an_invalid_key = next_x == -1 and next_y == -1
    if is_an_invalid_key:
        return False

    is_within_borders = within_borders(map, next_x, next_y)
    if not is_within_borders:
        return False

    move_pacman(map, next_x, next_y)

def within_borders(map, next_x, next_y):
    number_of_rows = len(map)
    x_is_valid = 0 <= next_x < number_of_rows

    number_of_columns = len(map[0])
    y_is_valid = 0 <= next_y < number_of_columns 

    return x_is_valid and y_is_valid

def next_position(map, key):
    x, y = find_pacman(map)

    next_x = -1
    next_y = -1

    if key == 'a':
        next_x = x
        next_y = y - 1

    elif key == 'd':
        next_x = x
        next_y = y + 1
    elif key == 'w':
        next_x = x - 1
        next_y = y
    elif key == 's':
        next_x = x + 1
        next_y = y

    return next_x, next_y

ui_print(map)
play(map, 'd')
print("*********")

ui_print(map)
play(map, 'd')
print("*********")

ui_print(map)
play(map, 'd')
print("*********")
ui_print(map)