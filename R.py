import turtle
t=turtle.Turtle()

def drawn():
    t.penup()
    t.goto(-30,50) #centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("red")
    t.right(90)
    t.forward(150)
    t.goto(-30,50)
    t.right(-90)
    t.circle(-40,180,10)
    t.penup()
    t.left(135)
    t.pendown()
    t.forward(80)