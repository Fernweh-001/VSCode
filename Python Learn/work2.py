
def Draw_square():
#用Turtle绘制正方形
    import turtle as t
    t.setup(800,600)
    t.penup()
    t.pensize(25)
    t.pencolor("black")
    t.goto(-200,-200)
    t.pendown()
    t.goto(-200,200)
    t.goto(200,200)
    t.goto(200,-200)
    t.goto(-200,-200)
    t.done()

def Draw_hexagon():
#用Turtle库绘制一个六边形
    import turtle as t
    t.setup(650,350,300,300)
    t.fd(60)
    for i in range(5):
        t.left(60)
        t.fd(60)
    t.done()

def Draw_amphiform():
    #绘制一个叠边形
    import turtle as t
    t.setup(700,600)
    t.pensize(20)
    t.pencolor("pink")
    t.fd(180)
    for i in range(8):
        t.left(80)
        t.fd(180)
    t.done()

def Draw_wind_mill():
#绘制一个风轮
    import turtle as t
    t.setup(600,400)
    t.pensize(30)
    t.pencolor("pink")
    t.left(45)
    t.fd(150)
    t.left(90)
    t.circle(150,45)
    t.left(90)
    t.fd(300)
    t.right(90)
    t.circle(-150,45)
    t.right(90)
    t.fd(150)
    t.left(90)
    t.fd(150)
    t.left(90)
    t.circle(150,45)
    t.left(90)
    t.fd(300)
    t.right(90)
    t.circle(-150,45)
    t.right(90)
    t.fd(150)

if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Draw square")
        print("2. Draw hexagon")
        print("3. Draw amphiform")
        print("4. Draw wind mill")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            Draw_square()
        elif choice == '2':
            Draw_hexagon()
        elif choice == '3':
            Draw_amphiform()
        elif choice == '4':
            Draw_wind_mill()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")