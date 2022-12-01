import turtle
import time

def drawnK():
    t=turtle.Turtle()
    t.penup()
    t.goto(-30,50)
    t.pendown()
    t.pensize(10)
    t.pencolor("black")
    
    t.right(90)
    t.forward(150)
    
    t.goto(-30,-20)
    t.left(45)
    t.forward(100)
    
    t.goto(-30,-20)
    t.left(90)
    t.forward(100)

    time.sleep(3)
drawnK()