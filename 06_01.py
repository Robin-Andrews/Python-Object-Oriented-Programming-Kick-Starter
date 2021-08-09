import turtle


class ToggleTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color1 = "red"
        self.color2 = "blue"
        self.fillcolor(self.color1)
        self.onclick(self.toggle_color)

    def toggle_color(self, x, y):
        if self.fillcolor() == self.color1:
            self.fillcolor(self.color2)
        else:
            self.fillcolor(self.color1)


tt = ToggleTurtle()

turtle.done()
