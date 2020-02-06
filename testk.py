import random
import turtle
 
#거북이로 동그라미까지 이동하기
 
player = turtle.Turtle()  #사용할 거북이
player.color("blue")
player.shape("turtle")
player.speed(0)
player.penup()
player.goto(random.randint(-300,300), random.randint(-300, 300))
screen = player.getscreen()
 
a1 = turtle.Turtle() #목표지점1
a1.color("red")
a1.shape("circle")
a1.speed(0)
a1.penup()
a1.goto(random.randint(-300,300), random.randint(-300, 300))
 
a2 = turtle.Turtle() #목표지점1
a2.color("red")
a2.shape("circle")
a2.speed(0)
a2.penup()
a2.goto(random.randint(-300,300), random.randint(-300, 300))
 
def left() :
        player.left(90)
def right():
        player.right(90)
def up() :
        player.forward(30)
def down() :
        player.backward(30)
 
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.listen()
 
 
def play() :
        player.forward(0)
        a1.forward(0)
        a2.forward(0)
        screen.ontimer(play, 100)
 
screen.ontimer(play, 100)
input()