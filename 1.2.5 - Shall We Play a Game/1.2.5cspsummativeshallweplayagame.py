# Imports and lists
import turtle as trtl
import random as rand
import leaderboard as lb
wn = trtl.Screen()

# Start screen with a button to press to start the game

# Ask for name and put it in the leaderboard.txt file

# Create the turtles for each of the different object, aliens and ship

# Add the code for the player to be able to move the ship around the screen

# Add a score counter that detects when you have dodged the projectile

# Add the code that makes it so that if you get hit by a projectile you lose

# Add a game over screen that asks if you'd like to play again while showing you the leaderboard


#-----events----------------
wn.setup(width=500, height=1000)
wn.cv._rootwindow.resizable(False, False)
wn.listen()
trtl.mainloop()