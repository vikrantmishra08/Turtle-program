import turtle

colr = ('red', 'green', 'yellow')

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')

t.speed(25)
t.pensize(8)

for i in range(200):
    t.color(colr[i%3])
    t.forward(i*0.2)
    t.right(45)
    t.width(5)
    t.forward(25)
    t.left(60)
    t.forward(i*0.3)
    
screen.exitonclick()