#pong
#ctrl-k ctrl-c to comment out a selected block
#c-k then c-u to uncomment 

from re import S
from tkinter import W
import turtle

#params
paddleSizeX = 5
paddleSizeY = 1
paddleMoveRate = 20

#window
window = turtle.Screen()
window.title("Pong by mettagame")
window.bgcolor("black")
window.setup(width=800, height=600) #0,0 is centre of screen
window.tracer(0) #prevent window from auto updating

def makePaddle(color, width, spawnPos):
    obj = turtle.Turtle() #create a turtle object
    obj.speed(0) #animation speed. 0 = max?
    obj.shape("square")
    obj.shapesize(stretch_wid=width, stretch_len=paddleSizeY)
    obj.color(color)
    obj.penup() #dont draw a line
    obj.goto(spawnPos, 0)
    return obj

#make paddles & ball
paddleLeft = makePaddle("white", paddleSizeX, -350)
paddleRight = makePaddle("white", paddleSizeX, 350)
ball = makePaddle("grey", paddleSizeY, 0)

#move paddles
# def moveLeft():
#     y = paddleLeft.ycor()
#     y += 100
#     paddleLeft.sety(y)
def moveLeft(dir):
    paddleLeft.sety(paddleLeft.ycor() + dir * paddleMoveRate)

def moveRight(direction): #this should work logigally, right?
    paddleRight.sety(paddleRight.ycor() + direction*paddleMoveRate)   

#keyboard bindings
window.listen()
window.onkeypress(lambda n=1: moveLeft(n), "w") #cannot use input params for a fn called within onkeypress. dummy lambda fn as first hit as workaround
window.onkeypress(lambda n=-1: moveLeft(n), "s")
window.onkeypress(lambda n=1: moveRight(n), "Up")
window.onkeypress(lambda n=-1: moveRight(n), "Down")

# window.onkeypress(moveLeft(), "Down")


#game loop
while True:
    window.update() 