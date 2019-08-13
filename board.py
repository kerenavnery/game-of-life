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
        # There are 5 states:
        ## 1. Normal cell cycle - White
        ## 2. Senscence - Gray
        ## 3. Cell death - Black
        ## 4. cancer - Red
        self.cells[y][x] = newvalue
        if newvalue == "normal_cell_cycle":
            color = "white"
        elif newvalue == "senescence":
            color = "gray"
        elif newvalue == "cell_death":
            color = "black"
        elif newvalue == "cancer":
            color = "red"
        else:
            color = "green"

        self.recs[y][x].setFill(color)


    def get(self, x, y):
        return self.cells[y][x]

    def get_num_of_cells_in_state(self, state):
        num_in_state = 0
        for x, y in self.allpos():
            if state == self.get(x,y):
                num_in_state = num_in_state + 1
        return num_in_state


    def initiailze(self):
        for x, y in self.allpos():
            self.set(x, y, "normal_cell_cycle")

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
        # Run over all the cells in the board, and decide what is the next value for each cell
        for x, y in self.allpos():
            currval = self.get(x,y)

            if currval == "normal_cell_cycle":
                ## Chance to remain healthy
                if (randrange(1,1000) < 900):
                    newval = currval
                ## Chance to experiance stress damage
                else:
                    chance = randrange(1,1000)
                    if chance < 2:
                        newval = "cell_death"
                    elif chance < 902:
                        newval = "senescence"
                    else:
                        newval = "cancer"

            elif currval == "senescence":
                ## Chance to remain SnC
                if (randrange(1,1000) < 900):
                    newval = currval
                ## Chance to be removed by immune system
                else:
                    newval = "cell_death"
                
            elif currval == "cell_death":
                newval = currval #What is dead may never die
                
            elif currval == "cancer":
                ## Chance to remain cancer
                if (randrange(1,1000) < 970):
                    newval = currval
                ## Chance to be removed by immune system
                else:
                    newval = "cell_death"
                
            else:
                print("Error")
           # neisum = self.neighbour_sum(x, y)
            #newval = 0
            #if neisum == 2:
            #    newval = self.get(x, y)
            #elif neisum == 3:
            #    newval = 1
            newcells[y][x] = newval

        for x, y in self.allpos():
            self.set(x, y, newcells[y][x])

    def get_game_over(self):
        game_over = False
        total_cells_normal = self.get_num_of_cells_in_state("normal_cell_cycle")
        total_cells_snc = self.get_num_of_cells_in_state("senescence")
        total_cells_death = self.get_num_of_cells_in_state("cell_death")
        total_cells_cancer = self.get_num_of_cells_in_state("cancer")
        ## Normal and senescence cells are less than 0.3 of the cells
        if (float(total_cells_normal + total_cells_snc)/(self.width * self.height)) < 0.3: #Must be smaller than 1
            game_over = True
        return game_over


