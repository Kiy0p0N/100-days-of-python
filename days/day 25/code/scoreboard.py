from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.correct_answer = 0
        self.list_states = []
        self.hideturtle()
        self.penup()
        self.color('white')

    def state_in_list(self, state):
        """Checks if the user has already responded to this state"""
        if state not in self.list_states:
            self.list_states.append(state)
            self.correct_answer += 1

    def victory(self):
        """Checks if the user got all the states right"""
        if self.correct_answer == 27:
            self.write(arg="Congratulations! You won!", align='center', font=('serif', 15, 'bold'))
            return True
        return False