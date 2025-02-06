from turtle import *
import pandas as pd

states_from_brazil = pd.read_csv('estados_brasil.csv')  # Upload the csv file

class State(Turtle):
    def __init__(self, state):
        super().__init__()
        self.name_state = state
        self.penup()
        self.hideturtle()
        self.goto(self.pos_state())
        self.write(arg=state, align='center', font=('serif', 10, 'bold'))

    def pos_state(self):
        """Get the x and y coordinates of the state in the csv file"""

        # Stores only the line that has the state answered by the user
        line_of_state = states_from_brazil[states_from_brazil['states'] == self.name_state]

        # Get the coordinates
        x_cor = line_of_state['x'].values[0]
        y_cor = line_of_state['y'].values[0]
        new_pos = (x_cor, y_cor)

        return new_pos

    @staticmethod
    def check_state(user_answer):
        """Checks if the user's response is in the list"""
        if user_answer in states_from_brazil['states'].to_list():
            return True
        return False