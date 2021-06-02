#Importing the turtle and shapes.
import turtle


#Setting modifications for the turtle.
jpat = turtle.Turtle()
jpat.color("red")
jpat.pensize(8)
jpat.speed(2)

jpat.goto(10,10)
jpat.write("Hello, welcome to drawin with jpat!")
jpat.goto(10,5)

#When filled
jpat.fillcolor("green")
jpat.begin_fill()
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
jpat.end_fill()


#When not filled
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
jpat.forward(200)
jpat.left(80)
