import turtle
sk = turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")
sk.pencolor('green')
a = 1
i = 0
e = 1
f = 1
sk.speed(15)
while True:
    while a <= 3:
        a = a+1
        if e == 1:
            sk.right(30)
            sk.right(30)
            sk.forward(100)
            sk.circle(10)
            e = 0
        else:
            sk.left(30)
            sk.forward(100)
            sk.circle(10)
            sk.backward(100)
            sk.right(30)
            sk.right(30)
            sk.forward(100)
            sk.circle(10)

    sk.penup()
    sk.setpos(0,0)
    sk.right(180)
    sk.pendown()
    if i == 0:
        a = 1


    while a <= 3:
        a = a+1
        if f == 1:
            sk.left(30)
            sk.left(30)
            sk.forward(100)
            sk.circle(10)
            f = 0
        else:
            sk.right(30)
            sk.forward(100)
            sk.circle(10)
            sk.backward(100)
            sk.left(30)
            sk.left(30)
            sk.forward(100)
            sk.circle(10)
        i = 1
    sk.penup()
    sk.setpos(0,-275)
    sk.pendown()

