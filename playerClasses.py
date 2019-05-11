# Player class
from creature import Creature
from attack import Attack, Heal
from random import randint
from misc import isInt

classes = ['Warrior', 'Mage', 'Sage', 'Berserker']

class Player(Creature):
	

	def gain_exp(self, expGain):
		if self.level == 100:
			return
		self.totalEXP += expGain

		while expGain > 0:
			levelUp = 50 + int(25*(self.level-1)**2/2)
			if self.exp + expGain >= levelUp:
				expGain = expGain - (levelUp - self.exp)
				self.level_up()
				self.exp = 0
			else:
				self.exp += expGain
				expGain = 0

	def is_player(self):
		return True

	def level_up(self):
		self.level += 1
		print('%s has reached level %i!' % (self.name, self.level))
		self.maxHP += self.levelUpStats['HP']
		self.maxMANA += self.levelUpStats['Mana']
		self.hp = self.maxHP
		self.mana = self.maxMANA
		input('%s now has %i HP and %i mana!' % (self.name, self.hp, self.mana))
		self.new_moves()

		if self.level % 5 == 0:
			for attack in list(self.attacks.keys()):
				self.attacks[attack].power_up()
			for heal in list(self.heals.keys()):
				self.heals[heal].power_up()

	def choose_heal(self):
		hls = list(self.heals.keys())
		print('------------- Heals -----------------------------------')
		for i in range(len(hls)):
			print('[%i] %s' % (i, self.heals[hls[i]]))
		selection = -1
		while selection not in range(len(hls)):
			stream = input('Choose attack number for %s: ' % self.name).rstrip()
			if isInt(stream):
				selection = int(stream)
		print('\n%s used %s!' % (self.name, hls[selection]))
		return self.heals[hls[selection]]

	def choose_attack(self):
		atks = list(self.attacks.keys())
		print('------------- Attacks ---------------------------------')
		for i in range(len(atks)):
			print('[%i] %s' % (i, self.attacks[atks[i]]))
		selection = -1
		while selection not in range(len(atks)):
			stream = input('Choose attack number for %s: ' % self.name).rstrip()
			if isInt(stream):
				selection = int(stream)
		print('\n%s used %s!' % (self.name, atks[selection]))

		return self.attacks[atks[selection]]

	def choose_action(self, party):
		if self.isDead:
			self.action = 'nothing'
			return
		actions = ['attack', 'defend', 'nothing']
		actList = '[Attack, Defend, '
		if self.heals:
			actions.append('heal')
			actList += 'Heal, '
		if party.has_battle_items():
			actions.append('item')
			actList += 'Item, '
		actList += 'Nothing]'
		action = ''
		while action not in actions:
			action = input('Choose action for %s %s\n' % (self.name, actList)).lower().rstrip()
		self.action = action

	def load_character(self, level, hp, mana, exp, totalEXP, attacks, heals):
		self.level = level
		self.load_hp_mana_exp(hp, mana, exp, totalEXP)

		for attack in attacks:
			info = attack.split(',')
			isMagic = False
			if info[3] == 'True':
				isMagic = True
			atk = Attack(info[0], int(info[1]), int(info[2]), isMagic, int(info[4]))
			self.add_attack(atk)

		for heal in heals:
			info = heal.split(',')
			isMagic = False
			if info[3] == 'True':
				isMagic = True
			atk = Heal(info[0], int(info[1]), int(info[2]), isMagic, int(info[4]))
			self.add_heal(atk)

	def new_moves(self):
		if self.level in self.levelUpMoves:
			if self.levelUpMoves[self.level].isHeal:
				self.add_heal(self.levelUpMoves[self.level], True)
			else:
				self.add_attack(self.levelUpMoves[self.level], True)





class Warrior(Player):

	def __init__(self, name):
		startHP = 25
		startMana = 0
		super().__init__(name, 1, startHP, startMana)
		self.kind = 'Warrior'
		self.add_attack(Attack('Hit', 5, 100, False, 0))
		self.levelUpStats = {'HP' : 5 + int(self.level/2), 'Mana' : 0}
		self.defendModifier = 3


		self.levelUpMoves[3] = Attack('Slash', 8, 90, False, 0)
		self.levelUpMoves[6] = Attack('Stab', 10, 85, False, 0)


	

class Mage(Player):

	def __init__(self, name):
		startHP = 15
		startMana = 10
		super().__init__(name, 1, startHP, startMana)
		self.kind = 'Mage'
		self.add_attack(Attack('Bash', 3, 75, False, 0))
		self.add_attack(Attack('Sparks', 7, 100, True, 3))
		self.levelUpStats = {'HP' : 3 + int(self.level/3), 'Mana' : 3 + int(self.level/3)}
		self.defendModifier = 1.5

		
		self.levelUpMoves[3] = Attack('Flames', 10, 90, True, 5)
		self.levelUpMoves[6] = Attack('Firebolt', 15, 95, True, 8)




class Sage(Player):
	def __init__(self, name):
		startHP = 15
		startMana = 10
		super().__init__(name, 1, startHP, startMana)
		self.kind = 'Sage'
		self.add_attack(Attack('Bash', 3, 75, False, 0))
		self.add_heal(Heal('Heal-1', 5, 95, True, 4))
		self.levelUpStats = {'HP' : 2 + int(self.level/3), 'Mana' : 3 + int(self.level/3)}
		self.defendModifier = 1


		self.levelUpMoves[3] = Heal('Heal-2', 10, 90, True, 6)
		self.levelUpMoves[6] = Attack('Stab', 10, 85, False, 0)




class Berserker(Player):
	def __init__(self, name):
		startHP = 20
		startMana = 0
		super().__init__(name, 1, startHP, startMana)
		self.kind = 'Berserker'
		self.add_attack(Attack('Smash', 7, 85, False, 0))
		self.levelUpStats = {'HP' : 3 + int(self.level/2), 'Mana' : 0}
		self.defendModifier = 2
		self.berserkChance = 20


		self.levelUpMoves[4] = Attack('Slam', 12, 70, False, 0)
		self.levelUpMoves[9] = Attack('Wallop', 20, 85, False, 0)


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
