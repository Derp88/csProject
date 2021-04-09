#AP CS Project
#Created by Dylan Barkley and Caleb Obenchain
#Uses Python Turtle Library

import turtle as trtl 

#Variables
v_gameOver = False
v_bulletNum = -1
v_positionCheckerCount = 0
v_gameStarted = False

#List
activeBulletList = []

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

#Functions
def initGame():
    player.showturtle()
    wn.bgpic("black.gif")

def mouseAim(X,Y):
    player.setheading(player.towards(X,Y))

def playerLeft():
    if player.xcor() > -280:
        player.setposition(player.xcor()-5, player.ycor())

def playerRight():
    if player.xcor() < 280:
        player.setposition(player.xcor()+5, player.ycor())

def generateBullet(X,Y, HEADING):
    global v_bulletNum

    #Makes bullet
    v_bulletNum = v_bulletNum + 1
    bullet = trtl.Turtle()
    bullet.penup()
    bullet.color("White")
    activeBulletList.append(bullet)
    

    #Sets bullet
    activeBulletList[v_bulletNum].setx(X)
    activeBulletList[v_bulletNum].sety(Y)
    activeBulletList[v_bulletNum].setheading(HEADING)
    wn.update()

def moveBullet():
    wn.update()
    global v_bulletNum
    global BulletX
    global BulletY
    global BulletHeading
    global v_positionCheckerCount
    

    for activeBullet in activeBulletList:
        v_positionCheckerCount = v_positionCheckerCount + 1
        #Reports bullet current position to collision checker
        if v_positionCheckerCount % 100 == 0:
            BulletX = activeBullet.xcor()
            BulletY = activeBullet.ycor()
            BulletHeading = activeBullet.heading()
        
        activeBullet.sety(activeBullet.ycor()-.1)

        #This removes the bullet when it goes out of bounds
        if activeBullet.xcor() > 300 or activeBullet.xcor() < -300 or activeBullet.ycor() > 300 or activeBullet.ycor() < -300:
            activeBullet.hideturtle()
            activeBulletList.remove(activeBullet)
            v_bulletNum = v_bulletNum - 1

def startGame():
    global v_gameStarted
    if v_gameStarted == False:
        v_gameStarted = True
        initGame()

def mainPerodic():
    moveBullet()



#Inputs
wn.onscreenclick(mouseAim)
wn.onkeypress(playerLeft, "a")
wn.onkeypress(playerRight, "d")
wn.onkeypress(startGame, "p")
wn.listen()

#Game Loop
while v_gameOver == False:
    wn.update()
    mainPerodic()

    




