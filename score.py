from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.hideturtle()
        self.alterar_pontuacao()

    def alterar_pontuacao(self):
        self.clear()
        self.write(f"Score: {self.points}, High Score: {self.highscore}", align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.points > self.highscore:
            self.highscore = self.points
        self.points = 0
        self.alterar_pontuacao()


    def aumentar_pontuacao(self):
        self.points += 1
        self.alterar_pontuacao()

