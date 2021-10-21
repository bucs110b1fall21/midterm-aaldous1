import turtle               #1. import modules
import random

lengthPolygon = 75
startX = -100
startY = 20
raceOne = 100
raceTwo = 10
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
	michelangelo.goto(startX,startY)
	leonardo.goto(startX,-startY)

	## 5. your code goes here
	michelangelo.forward(random.randrange(1,raceOne+1)) 
	leonardo.forward(random.randrange(1,raceOne+1))
	michelangelo.goto(startX,startY)
	leonardo.goto(startX,-startY)

	for i in range(raceTwo):
		michelangelo.forward(random.randrange(0,raceTwo+1))
		leonardo.forward(random.randrange(0,raceTwo+1))
	michelangelo.goto(startX,startY)
	leonardo.goto(startX,-startY)

	# Part B - complete part B here
	A = [3,4,6,9,12]
	michelangelo.down()
	for i in A:
		for j in range(i):
			michelangelo.forward(lengthPolygon)
			michelangelo.left(360/i)
		michelangelo.clear()
	
	window.exitonclick()
main()