import turtle
from turtle import *
from colorsys import *

def flower_pattern_1():
    """Orange square pattern flower"""
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.pencolor("orange")

    def square(x, y):
        for j in range(4):
            turtle.forward(x)
            turtle.right(y)

    for i in range(36):
        square(100, 90)
        turtle.right(10)
        turtle.circle(10)
        turtle.right(10)
    turtle.hideturtle()
    turtle.done()

def flower_pattern_2():
    """Colorful spiral flower"""
    bgcolor("black") 
    tracer(20)
    pensize(2)
    j = 0
    goto(-140, 170)

    for i in range(250):
        c = hsv_to_rgb(j, 1, 1)
        fillcolor(c)
        begin_fill()
        left(110)
        circle(25, 100)
        circle(-25, 100)
        circle(20)
        backward(350-i)
        j += 0.005
        end_fill()
    done()

# Choose which pattern to run:
# flower_pattern_1()  # Uncomment to run orange pattern
# flower_pattern_2()  # Uncomment to run colorful spiral pattern
