import turtle               #1. import modules
import random

lengthPolygon = 75
startX = -100
startY = 20
raceOne = 100
raceTwo = 10

def returnTurtles(turtle1, turtle2):
	"""
	Returns turtles to respective starting positions
	args: 2 turtle objects
	return: none
	"""
	turtle1.goto(startX,startY)
	turtle2.goto(startX,-startY)
def raceTurtles(turtle1, turtle2, value):
	"""
	Brings turtles forward by a random interval determined by passed value
	args: 2 turtle objects, int
	return: none
	"""
	turtle1.forward(random.randrange(1,value+1)) 
	turtle2.forward(random.randrange(1,value+1))
def drawPolygon(turtle, length, sides):
	"""
	Uses a turtle object to draw an n-sided polygon with specified length
	args: turtle object, 2 ints
	return: string
	"""
	for i in range(sides):
		turtle.forward(length)
		turtle.left(360/sides)
	turtle.clear()
	return print("Polygon with " + str(sides) + " sides")
	
def main():
	#Part A
	window = turtle.Screen()       # 2.  Create a screen
	window.bgcolor('lightblue')

	michelangelo = turtle.Turtle()    # 3.  Create two turtles
	leonardo = turtle.Turtle()
	michelangelo.color('orange')
	leonardo.color('blue')
	michelangelo.shape('turtle')
	leonardo.shape('turtle')

	michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
	leonardo.up()
	returnTurtles(michelangelo, leonardo)

	## 5. your code goes here
	raceTurtles(michelangelo, leonardo, raceOne)
	returnTurtles(michelangelo, leonardo)

	for i in range(raceTwo):
		raceTurtles(michelangelo, leonardo, raceTwo)
	returnTurtles(michelangelo, leonardo)

	# Part B - complete part B here
	A = [3,4,6,9,12]
	michelangelo.down()
	for i in A:
		drawPolygon(michelangelo, lengthPolygon, i)
		
	window.exitonclick()
main()