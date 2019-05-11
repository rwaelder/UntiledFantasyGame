# Armor class

from item import *


class Armor(Item):

	def __init__(self, name, defence, section):
		super().__init__(name, True)
		self.defence = defence
		self.section = section
