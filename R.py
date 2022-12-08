import turtle
t=turtle.Turtle()

def draw():
    t.pensize(10)
    t.pencolor("red")
    t.forward(10)
    t.right(-90)
    t.forward(150)
    t.right(90)
    t.circle(-40,180,10)
    t.penup()
    t.left(130)
    t.pendown()
    t.forward(90)

draw()