# Import turtle package
import turtle
from playsound import playsound

# Creating a turtle object(pen)

wn = turtle.Screen()
pen = turtle.Turtle()
wn.title("meow")
wn.bgcolor("black")
wn.setup(width=800, height=500)
pen.speed(0)
pen.color("white")


# Defining a method to draw curve
def curve():
	for i in range(200):

		# Defining step by step curve motion
		pen.right(1)
		pen.forward(1)

# Defining method to draw a full heart


def heart():
# Set the fill color to red
	pen.fillcolor('red')

	#Start filling the color
	pen.begin_fill()

	# Draw the left line
	pen.left(140)
	pen.forward(113)

	# Draw the left curve
	curve()
	pen.left(120)

	# Draw the right curve
	curve()

	# Draw the right line
	pen.forward(112)

	# Ending the filling of the color
	pen.end_fill()

# Defining method to write text


def txt():

	# Move turtle to air
	pen.up()

	# Move turtle to a given position
	pen.setpos(-68, 95)

	# Move the turtle to the ground
	pen.down()

	# Set the text color to white
	pen.color('white')

	# Write the specified text in
	# specified font style and size
	pen.speed(300)
	pen.write("I Love you shotu", font=("Verdana", 12, "bold"))
	playsound("C:\\Users\\libia\\Downloads\\Barney - I Love You (SONG with LYRICS).mp3")
	turtle.exitonclick()


# Draw a heart
heart()

# Write text
txt()

# To hide turtle
#pen.ht()
