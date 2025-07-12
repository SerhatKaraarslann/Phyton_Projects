import turtle 

turtle.speed(0)
turtle.bgcolor("black")
turtle.pencolor("orange")

def square(x,y):
    for j in range(4):
        turtle.forward(x)
        turtle.right(y)

for i in range(36):
    square(100,90)
    turtle.right(10)
    turtle.circle(10)
    turtle.right(10)
    turtle.hideturtle()
turtle.done()   