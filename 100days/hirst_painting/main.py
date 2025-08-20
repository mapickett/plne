from color_palette import Palette
import turtle

if __name__ == '__main__':

    palette = Palette('image.jpg', 50)

    turtle.setup(width=420, height=420) 
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.screen.colormode(255)
    t.penup()
    for row in range(10):
        t.goto(-180,-180 + 40*row)
        for _ in range(10):
            c = palette.get_color()
            t.dot(20, c)
            t.forward(40)

    turtle.exitonclick()