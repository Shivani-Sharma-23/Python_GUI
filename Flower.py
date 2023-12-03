import turtle

def draw_petal(color):
    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.circle(100, 60)
    turtle.left(120)
    turtle.circle(100, 60)
    turtle.left(120)

    turtle.end_fill()

def draw_flower(n, petal_color, border_color, border_width):
    turtle.pensize(border_width)
    turtle.pencolor(border_color)
    
    for _ in range(n):
        draw_petal(petal_color)
        turtle.left(360/n)

turtle.speed(6)
turtle.bgcolor("black")

draw_flower(10,"pink", "purple", 7)

turtle.hideturtle()

turtle.mainloop()
