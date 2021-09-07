import turtle
a = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('cyan')
a.pensize(10)
a.speed(10)
for i in range(85):
    a.forward(5+i)
    a.right(15)

turtle.done()

