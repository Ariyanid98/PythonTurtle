import turtle

t= turtle.Turtle()
t.screen.bgcolor("black")
t.pensize(3)
t.left(90)

t.backward(100)
t.speed(200)
t.shape("turtle")

def bunga (i):
    if i<10:
        return
    else:
        t.forward(i)
        t.color("white")
        t.circle(2)
        t.color("magenta")
        t.left(30)
        bunga(3*i/4)
        t.right(60)
        bunga(3*i/4)
        t.left(30)
        t.backward(i)
bunga(100)
turtle.done()
