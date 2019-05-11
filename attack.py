# Attack class
from random import randint


class Attack:

	def __init__(self, name, damage, accuracy, isMagic, manaCost):
		self.name = name
		self.damage = damage
		self.accuracy = accuracy
		self.isMagic = isMagic
		self.manaCost = manaCost
		self.isHeal = False

	def __str__(self):
		if self.isMagic:
			return '%s | %i mana' % ('{:<10}'.format(self.name), self.manaCost)
		else:
			return self.name

	def use_attack(self, user):
		if self.isMagic:
			if user.mana < self.manaCost:
				damage = 0
				text = 'doesn\'t have enough mana to hit'
				return damage, text
			else:
				user.use_mana(self.manaCost)
		chance = randint(1,100)
		if chance > self.accuracy:
			damage = 0
			text = 'missed'
		elif chance == self.accuracy:
			damage = int(self.damage / 2)
			text = 'grazed'
		else:
			damage = self.damage
			text = 'hit'
		return damage * user.damageModifier, text



	def power_up(self):
		input('%s is now more powerful!' % self.name)
		self.damage += int(self.damage/3)

	def save(self):
		return '%s,%i,%i,%s,%i' % (self.name, self.damage, self.accuracy, self.isMagic, self.manaCost)

class Heal(Attack):

	def __init__(self, name, healPower, accuracy, isMagic, manaCost):
		super().__init__(name, 0, accuracy, isMagic, manaCost)
		self.isHeal = True
		self.healPower = healPower


	def use_heal(self, user):
		if self.isMagic:
			if user.mana < self.manaCost:
				return 0, 'doesn\'t have enough mana to heal'
			else:
				user.use_mana(self.manaCost)
		chance = randint(1,100)
		if chance > self.accuracy:
			return 0, 'missed'
		elif chance == self.accuracy:
			return int(self.healPower / 2), 'grazed'
		else:
			return self.healPower, 'healed'

	def power_up(self):
		input('%s is now more powerful!' % self.name)
		self.healPower += int(self.healPower/3)

	def save(self):
		return '%s,%i,%i,%s,%i' % (self.name, self.healPower, self.accuracy, self.isMagic, self.manaCost)
#attackList = {'Struggle' : Attack('Struggle', )}