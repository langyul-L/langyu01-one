import turtle

def draw_triangle(x1,y1,x2,y2,x3,y3,t):
    #绘制一个三角形
    t.up()
    t.setpos(x1,y1)
    t.down()
    t.setpos(x2,y2)
    t.setpos(x3,y3)
    t.setpos(x1,y1)
    t.up()

def main():
    print("testing turtle graphics...")

    t = turtle.Turtle()
    t.hideturtle()
    draw_triangle(-100,0,0,-173.2,100,0,t)
    turtle.mainloop()

#调用main函数
if __name__ == '__main__':
    main() 