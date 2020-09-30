import turtle
paper = turtle.Screen()
paper.bgcolor("green")

leonardo=turtle.Pen ()
leonardo.shape("turtle")
leonardo.color("blue")
leonardo.stamp()

move = 30
for i in range(12):
    leonardo.penup()
    leonardo.forward (50)
    leonardo.pendown()
    leonardo.forward(25)
    leonardo.penup()
    leonardo.forward(15)
    leonardo.stamp()
    leonardo.home()
    leonardo.right(move)
    move=move+30

paper.mainloop()