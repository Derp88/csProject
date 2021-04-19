#AP CS Project
#Created by Dylan Barkley and Caleb Obenchain
#Uses Python Turtle Library and random

import turtle as trtl 
import random

#Variables
v_gameOver = False
v_bulletNum = -1
v_gameStarted = False
v_dodged = 0

#Lists
activeBulletList = []
spawnTimerList = [500,200,700]

#Game (WN) screen setup
wn = trtl.Screen()
wn.bgcolor("Black")
background = "start.gif"
wn.bgpic(background)
wn.tracer(0)
wn.addshape("badboy1.gif")
wn.addshape("badboy2.gif")
wn.addshape("badboy3.gif")

#Player Turtle
player = trtl.Turtle()
player.color("White")
player.penup()
player.goto(0,-300)
player.setheading(90)
player.shapesize(5)
player.hideturtle()

#Score Turtle
scoreTurtle = trtl.Turtle()
scoreTurtle.hideturtle()
scoreTurtle.color("White")
scoreTurtle.penup()
scoreTurtle.goto(0,334)

#Functions
def initGame():
    player.showturtle()
    wn.bgpic("background.gif")
    
def playerLeft():
    if player.xcor() > -180:
        player.setposition(player.xcor()-15, player.ycor())

def playerRight():
    if player.xcor() < 180:
        player.setposition(player.xcor()+15, player.ycor())

#Makes bullet
def generateBullet(X,Y, HEADING):
    global v_bulletNum

    v_bulletNum = v_bulletNum + 1
    bullet = trtl.Turtle()
    bullet.penup()
    v_imageRandomizer = random.randint(0,2)
    #Sets bullet image
    if v_imageRandomizer == 0:
        bullet.shape("badboy1.gif")
    elif v_imageRandomizer == 1:
        bullet.shape("badboy2.gif")
    else:
        bullet.shape("badboy3.gif")

    #Adds bullet to list
    activeBulletList.append(bullet)

    #Sets bullet
    activeBulletList[v_bulletNum].setx(X)
    activeBulletList[v_bulletNum].sety(Y)
    activeBulletList[v_bulletNum].setheading(HEADING)
    wn.update()

#Moves bullet down the screen
def moveBullet():
    wn.update()
    global v_bulletNum
    global v_dodged
    global v_gameOver
    
    #Goes through list of all active bullets and moves them
    for activeBullet in activeBulletList:
        activeBullet.sety(activeBullet.ycor() - .4)

        #This removes the bullet when it goes out of bounds and adds it to the score counter
        if activeBullet.xcor() > 300 or activeBullet.xcor() < -300 or activeBullet.ycor() > 300 or activeBullet.ycor() < -350:
            activeBullet.hideturtle()
            activeBulletList.remove(activeBullet)
            v_bulletNum = v_bulletNum - 1
            v_dodged = v_dodged + 1
            scoreTurtle.clear()
            scoreTurtle.write("Score: " + str(v_dodged),align="center", font=("Arial", 20, "normal"))

        #Checks for collison with player
        if player.distance(activeBullet.xcor(), activeBullet.ycor()) < 25:
            v_gameOver = True
        
#Chooses where on the screen the bullet will spawn
def spawnBullet():
    spawnTimerList[0] = spawnTimerList[0] + 1
    spawnTimerList[1] = spawnTimerList[1] + 1
    spawnTimerList[2] = spawnTimerList[2] + 1
    randomReset0 = random.randint(500,300000)
    randomReset1 = random.randint(500,300000)
    randomReset2 = random.randint(500,300000)
    if spawnTimerList[0] > randomReset0:  
        generateBullet(-40+random.randint(0,80),300, 270)
        spawnTimerList[0] = 0
    if spawnTimerList[1] > randomReset1:
        generateBullet(110+random.randint(0,80),300, 270)
        spawnTimerList[1] = 0
    if spawnTimerList[2] > randomReset2:
        generateBullet(-190+random.randint(0,80),300, 270)
        spawnTimerList[2] = 0

#Starts the game once "P" has been pressed 
def startGame():
    global v_gameStarted
    if v_gameStarted == False:
        v_gameStarted = True
        initGame()

#Calls functions that neeed to be constantly called, moveBullet and spawnBullet
def mainPerodic():
    global v_gameStarted
    if v_gameStarted == True:
        moveBullet()
        spawnBullet()

#Inputs
wn.onkeypress(playerLeft, "a")
wn.onkeypress(playerRight, "d")
wn.onkeypress(startGame, "p")
wn.listen()

#Game Loop
while v_gameOver == False:
    wn.update()
    mainPerodic()
