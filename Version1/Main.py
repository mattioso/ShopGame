
#Import the aid module
from Tools import *

#Init an aid of size 600x600
game = Aid(400, 600)

#Add the three power ups to the game
game.addRect("sheildPowerUp",imgLoc="res/ShieldIcon.png", layer=1)
game.addRect("shootPowerUp", imgLoc="res/ShootIcon.png", layer=1)
game.addRect("slowPowerUp", imgLoc="res/SlowIcon.png", layer=1)

#Add the player as a black 50x100 rectangle on the second layer 
game.addRect("player", width=50, height=100, colour=(0, 0, 0), layer=2)

for x in range(4):
	#Add in four enemies as red 50x100 rectangles 
	game.addRect("enemy{}".format(x), width=50, height=100, layer=2)

#Position the three power ups in a line across the top of the screen
game.sheildPowerUp.x = game.width / 2 - game.sheildPowerUp.width / 2
game.shootPowerUp.x = game.sheildPowerUp.x - game.sheildPowerUp.width / 2 - game.shootPowerUp.width / 2
game.slowPowerUp.x = game.sheildPowerUp.x + game.sheildPowerUp.width / 2 + game.sheildPowerUp.width / 2

#Position the player
game.player.x = game.width / 2 - game.player.width / 2
game.player.y = game.height - game.player.height - (game.height / 10)

while 1:

	game.update()