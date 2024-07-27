#七段数码管倒计时
import turtle,time
def drawGap():
    turtle.penup()
    turtle.fd(5)

def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(0)

def drawDate(date):
    turtle.pencolor('red')
    for i in reversed(range(date+1)):
        turtle.clear()
        turtle.pendown()
        drawDigit(i)
        turtle.goto(0,0)
        turtle.penup()
        time.sleep(1)

def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    
    turtle.pensize(5)
    drawDate(5)
    turtle.hideturtle()
    turtle.done()
    
main()

