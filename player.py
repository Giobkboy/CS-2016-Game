from enum import Enum

#to create a differnt type of Entity add it to the ENUM here 
#this is so one can type all fo the entitys
class Entity_Type(Enum):
	DEFALT = 0
	PLAYER = 1
	#THING = NUM


#this class is the object for an "attack" when a player is
# "hit" it is passed an attack object with a name and a certan
# amount of HP
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
		
	#
		
class Entity:
	
	def __init__(self, name, coins = 0, hp = 100):
	
		self.name = name
		self.coins = coins #starts with no coins by default
		self.hitPoints = hp #you start with a HP coins
		
		self.isAlive = True
		self.attacks = {}
		
		
		
	def takeAttack(self, attack_obj):
		
		if attack_obj is Attack: #makes sure that attack object is being passed being 
			self.hitPoints = self.hitPoints - attack_obj.hitPoints
			if self.hitPoints < 0:
				self.isAlive = False
			
		else: 
			return -1
			
			
	def attack(self, e, attack_name):
	
		if e is Entity:
			if len(self.attacks) > 0:
				e.takeAttack(attacks[attack_name])
				
				
			
				
			 			
							