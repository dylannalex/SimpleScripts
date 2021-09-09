import turtle

BLUE = (5, 10, 36)
YELLOW = (255, 224, 82)

turtle.Screen().colormode(255)
turtle.Screen().bgcolor()


def tree(pen, levels, size, angle) -> None:
    if levels == 0:
        return

    pen.forward(size)
    pen.right(angle)
    tree(pen, levels - 1, size * 0.8, angle)

    pen.left(angle * 2)
    tree(pen, levels - 1, size * 0.8, angle)

    pen.right(angle)
    pen.backward(size)


def setup(pen):
    pen.up()
    pen.goto(0, -100)
    pen.down()
    pen.left(90)


def main():
    pen = turtle.Turtle()
    pen.speed("fastest")
    pen.color()
    pen.width(2)
    levels = 8
    size = 76
    angle = 35
    setup(pen)
    tree(pen, levels, size, angle)
    pen.hideturtle()
    turtle.Screen().exitonclick()


if __name__ == "__main__":
    main()
