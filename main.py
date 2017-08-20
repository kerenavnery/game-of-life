#!/usr/bin/python3

from graphics import *

SQUARE_SIZE = 20

BOARD_WIDTH = 10
BOARD_HEIGHT = 10


def main():
    width = BOARD_WIDTH * SQUARE_SIZE
    height = BOARD_HEIGHT * SQUARE_SIZE

    win = GraphWin("Game of Life", width, height)
    win.getMouse()
    win.close()

main()
