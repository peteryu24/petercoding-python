import turtle

aaa = turtle.Turtle()
sc = turtle.Screen()
turtle.title('Drawing a Rectangle')

sc.setup(500,500, startx = 0, starty = 0)


aaa.penup()
aaa.goto(-100,100)
aaa.pendown()

aaa.goto(100,100)
aaa.goto(100,-100)
aaa.goto(-100,-100)
aaa.goto(-100,100)

turtle.done()
// draws a rectangle


import turtle
aaa = turtle.Turtle()
sc = turtle.Screen()
turtle.title('Click left mouse')
sc.setup(500,500, startx = 0, starty = 0)

aaa.speed(100)
def screenLeftClick(x, y) :    
    aaa.pendown()
    aaa.goto(x, y)  


turtle.onscreenclick(screenLeftClick, 1) #Event Function

turtle.done()
// draws wherever the mouse clicks

import turtle

aaa = turtle.Turtle()
sc = turtle.Screen()
turtle.title('Click left mouse')

sc.setup(500,500, startx = 0, starty = 0)

aaa.speed(100)
def screenLeftClick(x, y) :    
    aaa.pendown()
    aaa.goto(x, y)
    aaa.penup()

def screenRightClick(x, y):
    aaa.clear() #erase everything
    
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3) #register right click

turtle.done()
// same as previous code except when you click right, it erases everything


