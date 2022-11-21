from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.hideturtle()
        self.alterar_pontuacao()

    def alterar_pontuacao(self):
        self.write(f"Score: {self.points}", align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(x=0, y=125)
        self.write("GAME OVER", align='center', font=('Arial', 24, 'normal'))


    def aumentar_pontuacao(self):
        self.points += 1
        self.clear()
        self.alterar_pontuacao()

