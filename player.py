from enum import Enum

#to create a differnt type of Entity add it to the ENUM here 
#this is so one can type all fo the entities
class Entity_Type(Enum):
	DEFALT = 0
	PLAYER = 1
	#THING = NUM

##################################################################
#this class is the object for an "attack" when a player is		 #
# "hit" it is passed an attack object with a name and a certan   #
# amount of HP													 #
##################################################################
class Attack:
	
	#this the the constructor
	# name --- the name o the attack
	# hp --- the amount of hit points subtracted form the payers HP
	# message --- message displayed if killed
	def __init__(self, name, hp, message):
	
		self.name = name
		self.hitPoints = hp
		self.message = message
		
	# getter for hit points
	def get_hp(self):
		return self.hitPoints
		
	#getter for name
	def get_name(self):
		return self.name
		
	#this method return the message displayed on death
	def get_message(self):
		return self.message


##################################################################
# this class is the class for every entity for the game to create#
# a different type of enitty add one to the ENUM Entity_Type      #
##################################################################
class Entity:
	
	
	#constructor
	# name -- name of the player
	# coins -- the amount of currancey (init 0)
	# hp -- the amount of hit points to a Entity (init 100)
	def __init__(self, name, coins = 0, hp = 100):
	
		self.name = name
		self.coins = coins #starts with no coins by default
		self.hitPoints = hp #you start with a HP coins
		
		self.isAlive = True
		self.attacks = {}
		
		
	# pass an attack object to have an attack against a player
	# the amount of hp is 
	def takeAttack(self, attack_obj):
		
		if attack_obj is Attack: #makes sure that attack object is being passed being 
			self.hitPoints = self.hitPoints - attack_obj.get_hp()
			if self.hitPoints < 0:
				self.isAlive = False
		else: 
			return -1
			
			
	def attack(self, e, attack_name):
	
		if e is Entity:
			if len(self.attacks) > 0:
				e.takeAttack(attacks[attack_name])
				
				
			
				
			 			
							