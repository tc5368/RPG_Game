
from Hero_Class import *
from Map_Class import *


def intro():
	global player
	print('Welcome to the dungeon run!')
	print('First things first select a class from the selection below:')
	print()
	role = choose_class_menu()

	#mode = print('Are you playing alone or Co-op ?')
	#Just an idea for maybe a multiplayer mode, each take a turn
	#each or battle each other.

	name = str(input('Now to name your Character: '))
	player  = Hero(name,role)
	print()
	print('Ok set the scene here, give the task (kill 2 monsters and find an item)')
	print()
	player.showStats()



def choose_class_menu():
	'''Someone write a menu to explain the different stats and also then take
	   a player input and then check if its a valid class option, if so then
	   return the class by default everyone is a Barbarian'''
	return Barbarian




if __name__ == '__main__':
	intro()