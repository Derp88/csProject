#AP CS Project
#Created by Dylan Barkley and Caleb Obenchain
#Uses Python Turtle Library

import turtle as trtl 
import random

#Variables
v_gameOver = False
v_bulletNum = -1
v_gameStarted = False
v_dodged = 0

#List
activeBulletList = []
spawnTimerList = [500,200,700,900,0]


#Game (WN) screen setup
wn = trtl.Screen()
wn.bgcolor("Black")
background = "start.gif"
wn.bgpic(background)
wn.tracer(0)

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

#Functions
def initGame():
    player.showturtle()
    wn.bgpic("black.gif")

def playerLeft():
    if player.xcor() > -180:
        player.setposition(player.xcor()-15, player.ycor())


def playerRight():
    if player.xcor() < 180:
        player.setposition(player.xcor()+15, player.ycor())


def generateBullet(X,Y, HEADING):
    global v_bulletNum

    #Makes bullet
    v_bulletNum = v_bulletNum + 1
    bullet = trtl.Turtle()
    bullet.penup()
    bullet.color("White")
    wn.addshape("badboy1.gif")
    bullet.shape("badboy1.gif")
    bullet.shapesize(12)
    activeBulletList.append(bullet)

    #Sets bullet
    activeBulletList[v_bulletNum].setx(X)
    activeBulletList[v_bulletNum].sety(Y)
    activeBulletList[v_bulletNum].setheading(HEADING)
    wn.update()

def moveBullet():
    wn.update()
    global v_bulletNum
    global v_dodged
    global v_gameOver
    
    for activeBullet in activeBulletList:
        #activeBullet.forward(.4)
        activeBullet.sety(activeBullet.ycor() - .4)

        #This removes the bullet when it goes out of bounds and adds it to the score counter
        if activeBullet.xcor() > 300 or activeBullet.xcor() < -300 or activeBullet.ycor() > 300 or activeBullet.ycor() < -350:
            activeBullet.hideturtle()
            activeBulletList.remove(activeBullet)
            v_bulletNum = v_bulletNum - 1
            v_dodged = v_dodged + 1
            scoreTurtle.clear()
            scoreTurtle.write(v_dodged,align="center", font=("Arial", 20, "normal"))

        #Checks for collison
        if player.distance(activeBullet.xcor(), activeBullet.ycor()) < 25:
            v_gameOver = True
            

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
        
def startGame():
    global v_gameStarted
    if v_gameStarted == False:
        v_gameStarted = True
        initGame()

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

    




