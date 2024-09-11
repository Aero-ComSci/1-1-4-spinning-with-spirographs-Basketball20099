import turtle

t = turtle.Turtle()
turtle.bgcolor("lightgreen")

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

num_squares = 8
size_increment = 30


for i in range(num_squares):
    size = 50 + i * size_increment
    t.color(colors[i % len(colors)])
    t.penup()
    t.goto(-size / 2, -size / 2)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)


t.hideturtle()
turtle.done()
