#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create custom turtle shape
trtl.addshape("star", ((8, -12), (0, 13), (-8, -12), (12, 4), (-12, 4)))
trtl.addshape("six", ((4, 12), (-8, 12), (-8, -8), (4, -8), (4, -8), (4, 4), (-4, 4), (-4, 8), (4, 8), (4, 12)))
trtl.addshape("star2", ((8, -12), (0, 13), (-8, -12), (12, 4), (-12, 4)))
trtl.addshape("star3", ((8, -12), (0, 13), (-8, -12), (12, 4), (-12, 4)))
# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "star", "six", "star2", "star3"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "teal", "yellow", "silver", "blue"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  c= turtle_colors.pop()
  t.color(c)
  t.penup()
  my_turtles.append(t)

#  
startx = 0
starty = 0
h = 0

#
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(h)
  t.pendown()
  t.right(36)     
  t.forward(60)

#	
  startx = t.xcor()
  starty = t.ycor()
  h = t.heading()
wn = trtl.Screen()
wn.mainloop()