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
            rec.setFill('white')
            rec.draw(self.window)
            self.recs[y][x] = rec

    def set(self, x, y, newvalue):
        self.cells[y][x] = newvalue

        color = "black" if newvalue else "white"
        self.recs[y][x].setFill(color)


    def get(self, x, y):
        return self.cells[y][x]

    def randomize(self):
        for x, y in self.allpos():
            self.set(x, y, randrange(2))

    def allpos(self):
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)

    def blank_field(self, default_value):
        return [[default_value for _ in range(self.width)]
                for _ in range(self.height)]

    def neighbours(self, x, y):
        for yi in range(y - 1, y + 2):
            for xi in range(x - 1, x + 2):
                if xi <= 0 or yi <= 0:
                    continue
                if xi >= self.width or yi >= self.height:
                    continue
                if xi == x and yi == y:
                    continue
                yield (xi, yi)

    def neighbour_sum(self, x, y):
        return sum(self.get(xi, yi) for xi, yi in self.neighbours(x, y))

    def live(self):
        newcells = self.blank_field(0)
        for x, y in self.allpos():
            neisum = self.neighbour_sum(x, y)
            newval = 0
            if neisum == 2:
                newval = self.get(x, y)
            elif neisum == 3:
                newval = 1
            newcells[y][x] = newval

        for x, y in self.allpos():
            self.set(x, y, newcells[y][x])
