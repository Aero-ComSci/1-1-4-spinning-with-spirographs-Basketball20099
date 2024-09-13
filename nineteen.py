#   a114_nested_loops_4.py 
import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()


while (True):
    #Set condition for it to always run.
    x = -200
    y = 0
    move_x = 25  
    move_y = 25
    while (x < 200):

        while (y < 100):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = -25
        
        while (y > 0):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = 25

    #Go back to starting point and reset values.
    painter.penup()
    painter.goto(-200, 0)
    painter.pendown()
    x = -200
    y = 0
    move_x = 25  
    move_y = 25

    while (x < 200):
    
        while (y > -100):
            x = x + move_x
            y = y - move_y
            painter.goto(x,y)
        
        while (y < 0):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
    painter.penup()
    painter.goto(-200, 0)
    painter.pendown()

wn = trtl.Screen()
wn.mainloop()

