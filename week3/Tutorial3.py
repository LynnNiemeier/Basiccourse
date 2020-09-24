import turtle
window = turtle.Screen()
window.bgcolor("red") # Set the window background color
window.title("Hello, Tess!") # Set the window title

tess = turtle.Turtle()
tess.color("purple") # Tell tess to change her color
tess.pensize(3) # Tell tess to set her pen width

tess.forward(50)
tess.left(180)

tess.forward(50)

window.mainloop()