import turtle


class ToggleTurtle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x, y)
        self.color1 = "red"
        self.color2 = "blue"
        self.fillcolor(self.color1)
        self.onclick(self.toggle_color)

    def toggle_color(self, x, y):
        if self.fillcolor() == self.color1:
            self.fillcolor(self.color2)
        else:
            self.fillcolor(self.color1)


tt = ToggleTurtle(200, -200)

turtle.done()
