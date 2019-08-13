#!/usr/bin/python3

from graphics import *

from board import Board

SQUARE_SIZE = 10

BOARD_WIDTH = 100
BOARD_HEIGHT = 50

FPS = 1.0

def main():
    width = BOARD_WIDTH * SQUARE_SIZE
    height = BOARD_HEIGHT * SQUARE_SIZE

    win = GraphWin("Game of Life", width, height, autoflush=False)
    game_over_text = "GAME OVER"

    b = Board(win, BOARD_WIDTH, BOARD_HEIGHT)
    b.initiailze()
    update()

    clicked = False
    game_over = False
    while not clicked:
        b.live()
        if (b.get_game_over()):
            for idx, t in enumerate(game_over_text):
                text = Text(Point(500+idx*20, 150), t)
                text.setFill("green")
                text.draw(win)
        update(FPS)
        clicked = win.checkMouse()

    ## TODO: add game over
    win.close()

main()