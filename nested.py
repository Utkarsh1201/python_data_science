from turtle import *
speed('fastest')
pencolor('pink')
fillcolor('yellow')
pensize(5)
side = 8
for i in range(side):
    fd(100)
    begin_fill()
    for i in range(side):
        fd(25)
        for i in range(side):
            bk(25)
            rt(360/side)
            dot(20)
    rt(360/side)
end_fill()
lt(360/side)


hideturtle()
mainloop()