import turtle

wn =turtle.Screen()
t = turtle.Turtle()
t.color("red")
t.speed(20000)

for x in range(1000):
    if x % 10 == 0:
        t.color('green')
    else:
        t.color('red')
    if x % 5 == 0:
        t.color("blue")
    else:
        t.color('orange')   
    t.forward(x)
    t.left(91)