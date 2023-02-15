from pacman import *
from ui import *

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

game_finished = False

while not game_finished:
    ui_print(map)
    key = ui_key()
    valid_key, pacman_alive, won = play(map, key)

    move_ghosts(map)

    if not pacman_alive:
        ui_msg_lost()
        game_finished = True
    elif won:
        ui_msg_win()
        game_finished = True