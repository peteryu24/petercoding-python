import turtle

aaa = turtle.Turtle()
sc = turtle.Screen()
turtle.title('click on mouse')
aaa.shape('circle')

sc.setup(500,500, startx = 0, starty = 0)

aaa.speed(100)
aaa.pensize(3)
def screenLeftClick(x, y) :    
    aaa.pendown()
    aaa.goto(x, y)

def screenRightClick(x, y):
    aaa.clear() 
    
def dragging(x,y):
    print(x,y)
    aaa.pendown()
    aaa.goto(x,y)
    
    
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3)
aaa.ondrag(dragging)

turtle.done()
