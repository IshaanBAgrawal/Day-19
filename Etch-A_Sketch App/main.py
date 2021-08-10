import turtle as t

tom = t.Turtle()
screen = t.Screen()


def move_fd():
    tom.fd(10)


def move_bk():
    tom.bk(10)


def move_counter():
    tom.left(10)


def move_clockwise():
    tom.right(10)


def clear_drawing():
    tom.reset()


def pen_up():
    tom.penup()


def pen_down():
    tom.pendown()


screen.listen()

screen.onkey(key="W", fun=move_fd)
screen.onkey(key="w", fun=move_fd)

screen.onkey(key="S", fun=move_bk)
screen.onkey(key="s", fun=move_bk)

screen.onkey(key="A", fun=move_counter)
screen.onkey(key="a", fun=move_counter)

screen.onkey(key="D", fun=move_clockwise)
screen.onkey(key="d", fun=move_clockwise)

screen.onkey(key="C", fun=clear_drawing)
screen.onkey(key="c", fun=clear_drawing)

screen.onkey(key="U", fun=pen_up)
screen.onkey(key="u", fun=pen_up)

screen.onkey(key="B", fun=pen_down)
screen.onkey(key="b", fun=pen_down)

screen.exitonclick()
