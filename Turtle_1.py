import turtle
col = ('orange','white','green')
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(25)
t.pensize(10)
for i in range(150):
    t.color(col[i%3])
    t.forward(i*1.5)
    t.left(59)
    t.width(3)
    
screen.exitonclick()
