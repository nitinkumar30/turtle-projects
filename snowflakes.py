# import Turtle
import turtle
from random import randint

p = turtle.Turtle()
p.shape("turtle")
# speed of turtle
p.speed(1500)
p.pensize(4)
scr = turtle.Screen()
# setting the background color & title
scr.bgcolor("SkyBlue1")
scr.title("Merry Christmas")


# function for setting the color a and y coordinates and size of snowflake
def snowflake(color, x, y, size):
    p.penup()
    p.goto(x, y)
    p.pendown()

    p.color(color)
    p.left(90)

    # Set the for loop for create the snowflake branches
    for i in range(0, branches):
        # creates the shape of the snowflake
        p.forward(100 * size / 100)
        p.backward(40 * size / 100)
        p.left(40)
        p.forward(30 * size / 100)
        p.backward(30 * size / 100)
        p.right(80)
        p.forward(30 * size / 100)
        p.backward(30 * size / 100)
        p.left(40)
        p.backward(40 * size / 100)
        p.left(40)
        p.forward(30 * size / 100)
        p.backward(30 * size / 100)
        p.right(80)
        p.forward(30 * size / 100)
        p.backward(30 * size / 100)
        p.left(40)
        p.backward(20 * size / 100)
        p.right(360 / branches)


# writing the text and providing the color
p.color("green")
style = ('Courier', 20, 'italic')
p.write('Beautiful Snow', font=style, align='center')

# for loop for to develop 20 snowflakes
for i in range(0, 20):
    randomX = randint(-200, 200)
    randomY = randint(-200, 200)
    randomSize = randint(5, 40)
    branches = randint(5, 10)
    snowflake("white", randomX, randomY, randomSize)
turtle.done()
