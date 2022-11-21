from turtle import Turtle,Screen


class Snake:
    def __init__(self):
        self.turtles = []
        count = 0
        for i in range(3):
            new = Turtle()
            new.color("white")
            new.shape("square")
            new.penup()
            new.goto(x=0 - count, y=0)
            count += 20
            self.turtles.append(new)
        self.head = self.turtles[0]

    def ampliar_cobra(self):
        new = Turtle()
        new.goto(self.turtles[-1].pos())
        new.penup()
        new.color("white")
        new.shape("square")
        self.turtles.append(new)

    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            new_xpos = self.turtles[turtle - 1].xcor()
            new_ypos = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(x=new_xpos, y=new_ypos)
        self.turtles[0].forward(20)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
