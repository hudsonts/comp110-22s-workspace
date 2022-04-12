"""This program will draw a scene of turtles among other objects!"""

__author__ = "730509671"

from turtle import Turtle, colormode, done
wellbase: int = 300
wellheight: int = 80
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    sky(ertle, -750, 500)
    well(ertle, -150, -150)
    grass(ertle, -750, -200)
    flag(ertle, -500, -220)
    flag(ertle, 500, -220)
    done()


def well(old_well: Turtle, x: float, y: float) -> None:
    """Draw an image of the old well whose top left corner is located at x, y."""
    old_well.speed(50)
    old_well.penup()
    old_well.goto(x, y)
    old_well.pendown()
    old_well.speed(50)
    old_well.begin_fill()
    old_well.fillcolor(200, 200, 200)
    i: int = 0 
    h: int = 0
    z: int = 0
    while i < 2: 
        old_well.forward(wellbase)
        old_well.right(90)
        old_well.forward(wellheight)
        old_well.right(90)
        i = i + 1
    old_well.forward(40)
    old_well.left(90)
    old_well.forward(200)
    old_well.left(90)
    old_well.forward(40)
    old_well.right(90)
    while h < 7:
        old_well.forward(12)
        old_well.right(75)
        old_well. forward(13)
        old_well.left(75)
        h = h + 1
    old_well.right(90)
    old_well.forward(118)
    old_well.right(15)
    old_well.forward(12)
    old_well.right(75)
    while z < 6:
        old_well.forward(12)
        old_well.left(75)
        old_well.forward(13)
        old_well.right(75)
        z = z + 1
    old_well.forward(12)
    old_well.right(90)
    old_well.forward(40)
    old_well.left(90)
    old_well.forward(200)
    old_well.right(90)
    old_well.forward(125)
    old_well.right(90)
    old_well.forward(50)
    old_well.left(45)
    old_well.forward(15)
    old_well.right(135)
    old_well.forward(70)
    old_well.right(135)
    old_well.forward(15)
    old_well.left(45)
    old_well.forward(50)
    old_well.end_fill()


def sky(sky: Turtle, x: float, y: float) -> None:
    """This function draws the sky in the background of the image. I also attempted to leave a white space that will sit behind the well, that way the water fountain in the well can be a lighter shade than the well itself."""
    sky.speed(50)
    sky.penup()
    sky.goto(x, y)
    sky.pendown()
    sky.begin_fill()
    sky.fillcolor(209, 249, 255)
    sky.color(209, 249, 255)
    i: int = 0
    while i < 4:
        sky.forward(2000)
        sky.right(90)
        i = i + 1
    sky.end_fill()
    sky.penup()
    sky.goto(-50, -70)
    sky.pendown()
    sky.begin_fill()
    sky.fillcolor(250, 250, 250)
    h: int = 0
    while h < 4:
        sky.forward(100)
        sky.right(90)
        h = h + 1
    sky.end_fill()


def grass(grass: Turtle, x: float, y: float) -> None:
    """This function draws grass that the well sits upon."""
    grass.speed(50)
    grass.penup()
    grass.goto(x, y)
    grass.pendown()
    grass.begin_fill()
    grass.fillcolor(0, 163, 47)
    i: int = 0
    grass.left(67.5)
    while i < 60:
        grass.left(45)
        grass.forward(15)
        grass.right(45)
        grass.forward(15)
        i = i + 1
    grass.right(55)
    grass.forward(500)
    grass.right(90)
    grass.forward(2000)
    grass.end_fill()


def flagpole(flagpole: Turtle, x: float, y: float) -> None:
    """This function sets the point and draws the flagpole that will be used in the flag function to create a composite structure."""
    flagpole.speed(50)
    flagpole.penup()
    flagpole.goto(x, y)
    flagpole.pendown()
    flagpole.color("Black")
    flagpole.left(225)
    flagpole.forward(20)
    flagpole.left(35)
    flagpole.forward(450)


def flag(flag: Turtle, x: float, y: float) -> None:
    """This function draws trees that will be placed on either side of the old well."""
    flagpole(flag, x, y)
    i: int = 0
    flag.begin_fill()
    flag.fillcolor(118, 212, 244)
    flag.color(118, 212, 244)
    while i < 15:
        flag.right(80)
        flag.forward(60)
        flag.right(100)
        flag.forward(40)
        i = i + 1
    flag.end_fill()
    flag.right(79)
    flag.penup()


if __name__ == "__main__":
    main()