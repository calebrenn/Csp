#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def maze1_solution():
  for step in range(4):
    move()

  for step in range(3):
    turn_left()

  for step in range(4):
    move()

def maze2_solution():
  for step in range(3):
    turn_left()

  for step in range(3):
    move()

  for step in range(1):
    turn_left()

  for step in range(3):
    move()

  for step in range(1):
    turn_left()

  for step in range(1):
    move()

def maze3_solution():
    for each in range(2):
      move()
      for turn in range(3):
        turn_left()
      for step in range(2):
        move()
      turn_left()
      move()
      robot.pencolor("red")
    
#---- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample for loop
maze1_solution()

keep_going = trtl.textinput("Continue?" , "Do you want to continue?")
keep_going = keep_going.lower() # error handling

if keep_going == 'y':
  robot.clear()
  robot.goto(startx, starty)
  robot.setheading(90)
  wn.bgpic("maze2.png")
  maze2_solution()
else:
  wn.bye()

keep_going = trtl.textinput("Continue?" , "Do you want to continue?")
keep_going = keep_going.lower() # error handling

if keep_going == 'y':
  robot.clear()
  robot.goto(startx, starty)
  robot.setheading(90)
  wn.bgpic("maze3.png")
  maze3_solution
else:
  wn.bye()




#---- end robot movement 
wn.mainloop()
