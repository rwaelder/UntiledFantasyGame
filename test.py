from random import randint

class Attack:

	def __init__(self, name, damage, accuracy, isMagic, manaCost):
		self.name = name
		self.damage = damage
		self.accuracy = accuracy
		self.isMagic = isMagic
		self.manaCost = manaCost

class Creature:

	def __init__(self, name, level, hp, mana):
		self.name = name
		self.level = level
		self.maxHP = hp
		self.hp = hp
		self.maxMANA = mana
		self.mana = mana
		self.exp = 0
		self.isDefending = False
	

	def take_damage(self, damage):
		if self.hp - damage < 0:
			self.hp = 0
		else:
			self.hp -= damage

	def HP(self):
		return 'HP: %i/%i' % (self.hp, self.maxHP)

	def MANA(self):
		return 'Mana: %i/%i' % (self.mana, self.maxMANA)

	def defend(self):
		self.isDefending = True

	def stop_defend(self):
		self.isDefending = False

	def __str__(self):
		return '%s lv. %i' % (self.name, self.level)


class Warrior(Creature):

	def __init__(self, name):
		startHP = 25
		startMana = 0
		super().__init__(name, 1, startHP, startMana)
		self.attack = Attack('Hit', 5, 100, False, 0)

	def use_attack(self):
		chance = randint(1,100)
		input('%s used %s!' % (self.name, self.attack.name))
		if chance > self.attack.accuracy:
			return 0, 'missed'
		elif chance == self.attack.accuracy:
			return int(self.attack.damage / 2), 'grazed'
		else:
			return self.attack.damage, 'hit'

class Orc(Creature):

	def __init__(self, level):
		hp, attackDamage, exp = Orc.set_stats(level)
		super().__init__('Orc', level, hp, 0)
		self.attack = Attack('Bash', attackDamage, 90, False, 0)
		self.exp = exp


	def set_stats(level):
		hp = 15 + 4*level
		attackDamage = 6 + level
		exp = 10 + 4*level
		return hp, attackDamage, exp

	def use_attack(self):
		chance = randint(1,100)
		input('%s used %s!' % (self.name, self.attack.name))
		if chance > self.attack.accuracy:
			return 0, 'missed'
		elif chance == self.attack.accuracy:
			return int(self.attack.damage / 2), 'grazed'
		else:
			return self.attack.damage, 'hit'

	def get_action(self):
		chance = randint(1,100)
		if chance <= 80:
			return 'attack'
		else:
			return 'nothing'

def new_turn(players):
	for player in players:
		player.stop_defend()

def print_turn(player, enemy):
	print('\n\n')
	print('\t %s \t %s' % (player, enemy))
	print('\t %s \t %s' % (player.HP(), enemy.HP()))
	print('\t %s \t %s' % (player.MANA(), enemy.MANA()))
	print('\n')

def get_player_action():
	action = ''
	while action not in ['attack', 'defend', 'nothing']:
		action = input('Choose action [Attack, Defend, Nothing]\n').lower()
	return action

def do_attack(user, target):
	damage, text = user.use_attack()
	input('%s %s %s!' % (user.name, text, target.name))
	if target.isDefending:
		input('%s is defending!' % target.name)
		damage = int(damage / 2)
	target.take_damage(damage)

def do_defend(user):
	user.defend()
	input('%s is now defending!' % user.name)

def do_nothing(user):
	input('%s is doing nothing!' % user.name)

def battle(player, enemy):
	while player.hp > 0 and enemy.hp > 0:
		new_turn([player, enemy])
		print_turn(player, enemy)
		playerAction = get_player_action()
		enemyAction = enemy.get_action()

		if 'defend' in [playerAction, enemyAction]:
			if playerAction == 'defend':
				do_defend(player)
			if enemyAction == 'defend':
				do_defend(enemy)
		if playerAction == 'attack':
			do_attack(player, enemy)
			if enemy.hp == 0:
				break
		if playerAction == 'nothing':
			do_nothing(player)

		if enemyAction == 'attack':
			do_attack(enemy, player)
		if enemyAction == 'nothing':
			do_nothing(enemy)

	if enemy.hp == 0:
		input('%s defeated %s! You win!' % (player.name, enemy.name))

	elif player.hp == 0:
		input('%s defeated by %s! You lose!' % (player.name, enemy.name))

player = Warrior('Jeff')

enemy = Orc(1)

battle(player, enemy)















