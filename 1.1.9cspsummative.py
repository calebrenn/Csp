import turtle as trtl
tree = trtl.Turtle()
tree.speed(0)

#configure the trunk of the tree
tree.pensize(3)
tree.pencolor("brown")

# build the trunk of the tree
tree.penup()
tree.goto(60, -410)
tree.pendown()
tree.fillcolor("brown")
tree.begin_fill()
tree.left(90)
tree.forward(410)
tree.left(90)
tree.forward(120)
tree.left(90)
tree.forward(410)
tree.fillcolor("brown")
tree.end_fill()

# configure the color of the leaves
color = trtl.textinput("color", "What color do you want the leaves to be?")
tree.pencolor(color)

# build the leaves of the tree
tree.penup()
tree.fillcolor(color)
tree.begin_fill()
tree.goto(0, -70)
tree.left(90)
tree.pendown()
tree.circle(225, 360)
tree.end_fill()

# drawing the flowers
painter = trtl
startx = 300
painter.speed(0)

for flower in range (4):
    painter.color("green")
    painter.pensize(10)
    painter.penup()
    painter.goto(startx, -410)
    painter.pendown()
    painter.setheading(90)
    painter.forward(100)
    painter.penup()

    #  leaf
    painter.pendown()
    painter.setheading(270)
    painter.circle(20, 120, 20)
    painter.setheading(90)
    painter.penup()
    painter.goto(startx, -350)

    # rest of stem
    painter.pendown()
    painter.forward(60)
    painter.setheading(0)

    # change pen
    painter.penup()
    painter.shape("circle")
    painter.turtlesize(1)

    # draw flower
    painter.color("bisque")
    painter.goto(startx,-225)
    startx -= 200

    for petal in range(36):
        painter.right(10)
        painter.forward(5)
        painter.stamp()

# create leaves
trtl.addshape("leaf1", ((8, -12), (0, 13), (-8, -12), (12, 4), (-12, 4)))
trtl.addshape("leaf2", ((8, -12), (0, 13), (-8, -12), (12, 4), (-12, 4)))
trtl.addshape("leaf3", ((8, -12), (0, 13), (-8, -12), (12, 4), (-12, 4)))
trtl.addshape("leaf4", ((8, -12), (0, 13), (-8, -12), (12, 4), (-12, 4)))
trtl.addshape("leaf5", ((8, -12), (0, 13), (-8, -12), (12, 4), (-12, 4)))

# create an empty list
my_leaves = []

# use diff leaves and colors
leaf_shapes = ["leaf1","leaf2", "leaf3", "leaf4", "leaf5"]
leaf_colors = ["burlywood", "goldenrod", "lawngreen", "fuchsia", "forestgreen"]

# ask user how many leaves they want
leaf = int(trtl.textinput("leaves", "How many leaves do you want to have on the screen?"))

# leaves
leaves = trtl.Turtle()
import random
leaves.color = "leaf_color"
leaves.speed(0)

# put the leaves all over the screen
for l in range(leaf):
    for current_leaf in leaf_shapes and leaf_colors:
        leaves.penup()
        leaves.goto(random.randint(-400, 400), random.randint(-400, 0))
        leaves.stamp()
        leaves.pendown()


wn = trtl.Screen()
wn.mainloop()