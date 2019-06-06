from creature import Creature
from attack import Attack, Heal
from random import randint, choice

class Enemy(Creature):

	def choose_action(self, party):
		if self.isDead:
			self.action = 'nothing'

		act = randint(1, 100)

		if 'heal' in self.behavior:
			nothingCutoff = self.behavior['nothing']
			defendCutoff = nothingCutoff + self.behavior['defend']
			attackCutoff = defendCutoff + self.behavior['attack']
			healCutoff = attackCutoff + self.behavior['heal']

			if act <= nothingCutoff:
				self.action = 'nothing'
			elif act <= defendCutoff:
				self.action = 'defend'
			elif act <= attackCutoff:
				self.action = 'attack'
			else:
				self.action = 'heal'
		else:	
			nothingCutoff = self.behavior['nothing']
			defendCutoff = nothingCutoff + self.behavior['defend']
			attackCutoff = defendCutoff + self.behavior['attack']

			if act <= nothingCutoff:
				self.action = 'nothing'
			elif act <= defendCutoff:
				self.action = 'defend'
			else:
				self.action = 'attack'



	def choose_attack(self):
		atk = choice(list(self.attacks.keys()))
		print('%s used %s!' % (self.name, atk))
		return self.attacks[atk]

	def choose_heal(self):
		hl = choice(list(self.heals.keys()))
		print('%s used %s!' % (self.name, hl))
		return self.heals[hl]


	def is_player(self):
		return False

# ------ Orcs ---------------------------------------------------------

class Orc(Enemy):

	def __init__(self, level):
		hp, attackDamage, exp, gold = Orc.set_stats(level)
		super().__init__('Orc', level, hp, 0)
		self.add_attack(Attack('Bash', attackDamage, 90, False, 0))
		self.exp = exp
		self.behavior = {'attack' : 80, 'defend' : 0, 'nothing' : 20}
		self.gold = gold

	def set_stats(level):
		hp = 15 + 4*level
		attackDamage = 6 + level
		exp = 10 + 4*level
		gold = 6
		return hp, attackDamage, exp, gold

class OrcShaman(Enemy):

	def __init__(self, level):
		hp, mana, attackDamage, healPower, exp, gold = OrcShaman.set_stats(level)
		super().__init__('Orc Shaman', level, hp, mana)
		self.add_attack(Attack('Bash', attackDamage, 70, False, 0))
		self.add_heal(Heal('Heal', healPower, 90, True, 4))
		self.exp = exp
		self.behavior = {'attack' : 30, 'defend' : 20, 'heal' : 40, 'nothing' : 10}
		self.defendModifier = 1

	def set_stats(level):
		hp = 13 + 2*level
		mana = 8 + 2*level
		attackDamage = 2 + level
		healPower = 5 + int(3/2*level)
		exp = 14 + 2*(level+1)
		gold = int(level/2)
		return hp, mana, attackDamage, healPower, exp, gold

class OrcLeader(Enemy):

	def __init__(self, level):
		hp, attackDamage, exp, gold = OrcLeader.set_stats(level)
		super().__init__('Orc Leader', level, hp, 0)
		self.add_attack(Attack('Bash', attackDamage, 90, False, 0))
		self.add_attack(Attack('Toss', attackDamage*2, 45, False, 0))
		self.exp = exp
		self.gold = gold
		self.behavior = {'attack' : 70, 'defend' : 25, 'nothing' : 5}
		self.defendModifier = 1.5
	
	def set_stats(level):
		hp = 25 + 5*level
		attackDamage = 6 + level
		exp = 15 + 10*level
		gold = 50
		return hp, attackDamage, exp, gold

class OrcBerserker(Enemy):

	def __init__(self, level):
		hp, attackDamage, exp, gold = OrcBerserker.set_stats(level)
		super().__init__('Orc Berserker', level, hp, 0)
		self.add_attack(Attack('Smash', attackDamage, 85, False, 0))
		self.exp = exp
		self.behavior = {'attack' : 90, 'defend' : 0, 'nothing' : 10}
		self.gold = gold
		self.berserkChance = 25 + int(level/2)

	def set_stats(level):
		hp = 15 + 4*level
		attackDamage = 6 + level
		exp = 10 + 4*level
		gold = 8
		return hp, attackDamage, exp, gold

	def go_berserk(self):
		input('%s is going berserk!' % self.name)
		self.hp = int(self.maxHP/2)
		self.damageModifier *= 2

	def reset(self):
		self.isDefending = False
		self.action = ''

	def take_damage(self, damage):
		if self.isDefending:
			input('%s is defending!' % self.name)
			damage = self.defend_damage_modifier(damage)
		input('%s took %i damage!' % (self.name, damage))

		if self.hp - damage <= 0:
			chance = randint(1,100)
			if chance < self.berserkChance:
				self.go_berserk()
			else:
				self.hp = 0
				self.isDead = True
				input('%s is dead!' % self.name)
		else:
			self.hp -= damage

class OrcPeon(Enemy):

	def __init__(self, level):
		hp, attackDamage, exp, gold = OrcPeon.set_stats(level)
		super().__init__('Orc Peon', level, hp, 0)
		self.exp = exp
		self.behavior = {'attack' : 50, 'defend' : 10, 'nothing' : 40}
		self.gold = gold

	def set_stats(level):
		hp = 6 + 4*level
		attackDamage = 6 + level
		exp = 5 + 4*level
		gold = 3
		return hp, attackDamage, exp, gold


class Goblin(Enemy):

	def __init__(self, level):
		hp, attackDamage, exp, gold = Goblin.set_stats(level)
		super().__init__('Goblin', level, hp, 0)
		self.add_attack(Attack('Scratch', attackDamage, 100, False, 0))
		self.exp = exp
		self.behavior = {'attack' : 70, 'defend' : 20, 'nothing' : 10}
		self.defendModifier = 1.5

	def set_stats(level):
		hp = 8 + 2*level
		attackDamage = 4 + level
		exp = 6 + 2*level
		gold = 8 + int(level/2)
		return hp, attackDamage, exp, gold