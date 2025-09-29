import turtle as trtl
tree = trtl.Turtle()
tree.speed(0)

#configure the trunk of the tree
tree.pensize(3)
tree.pencolor("brown")

# build the trunk of the tree
tree.penup()
tree.goto(60, -380)
tree.pendown()
tree.fillcolor("brown")
tree.begin_fill()
tree.left(90)
tree.forward(380)
tree.left(90)
tree.forward(120)
tree.left(90)
tree.forward(380)
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












wn = trtl.Screen()
wn.mainloop()