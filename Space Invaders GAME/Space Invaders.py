import os
import turtle as tr
import math
import random
import winsound
from playsound import playsound




wn=tr.Screen()
wn.bgcolor("black")
wn.title(" Space Invaders")
wn.bgpic("space.gif")
wn.tracer(0)

name=tr.Turtle()
name.speed(1)
name.color("white")
name.penup()
name.setposition(-285,0)
namegame = "Space Invaders by DIVAX SHAH" 
name.write(namegame,False,align="left",font=("arial",30,"normal"))
name.hideturtle()
playsound("intro1.wav")
name.clear()


tr.register_shape("alien.gif")
tr.register_shape("player.gif")
tr.register_shape("bullet.gif")

pen=tr.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.setposition(-300,-300)
pen.pendown()
pen.pensize(3)
for side in range(4):
    pen.fd(600)
    pen.lt(90)
pen.hideturtle()

score = 0
sp=tr.Turtle()
sp.speed(0)
sp.color("white")
sp.penup()
sp.setposition(-290,280)
scorestring = "score: %s" %score
sp.write(scorestring,False,align="left",font=("arial",14,"normal"))
sp.hideturtle()



pl=tr.Turtle()
pl.color("blue")
pl.shape("player.gif")
pl.speed(0)
pl.penup()
pl.setposition(0,-280)
pl.setheading(90)

ps=5

no_of_enemies=30
enemies = []
for i in range(no_of_enemies):
	enemies.append(tr.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number=0
for en in enemies:	
	en.color("red")
	en.speed(0)
	en.penup()
	en.shape("alien.gif")
	x = enemy_start_x + (50 * enemy_number)
	y=enemy_start_y
	en.setposition(x,y)
	enemy_number+=1
	en.setheading(90)
	if enemy_number == 10:
		
		enemy_start_y -= 50
		enemy_number=0


es=0.05

bullet = tr.Turtle( )
bullet.color("yellow")
bullet.shape ("bullet.gif")
bullet.penup ( )
bullet.speed(0)
bullet.setheading (90)
bullet.shapesize(0.6, 0.6)
bullet.hideturtle( )
bulletspeed = 5
bulletstate="Ready"

def move_left():
	x=pl.xcor()
	if x<-250:
		x=-250
	x-=ps
	pl.setx(x)
    

def move_right():
	x=pl.xcor()
	if x > 250:
		x = 250
	x+=ps
	pl.setx(x) 

def fire_bullet():
	global bulletstate
	if bulletstate == "Ready":
		play_sound("fire.wav")
		bulletstate = "fire"
		x = pl.xcor()
		y = pl.ycor()+ 10
		bullet.setposition(x,y)
		bullet.showturtle()

def isCollison(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
	if distance < 17:
		return True
	else:
		return False
def isCollisonn(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
	if distance < 17:
		return True
	else:
		return False
def play_sound(sound_file,time=0):
	winsound.PlaySound(sound_file,winsound.SND_ASYNC)

	if time > 0:
		tr.ontimer(lambda: play_sound(sound_file, time),t=int(time*1000))

	
	

	
tr.listen()
tr.onkey(move_left,"Left")
tr.onkey(move_right,"Right")
tr.onkey(fire_bullet,"space")
play_sound("intro.wav",34)



while True:
	wn.update()
	for en in enemies:
		x=en.xcor()
		x+=es
		en.setx(x)
		if en.xcor() > 280:
			for e in enemies:
				y = e.ycor()
				y-=40
				e.sety(y)
			es*=-1		
		if en.xcor() < -280:
			for e in enemies:
				y = e.ycor()
				y-=40
				e.sety(y)
			es*=-1
		if y < -300:
			pl.clear()
			en.clear()
			bullet.clear()
			ST=tr.Turtle()
			ST.speed(1)
			ST.color("red")
			ST.penup()
			ST.setposition(-270,200)
			STGAME= "YOU LOSE" 
			ST.write(STGAME,False,align="left",font=("arial",40,"normal"))
			ST.hideturtle()
			playsound("intro1.wav")
			ST.clear()
			tr.Screen().bye()
		if isCollison( bullet, en):
			play_sound("collison.wav")
			bullet.hideturtle()
			bulletstate="Ready"
			bullet.setposition(0,-400)
			en.setposition(0,10000)
			score += 10
			scorestring = "score: %s" %score
			sp.clear()
			sp.write(scorestring,False,align="left",font=("arial",14,"normal"))

		if isCollisonn(pl,en):
			play_sound("collison.wav")
			pl.hideturtle()
			en.hideturtle()
			pl.clear()
			en.clear()
			bullet.clear()
			ST=tr.Turtle()
			ST.speed(1)
			ST.color("red")
			ST.penup()
			ST.setposition(-270,200)
			STGAME= "YOU LOSE" 
			ST.write(STGAME,False,align="left",font=("arial",40,"normal"))
			ST.hideturtle()
			playsound("intro1.wav")
			ST.clear()
			tr.Screen().bye()
	if bulletstate == "fire":
		y=bullet.ycor()
		y+=bulletspeed
		bullet.sety(y)
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate="Ready"
	
	if score == 300:
		pl.clear()
		en.clear()
		bullet.clear()
		EX=tr.Turtle()
		EX.speed(1)
		EX.color("yellow")
		EX.penup()
		EX.setposition(-285,200)
		EXGAME= "YOU WON" 
		EX.write(EXGAME,False,align="left",font=("arial",30,"normal"))
		EX.hideturtle()
		playsound("intro1.wav")
		EX.clear()
		break
tr.Screen().bye()





	


