#AP CS Project
#Created by Dylan Barkley and Caleb Obenchain
#Uses Python Turtle Library

import turtle as trtl 

#Variables
v_gameOver = False

#Game (WN) screen setup
wn = trtl.Screen()
wn.bgcolor("Black")
#background = "iceMap.gif"
#wn.bgpic(background)
wn.tracer(0)

#Player Turtle
player = trtl.Turtle()
player.color("White")
player.penup()
player.goto(0,-300)
player.setheading(90)

#Functions
def mouseAim(X,Y):
    player.setheading(player.towards(X,Y))

def playerLeft():
    if player.xcor() > -300:
        player.setposition(player.xcor()-1, player.ycor())

def playerRight():
    if player.xcor() < 300:
        player.setposition(player.xcor()+1, player.ycor())

#Inputs
wn.onscreenclick(mouseAim)
wn.onkeypress(playerLeft, "a")
wn.onkeypress(playerRight, "d")
wn.listen()

while True:
    wn.update()




