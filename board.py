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
        self.recs = self.blank_field(0)

        for x, y in self.allpos():
            self.cells[y][x] = randrange(2)
            self.recs[y][x] = \
                Rectangle(
                    Point(x * self.cell_size, y * self.cell_size),
                    Point((x + 1) * self.cell_size, (y + 1) * self.cell_size))
            self.recs[y][x].setFill('black')

    def draw(self):
        """
        Draw entire board
        """
        for x, y in self.allpos():
            rec = self.recs[y][x]
            if self.cells[y][x]:
                rec.draw(self.window)
            else:
                rec.undraw()

    def allpos(self):
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)

    def blank_field(self, default_value):
        return [[default_value for _ in range(self.width)]
                for _ in range(self.height)]
