import turtle

def draw_heart_shape(t, size, color):
    t.begin_fill()
    t.color(color)
    t.left(140)
    t.forward(size)
    t.circle(-size // 2, 200)
    t.left(120)
    t.circle(-size // 2, 200)
    t.forward(size)
    t.end_fill()
    t.setheading(0)

def display_message():
    turtle.penup()
    turtle.goto(0, -350)  # Position the message below the hearts
    turtle.color("white")
    turtle.write(
        "Happy Birthday, Babe!\nAll the best to you ❤️\nI just want to say I love you <33",
        align="center",
        font=("Arial", 18, "bold")
    )
    turtle.hideturtle()

def draw_heart():
    turtle.bgcolor("lightpink")
    turtle.speed(3)
    turtle.width(3)
    
    sizes = [250, 200, 150, 100, 50]
    colors = ['#E57582', '#E793A2', '#DCB783', '#E47381', '#E793A2']

    for size, color in zip(sizes, colors):
        turtle.penup()
        turtle.goto(0, -size // 2)
        turtle.pendown()
        draw_heart_shape(turtle, size, color)

    display_message()
    turtle.done()

draw_heart()
