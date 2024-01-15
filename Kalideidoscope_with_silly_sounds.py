import random
import turtle
from playsound import playsound

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow","blue","green","orange","purple","white","gray"]


playsound('sound_sebi_time_to_start.mp3')


for n in range(50):
    playsound('sound_papa_r2d2.mp3')
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)