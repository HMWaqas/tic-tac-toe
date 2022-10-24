from itertools import cycle
import display

slotes = {
    1: "\t",
    2: "\t",
    3: "\t",
    4: "\t",
    5: "\t",
    6: "\t",
    7: "\t",
    8: "\t",
    9: "\t",
}
players = cycle([1, 2])
currentPlayer = 1


def get_available_slotes():
    return list(dict(filter(lambda value: value[1] == "\t", slotes.items())).keys())


def set_next_player():
    global currentPlayer
    currentPlayer = next(players)


def set_slot(index):
    slotes[int(index)] = f"  p{currentPlayer}   "


def decalre_result(result):
    display.print_congrats
    print(f"\n\tPLAYER {currentPlayer} WON by combination {result[0]}")
    print("\t\t\tGame Ended")


def check_win():
    combinations = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 5, 9),
        (3, 5, 7),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
    )
    return tuple(
        filter(
            lambda combination: slotes[combination[0]]
            == slotes[combination[1]]
            == slotes[combination[2]]
            != "\t",
            combinations,
        )
    )


def get_user_input():
    availableslotes = get_available_slotes()
    print(f"\n\n\t\t\tplayer {currentPlayer}\n")
    print("Choose an empty slot from ", availableslotes, " :"),
    position = input()
    while int(position) not in availableslotes:
        print("invalid input, please choose from", availableslotes)
        position = input()
    return position


def start():
    for i in range(len(slotes) + 1):
        display.display_board(slotes)
        result = check_win()
        if len(result):
            decalre_result(result)
            break
        set_next_player()
        index = get_user_input()
        set_slot(index)


start()
