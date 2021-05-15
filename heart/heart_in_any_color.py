import turtle as t

t.pensize(2)
clr=input("Which colour of heart do you want?\n 1. Red\n 2. Green\n 3. Purple\n 4. Yellow\n 5. Blue\n 6. Orange\nTYPE THE COLOUR NAME:  ")

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.fillcolor(clr)
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()
t.ht()
t.done()
