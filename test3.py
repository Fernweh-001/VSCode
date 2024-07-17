
def Test_one():
#TempConvert.py
    TempStr = input("请输入:")
    if TempStr[-1] in ('f','F'):
        C = (eval(TempStr[0:-1])-32)/1.8
        print("{:.2f}C".format(C))
    elif TempStr[-1] in ('C','c'):
        F = 1.8*eval(TempStr[0:-1])+32
        print("{:.2f}F".format(F))
    else:
        print("输入格式错误")


def Test_two():
    import turtle as t
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(45)
    t.fd(140)


def Test_three():
#DayDayUpQ1
    dayfactor = 0.005
    dayup = pow(1+dayfactor,365)
    daydown = pow(1-dayfactor,365)
    print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))

def Test_four():
#DayDayUpQ2
    dayup = 1
    dayfactor = 0.01
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1-dayfactor)
            print("{:>2f}".format(dayup))
        else:
            dayup = dayup*(1+dayfactor)
            print("{:2f}".format(dayup))

def Test_five():
#DayDayUpQ3
    def dayUP(df):
        dayup = 1
        for i in range(365):
            if i % 7 in [6,0]:
                dayup = dayup*(1 - 0.01)
            else:
                dayup = dayup*(1+df)
        return dayup
    dayfactor = 0.01
    while dayUP(dayfactor) < 37.78:
        dayfactor += 0.001
    print("工作日的努力参数是:{:.3f}".format(dayfactor))

if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Test one")
        print("2. Test two")
        print("3. Test three")
        print("4. Test four")
        print("5. Test five")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            Test_one()
        elif choice == '2':
            Test_two()
        elif choice == '3':
            Test_three()
        elif choice == '4':
            Test_four()
        elif choice == '5':
            Test_five()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")