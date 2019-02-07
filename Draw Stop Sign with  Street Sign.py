# Program: Draw Stop Sign w/ Street Sign 
# Author: Charlie Emmett

# import modules

import turtle as t

# declare constants

turtle_speed = 0
post_initial_x = 0
post_initial_y = -400
post_thickness = 14
post_length = 550
oct_initial_x = -50 
oct_initial_y = 120
side_length =  100
turn_angle = 45
side_count = 8
border_line_weight = 8
border_side_length = 92
word_initial_x = 0
word_initial_y = -45
stop_font_size = 56
st_sign_initial_x =-150
st_sign_initial_y = 145
st_sign_length = 300
st_sign_height = 80
st_sign_word_x = 0
st_sign_word_y = 165
st_sign_font_size = 30

# set turtle speed

t.speed(turtle_speed)

# draw sign post

t.penup()
t.setx(post_initial_x)
t.sety(post_initial_y)
t.left(90)
t.pensize(post_thickness)
t.color('grey','grey')
t.pendown()
t.forward(post_length)
t.right(90)
t.penup()

# position turtle for octagon

t.setx(oct_initial_x)
t.sety(oct_initial_y)
t.pendown()

# set octagon color

t.color('red', 'red')

# draw octagon

t.begin_fill()

for x in range(side_count):
    t.forward(side_length)
    t.right(turn_angle)

t.end_fill()

# position turtle to draw border

t.forward(6)
t.right(90)
t.forward(10)
t.left(90)

# set border line weight

t.pensize(border_line_weight)

# set border color

t.color("white",'white')

# draw border

for x in range(side_count):
    t.forward(border_side_length)
    t.right(turn_angle)

t.penup()

# positon turtle to write stop

t.setx(word_initial_x)
t.sety(word_initial_y)

# write stop

t.write('STOP',align='center', font=("Highway Gothic",stop_font_size,"bold"))

# position turtle to draw street sign

t.setx(st_sign_initial_x)
t.sety(st_sign_initial_y)
t.seth(0)

# set street sign color

t.color('green','green')

# draw street sign

t.begin_fill()
t.pendown()
t.forward(st_sign_length)
t.left(90)
t.forward(st_sign_height)
t.left(90)
t.forward(st_sign_length)
t.left(90)
t.forward(st_sign_height)
t.end_fill()

# set color of street sign word

t.color("white","white")

# position turtle to write word on street sign

t.penup()
t.setx(st_sign_word_x)
t.sety(st_sign_word_y)

# write word on street sign

t.write("Spring Loop",align="center",font=("Highway Gothic",st_sign_font_size,"bold"))
t.hideturtle()


