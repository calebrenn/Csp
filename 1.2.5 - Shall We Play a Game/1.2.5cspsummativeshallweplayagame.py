# Imports and lists
import turtle as trtl
import random as rand
import leaderboard as lb
import time as t
wn = trtl.Turtle()
wn.hideturtle()
ship = trtl.Turtle()
wn = trtl.Screen()
wn.setup(width=1000, height=1000)

leaderboard_file_name = "125_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
max_chars = 8
score = 0
player_name = trtl.textinput("Name", "Enter your name, with max chars " + str(max_chars) + ":")
player_name = player_name[:max_chars]

COLLISION_THRESHOLD = 50

timer = 60
counter_interval = 1000   #1000 represents 1 second
timer_up = False
# Ask for name and put it in the leaderboard.txt file
while "," in  player_name or len(player_name)== 0 :
   player_name = trtl.textinput("Name", "please enter name properly, no commas and actually write your name")
font_setup = ("arial", 30, "normal")

# add a timer
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()

def countdown():
  global timer, timer_up
  counter.clear()
  counter.goto(-50, 175)
  if timer <= 0:
    ship.hideturtle()
    alienship.hideturtle()
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    ship.penup()
    alienship.penup()
    ship.color("black")
    manage_leaderboard()
    
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    ship.penup()
    counter.color("black")

# code for the alien projectile
alienprojectileshape1 = "alienprojectile1.gif"
wn.addshape(alienprojectileshape1)
alienprojectile = trtl.Turtle()
alienprojectile.shape(alienprojectileshape1)

def drop_projectile(): 
  alienprojectile.speed(4)
  alienprojectile.penup()
  alienprojectile.goto(alienship.xcor(), -300)
  alienprojectile.clear()
  resetprojectile()

# Add a score counter that detects when you have dodged the projectile
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 200)
score_writer.write(score, font=font_setup)

def change_score():
    score_writer.clear()
    global score
    score += 1
    score_writer.pendown()
    score_writer.write(score, font=font_setup)

# Start screen with a button to press to start the game like enter
wn.bgpic("start.gif")
def startscreen(letter):
  if letter == "space":
    print(letter)
    wn.bgpic("gamebackground.gif")
    wn.setup(width=400, height=500)
    movethealienships()

for letter in {"space"}: 
  wn.onkeypress(lambda l=letter: startscreen(l), letter)
  print(letter) 

# Create the turtles for each of the different object, aliens and ship
# ship turtle
shipshape = "ship.gif"
wn.addshape(shipshape)
ship.shape(shipshape)
ship.penup()
ship.goto(0, -150)
ship.setheading(90)
ship.shape(shipshape)

# alien ship turtle
alienshipshape1 = "alienship1.gif"
wn.addshape(alienshipshape1)
alienship = trtl.Turtle()
alienship.shape(alienshipshape1)
alienship.penup()
alienship.goto(0, 150)

# Add the code for the player to be able to move the ship around the screen
def draw_ship(movingship, letter):
  if letter == "Up":
    movingship.goto(ship.xcor(), ship.ycor()+25)
  if letter == "Down":
    movingship.goto(ship.xcor(), ship.ycor()-25)
  if letter == "Left":
    movingship.goto(ship.xcor()-25, ship.ycor())
  if letter == "Right":
    movingship.goto(ship.xcor()+25, ship.ycor())


def check_key(key):
  wn.tracer(True)
  print("you pressed " +key)
  if key == "Up":
    ship.goto(ship.xcor(), ship.ycor()+25)
  if key == "Down":
    ship.goto(ship.xcor(), ship.ycor()-25)
  if key == "Left":
    ship.goto(ship.xcor()-25, ship.ycor())
  if key == "Right":
    ship.goto(ship.xcor()+25, ship.ycor())

for letter in {"Escape","Up","Down","Left","Right"}: 
  wn.onkeypress(lambda l=letter: check_key(l), letter)
  print(letter)

wn.onkeypress(quit, "Escape")

# reset the projectile
def resetprojectile():
  alienprojectile.penup()
  alienprojectile.goto(alienship.xcor(), alienship.ycor())
  change_score() 

# Add the code that makes it so that if you get hit by a projectile you lose or if the time runs out you win
resetprojectile()
startscreen(letter)
def movethealienships():
  while timer >= 0:
      alienship.speed(0)
      new_y = rand.randint(-120, 120)
      alienship.goto(new_y, 150)
      drop_projectile()
      
      if abs(alienprojectile.xcor() - ship.xcor())<= COLLISION_THRESHOLD: #check x coordinates
          alienprojectile.hideturtle()
          alienship.hideturtle()
          ship.hideturtle()
          wn.bgpic("blank.gif")
          manage_leaderboard()
          break
      if abs(alienprojectile.ycor() - ship.ycor())<= COLLISION_THRESHOLD: #check y coordinates)
          alienprojectile.hideturtle()
          alienship.hideturtle()
          ship.hideturtle()
          manage_leaderboard()
          break
# Add a game over screen that asks if you'd like to play again while showing you the leaderboard
# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global ship

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, ship, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, ship, score)

def change_score():
    score_writer.clear()
    global score
    score += 1
    score_writer.pendown()
    score_writer.write(score, font=font_setup)



#-----events---------------
wn.ontimer(countdown, counter_interval) 
wn.cv._rootwindow.resizable(False, False)
wn.listen()
trtl.mainloop()