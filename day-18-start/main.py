from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

#Make a square
timmy_the_turtle.fd(10)
timmy_the_turtle.penup()
timmy_the_turtle.fd(10)
timmy_the_turtle.pendown()
timmy_the_turtle.fd(100)
timmy_the_turtle.penup()
timmy_the_turtle.fd(10)
timmy_the_turtle.pendown()
timmy_the_turtle.fd(10)
timmy_the_turtle.penup()
timmy_the_turtle.fd(10)
timmy_the_turtle.pendown()



screen = Screen()
screen.exitonclick()

