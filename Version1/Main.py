
#Import the aid module
from Tools import *

#Import randint
from random import randint
from random import choice

#Init an aid of size 400x600
global game
game = Aid(400, 600)

#Add the three power ups to the game
game.addRect("sheildPowerUp",imgLoc="res/ShieldIcon.png", layer=1)
game.addRect("shootPowerUp", imgLoc="res/ShootIcon.png", layer=1)
game.addRect("slowPowerUp", imgLoc="res/SlowIcon.png", layer=1)

#Add the player as a black 50x100 rectangle on the second layer 
game.addRect("player", width=50, height=90, colour=(0, 0, 0), layer=2)

for x in range(4):
	#Add in four enemies as red 50x100 rectangles 
	game.addRect("enemy{}".format(x), width=50, height=90, layer=2)

#Position the three power ups in a line across the top of the screen
game.sheildPowerUp.x = game.width / 2 - game.sheildPowerUp.width / 2
game.shootPowerUp.x = game.sheildPowerUp.x - game.sheildPowerUp.width / 2 - game.shootPowerUp.width / 2
game.slowPowerUp.x = game.sheildPowerUp.x + game.sheildPowerUp.width / 2 + game.sheildPowerUp.width / 2

#Position the player
game.player.x = game.width / 2 - game.player.width / 2
game.player.y = game.height - game.player.height - (game.height / 10)

#Define a list x positions the enemies can travel down
global enemyLanes
enemyLanes = [(400 / 5 * 1) - game.enemy0.width / 2, (400 / 5 * 2) - game.enemy0.width / 2, (400 / 5 * 3) - game.enemy0.width / 2, (400 / 5 * 4) - game.enemy0.width / 2]

#Define a speed variable to be applied to all enemies
global enemySpeed
enemySpeed = 0

#Define a score
score = 0

#Define a function to reposition the enemies
def resetEnemies(score):

	#Use the global variables
	global enemyLanes
	global enemySpeed
	global game


	#Make a scaling difficulty on the size of the gaps between the oncoming enemies
	if 150 - (int(score) / 10) >= game.player.height * 1.2:
		enemyDistance = int(100 - int(score))

	else:
		enemyDistance = game.player.height * 1.2

	#Set the first enemy to be place at y = -100
	currentDistance = - 100

	#Iterate through the four enemies
	for x in range(4):
		#Set the y to the defined current distance var
		eval("game.enemy{}".format(x)).y = currentDistance
		#Set the x to a random choice of the list
		eval("game.enemy{}".format(x)).x = choice(enemyLanes)
		#Minis the size from the current distance
		currentDistance = currentDistance - enemyDistance - game.player.height

	#Create a scaling speed
	if 5 + int(score / 5) > 10:
		enemySpeed = 5 + int(score / 5)

	else:
		enemySpeed = 10

#Reset the enemies
resetEnemies(score)

#Run our game loop
while 1:

	#Iterate through the four enemies and move them downwards
	for x in range(4):
		eval("game.enemy{}".format(x)).y += enemySpeed

	#If the fourth and final enemy has gone off screen
	if game.enemy3.y >= game.height:
		#Add one to the score
		score += 1
		#Reset the enemies
		resetEnemies(score)

	#Update the game
	game.update()