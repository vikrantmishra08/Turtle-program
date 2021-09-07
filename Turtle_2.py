import turtle
colr = ('white','magenta','green','blue','yellow','red')
wn = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
wn.speed(20)
for i in range(100):
    wn.color(colr[i%6])
    wn.forward(i*1.5)
    wn.right(60)
    wn.width(5)

screen.exitonclick()