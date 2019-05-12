# Base creature class
from attack import Attack
class Creature:

	def __init__(self, name, level, hp, mana):
		self.name = name
		self.level = level
		self.maxHP = hp
		self.hp = hp
		self.maxMANA = mana
		self.mana = mana
		self.totalEXP = 0
		self.exp = 0
		self.isDefending = False
		self.attacks = {'Struggle' : Attack('Struggle', 2+int(level/2) , 50, False, 0)}
		self.levelUpStats = {'HP' : 0, 'Mana' : 0}
		self.kind = ''
		self.defendModifier = 2
		self.isDead = False
		self.heals = {}
		self.levelUpMoves = {}
		self.action = ''
		self.damageModifier = 1
		self.gold = 0


	def load_hp_mana_exp(self, hp, mana, exp, totalEXP):
		self.hp = hp
		self.maxHP = hp
		self.mana = mana
		self.maxMANA = mana
		self.exp = exp
		self.totalEXP = totalEXP

	def add_attack(self, attack, verbose=False):
		if 'Struggle' in self.attacks:
			del self.attacks['Struggle']
		if verbose:
			input('%s learned %s!' % (self.name, attack.name))

		self.attacks[attack.name] = attack

	def add_heal(self, heal, verbose=False):
		if verbose:
			input('%s learned %s!' % (self.name, heal.name))
		self.heals[heal.name] = heal


	def defend_damage_modifier(self, damage):
		return int(damage/self.defendModifier)

	def defend_heal_modifier(self, healPower):
		return int(healPower*self.defendModifier)

	def take_damage(self, damage):
		if self.isDefending:
			input('%s is defending!' % self.name)
			damage = self.defend_damage_modifier(damage)
		input('%s took %i damage!\n' % (self.name, damage))
		if self.hp - damage <= 0:
			self.hp = 0
			self.isDead = True
			input('%s is dead!' % self.name)
		else:
			self.hp -= damage
			


	def restore_hp(self, healPower):
		if self.isDefending:
			input('%s is defending!' % self.name)
			healPower = self.defend_heal_modifier(healPower)
		input('%s healed %i HP!' % (self.name, healPower))
		if self.hp + healPower > self.maxHP:
			self.hp = self.maxHP
		elif self.isDead:
			if healPower - self.level > 0:
				self.isDead = False
				self.hp += healPower - self.level
			else:
				print('Not enough healing power to revive %s' % self.name)
		else:
			self.hp += healPower


	def restore_mana(self, power):
		input('%s recovered %i mana!' %(self.name, power))
		if self.mana + power > self.maxMANA:
			self.mana = self.maxMANA
		else:
			self.mana += power

	def full_hp(self):
		self.hp = self.maxHP
		self.isDead = False

	def full_mana(self):
		self.mana = self.maxMANA

	def use_mana(self, manaCost):
		self.mana -= manaCost

	def HP(self):
		return 'HP: %i/%i' % (self.hp, self.maxHP)

	def MANA(self):
		return 'Mana: %i/%i' % (self.mana, self.maxMANA)

	def defend(self):
		self.isDefending = True

	def reset(self):
		self.isDefending = False
		self.action = ''
		self.damageModifier = 1

	def end_battle_reset(self):
		self.isDefending = False
		self.action = ''
		self.damageModifier = 1

	def __str__(self):
		return '%s lv. %i\t%s\t%s' % ('{:<15}'.format(self.name), self.level, self.HP(), self.MANA())

	def get_exp(self):
		return self.exp

	def get_hp(self):
		return self.hp




