import turtle as trtl
tree = trtl.Turtle()
import random
tree.color("green")


for leaf in range(30):
    tree.penup()
    tree.goto(random.randint(-400, 400), random.randint(-400, 400))
    tree.stamp()
    tree.pendown()




wn = trtl.Screen()
wn.mainloop()