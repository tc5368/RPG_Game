#Game Template.py


class Hero():
	def __init__(self,Name,Role):
		#Basic Setup for thing not unique to Role
		self.name = Name
		self.role = Role
		self.inventory = []

		#Setup for other characteristics
		self.health = self.role[0]
		self.speed  = self.role[1]
		self.mana   = self.role[2]

	def addToInventory(self,item):
		#This will add items to the characters inventory
		self.inventory.append(item)

	def showStats(self):
		#This prints all the players stats
		print('%s\'s  Stats: ' %self.name)
		print('Health: %s' %self.health)
		print('Speed: %s' %self.speed)
		print('Mana: %s' %self.mana)
		print('\nInventory: ')
		self.showInventory()

	def showInventory(self):
		for i in range(len(self.inventory)):
			print(inventory[i])


#This is going to be where all the possible Class choices will be.
#Each class has the same base features and they will go into the base array like so:
# [Health,Speed,Mana]

Barbarian = [30,30,00]
Wizard    = [15,15,30]
Ranger    = [15,20,15]


























































