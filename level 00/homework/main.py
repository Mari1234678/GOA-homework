from turtle import * 
width(7)
speed(0)

# cube filled in 
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)

penup()
goto(130 ,0)
pendown()

# first colourd door
color("#a15c86")
begin_fill()
left(180)
forward(130)
right(90)
forward(50)
right(90)
forward(130)
end_fill()
# first colourd window
penup()
goto(280, 150)
pendown()
color("#f08bdc")
begin_fill()
right(90)
forward(50)
right(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(20, 150)
pendown()
# second colourd window
begin_fill()
left (90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
penup()
goto(300, 300)
pendown()
# roof 
color("pink")
begin_fill()
right(135)
forward(200)
left(86)
forward(210)
end_fill()





exitonclick()