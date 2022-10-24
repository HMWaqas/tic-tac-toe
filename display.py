import os


def display_board(slotes):
    os.system("clear")
    print("\n\t\tWelcom to tic tac toe game")
    print("\n\n\n\t\t -----------------------")
    print(f"\t\t|{slotes[1]}|{slotes[2]}|{slotes[3]}|")
    print("\t\t -----------------------")
    print(f"\t\t|{slotes[4]}|{slotes[5]}|{slotes[6]}|")
    print(" \t\t -----------------------")
    print(f"\t\t|{slotes[7]}|{slotes[8]}|{slotes[9]}|")
    print("\t\t -----------------------")


def print_congrats():
    print("\n\t\t*******************************")
    print("\t\t********   CONGRATS   *********")
    print("\t\t*******************************")
