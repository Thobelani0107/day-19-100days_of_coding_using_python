from turtle import  Turtle, Screen

MAG=Turtle()
screen=Screen()

def Move_Forward():
    MAG.forward(10)

def move_backward():
    MAG.backward(10)

def counter_clockwise():
    MAG.right(30)

def clockwise():
    MAG.left(30)
def clear_drawing():
    MAG.clear()

screen.listen()
screen.onkey(key="w",fun=Move_Forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear_drawing)


screen.exitonclick()