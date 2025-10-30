# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
trtl.addshape("star", ((8, -12), (0, 13), (-8, -12), (12, 4), (-12, 4)))
trtl.addshape("six", ((4, 12), (-8, 12), (-8, -8), (4, -8), (4, -8), (4, 4), (-4, 4), (-4, 8), (4, 8), (4, 12)))

#-----game configuration----
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
max_chars = 8
player_name = trtl.textinput("Name", "Enter your name, with max chars " + str(max_chars) + ":")
player_name = player_name[:max_chars]

while "," in  player_name or len(player_name)== 0 :
   player_name = trtl.textinput("Name", "please enter name properly, no commas and actually write your name")

#print(leader_names_list)
#print(leader_scores_list)
spot =trtl.Turtle()
spot.hideturtle()
size = 4
fill_color = "green"
shape = "turtle"
score = 0
font_setup = ("arial", 30, "normal")

timer = 20
counter_interval = 1000   #1000 represents 1 second
timer_up = False

sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
colors = ["red", "blue", "green", "pink", "purple", "yellow", "orange", "black", "gold", "grey", "chocolate", "thistle"]
shapes = ["turtle", "square", "triangle", "star", "circle", "arrow", "six"]
#-----initialize turtle-----
spot = trtl.Turtle(shape=shape)
spot.turtlesize(size)
spot.fillcolor(fill_color)
spot.penup()
spot.speed(0)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-20, 300)
score_writer.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()

#-----game functions--------
def spot_clicked(x,y):
    change_score()
    sizeshapeandcolorchange()
    global score
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
  counter.goto(100, 300)
  if timer <= 0:
    spot.hideturtle()
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    spot.penup()
    spot.color("black")
    manage_leaderboard()
    
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    spot.penup()
    counter.color("black")



def sizeshapeandcolorchange():
   spot.shapesize(rand.choice(sizes))
   spot.color(rand.choice(colors))
   spot.shape(rand.choice(shapes))



# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

#-----events----------------
change_position()
spot.onclick(spot_clicked)

wn = trtl.Screen()

wn.setup(width=1000, height=800)

wn.cv._rootwindow.resizable(False, False)

wn.ontimer(countdown, counter_interval) 

wn.mainloop()