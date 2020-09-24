import turtle

paper = turtle.Screen()
paper.bgcolor("black")

leonardo = turtle.Turtle()
leonardo.color("gold")

leonardo.left(40)
leonardo.forward(80)
leonardo.left(40)
leonardo.forward(80)
leonardo.left(40)
leonardo.forward(80)
leonardo.left(40)
leonardo.forward(80)
leonardo.left(40)
leonardo.forward(80)
leonardo.left(40)
leonardo.forward(80)
leonardo.left(40)
leonardo.forward(80)
leonardo.left(40)
leonardo.forward(80)
leonardo.left(40)
leonardo.forward(80)
leonardo.penup()
leonardo.left(90)
leonardo.forward(30)
leonardo.left(90)
leonardo.forward(10)
leonardo.pendown()
for element in (0, 1, 2, 3, 4, 5, 6, 7, 8):
    leonardo.forward(60)
    leonardo.right(40)
    print(element)

paper.exitonclick()

paper.mainloop()







