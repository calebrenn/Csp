# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
spot =trtl.Turtle()
spot.hideturtle()
size = 4
fill_color = "green"
shape = "turtle"
score = 0
font_setup = ("arial", 30, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
spot = trtl.Turtle(shape=shape)
spot.turtlesize(size)
spot.fillcolor(fill_color)
spot.penup()
spot.speed(0)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-20, 150)
score_writer.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()

#-----game functions--------
def spot_clicked(x,y):
    change_score()
    global score
    score += 1
    change_position()
    print("Turtle Clicked")
    print(spot.xcor(),spot.ycor())

def change_position():
    new_x = rand.randint(-225, 225)
    new_y = rand.randint(-170, 160)
    spot.goto(new_x, new_y)

def change_score():
    score_writer.clear()
    global score
    score += 1
    score_writer.pendown()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
#-----events----------------
change_position()
spot.onclick(spot_clicked)

wn = trtl.Screen()

wn.setup(width=500, height=400)

wn.cv._rootwindow.resizable(False, False)

wn.ontimer(countdown, counter_interval) 

wn.mainloop()