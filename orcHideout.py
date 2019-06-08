# Orc Hideout
from partyBattle import battle
from enemies import Orc, OrcShaman, OrcPeon, OrcBerserker, OrcLeader
from item import Potion, Ether, Spear
from random import choice, randint
from party import Party
from shop import Shop

def set_enemy_level(party):
	level = party.get_level()
	if level == 1:
		return 1
	else:
		level = choice([level-1, level, level+1])
		if level == 0:
			level += 1
		return level


def game_over():
	input('Quest failed. Game over.')


def fight_orc_peons(playerParty, numEnemies=2):
	enemies = []
	
	for i in range(numEnemies):
		level = set_enemy_level(playerParty)
		enemies.append(OrcPeon(level))

	enemyParty = Party(enemies)
	won = battle(playerParty, enemyParty)

	return won

def fight_orc_squad(playerParty, numEnemies=3):
	enemies = []
	

	for i in range(numEnemies):
		level = set_enemy_level(playerParty)
		chance = randint(1, 100)
		if chance <= 2:
			enemies.append(OrcLeader(level))
		elif chance <= 10:
			enemies.append(OrcShaman(level))
		elif chance <= 20:
			enemies.append(OrcBerserker(level))
		elif chance <= 40:
			enemies.append(Orc(level))
		else:
			enemies.append(OrcPeon(level))

	enemyParty = Party(enemies)
	won = battle(playerParty, enemyParty)

	return won

def boss_fight(playerParty):
	enemies = []

	enemies.append(OrcLeader(set_enemy_level(playerParty)+3))
	enemies.append(OrcShaman(set_enemy_level(playerParty)+2))
	enemies.append(Orc(set_enemy_level(playerParty)))
	enemies.append(Orc(set_enemy_level(playerParty)))

	enemyParty = Party(enemies)
	won = battle(playerParty, enemyParty)

	return won

def play(playerParty, first=True):

	if first:
		print('\n\n')
		print('--------------------------------------------------------------')
		print('--------------------------------------------------------------')
		print('------------------------- Welcome to -------------------------')
		print('--------------------------------------------------------------')
		print('------------------------- Orc Cavern -------------------------')
		print('--------------------------------------------------------------')
		input('\n\n')

	input('You find a couple items on the ground because story')

	playerParty.add_item(Potion(1, 2))
	playerParty.add_item(Ether(1, 2))

	input('You made too much noise collecting your items, now kill these guards.')
	
	won = fight_orc_peons(playerParty)
	if not won:
		game_over()
		return

	input('Oh no, reinforcements!')

	
	won = fight_orc_squad(playerParty)
	if not won:
		game_over()
		return

	input('You WILL lose this fight.')


	won = boss_fight(playerParty)
	attempt = 0

	if won:
		input('Good job, you win I guess')
	elif attempt < 2:
		attempt += 1
		print()
		print('Despite getting the whalloping of your lives, you')
		input('manage to get out of there and meet a traveling salesman.')
		shopItems = []
		shopItems.append(Potion(2, 4))
		shopItems.append(Ether(2, 4))
		shopItems.append(Spear(2, 4))
		shop = Shop(shopItems)
		shop.use_shop(playerParty)
		
		print('After buying items from his shop, the salesman')
		print('sets up his camp and allows you to stay the')
		print('night with him. Refreshed, you head back to the')
		input('orc hideout the following morning.')
		playerParty.heal_and_revive_party()
		play(playerParty, False)
	else:
		game_over()
		return
		
	








































