from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        with open("data.txt") as score_file:
            self.highest_score = int(score_file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", "w") as score_file:
                score_file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
