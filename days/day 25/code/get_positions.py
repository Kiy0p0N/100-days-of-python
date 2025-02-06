import turtle
from turtle import Screen

screen = Screen()
screen.setup(width=800, height=800)
image = './image/mapa-brasil.gif'
screen.bgpic(image)

def get_pos(x, y):
    print(x, y)

turtle.onscreenclick(get_pos)


turtle.mainloop()
screen.exitonclick()