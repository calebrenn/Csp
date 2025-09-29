#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
num_spiderlegs = 6
leg_length = 100
leg_angle = 380 / num_spiderlegs
print('z=', leg_angle)
spider.pensize(5)
leg = 0
while (leg < num_spiderlegs):
  spider.goto(0,0)
  spider.setheading(leg_angle*leg)
  print('z=', leg_angle*leg)
  spider.forward(leg_length)
  leg = leg + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()