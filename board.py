from random import randrange

from graphics import Point, Rectangle

class Board():

    def __init__(self, window, width, height, cell_size=20):
        self.window = window
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self._initialize()

    def _initialize(self):
        self.cells = self.blank_field(0)
        self.recs = self.blank_field(None)

        for x, y in self.allpos():
            rec = \
                Rectangle(
                    Point(x * self.cell_size, y * self.cell_size),
                    Point((x + 1) * self.cell_size, (y + 1) * self.cell_size))
            rec.setFill('black')
            rec.draw(self.window)
            self.recs[y][x] = rec

        self.randomize()

    def randomize(self):
        for x, y in self.allpos():
            self.cells[y][x] = randrange(2)

            color = "black" if self.cells[y][x] else "white"
            self.recs[y][x].setFill(color)

    def allpos(self):
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)

    def blank_field(self, default_value):
        return [[default_value for _ in range(self.width)]
                for _ in range(self.height)]
