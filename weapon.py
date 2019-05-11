# Weapon class

from item import *

class Weapon(Item):

	def __init__(self, name, attack, numHands):
		super().__init__(name, True)
		self.attack = attack
		self.numHands = numHands
