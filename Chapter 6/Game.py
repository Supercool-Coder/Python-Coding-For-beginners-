from graphics import *

def main():
    win = GraphWin()
    a = point(25, 25)
    b = point(100, 175)
    c = point(100, 100)

    rect = Rectangle(a ,b)
    Circ= Circle(c, 50)

    rect = setFill("red")
    circ.setFill("blue")
    rect.setOutline("green")
    circ.setOutline("yellow")
    rect.setwidth(5)
    circ.setwidth(10)

    rect.draw(win)
    circ.draw(win)

    raw_input("Press <Enter> to quit")
    win.close()

main()