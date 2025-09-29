#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

#Ctreate a spider body
spider.pensize(40)
spider.circle(20)
#-----------------+

#Configure spider legs
num_spiderlegs = 8
leg_length = 100
leg_angle = 20
print('z=', leg_angle)
spider.pensize(10)
#-----------------+

#Draw spider legs
leg = 0
while (leg < num_spiderlegs):
  spider.goto(0,20)
  if leg<4:
    spider.pendown()
    spider.setheading(leg_angle*leg - 5)
    spider.circle(-100, 100)
    spider.penup()
  else:
    spider.pendown()
    spider.setheading(leg_angle*leg + 45)
    spider.circle(100, 100)
    spider.penup()
  print('z=', leg_angle*leg)
  spider.forward(leg_length)
  leg = leg + 1
spider.penup()
#-----------------+

#Draw spider head
spider.goto(-7.5,-40)
spider.pendown()
spider.pensize(25)
spider.circle(10)
spider.penup()
#-----------------+

#Configure spider eyes
spider.pencolor("purple")
spider.pensize(10)
#-----------------+

#Draw Spider Eyes
spider.goto(10,-40)
spider.pendown()
spider.circle(1)
spider.penup()
spider.goto(-10,-40)
spider.pendown()
spider.circle(1)
spider.penup()
#-----------------+

#Configure spider pupils
spider.pencolor("white")
spider.pensize(5)
#-----------------+

#Draw Spider pupils
spider.goto(10,-40)
spider.pendown()
spider.circle(1)
spider.penup()
spider.goto(-10,-40)
spider.pendown()
spider.circle(1)
#-----------------+

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()