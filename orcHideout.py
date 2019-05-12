# Orc Hideout
from partyBattle import battle
from enemies import Orc, OrcShaman, OrcPeon, OrcBerserker, OrcLeader
from item import Potion, Ether, Spear
from random import choice
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


def play(playerParty):

	print('\n\n')
	print('--------------------------------------------------------------')
	print('------------------------- Welcome to -------------------------')
	print('--------------------------------------------------------------')
	print('--------------------------------------------------------------')
	print('------------------------- Orc Cavern -------------------------')
	print('--------------------------------------------------------------')
	input('\n\n')

	input('You find a couple items on the ground because story')

	playerParty.add_item(Potion(1, 2))
	playerParty.add_item(Ether(1, 2))

	input('You made too much noise collecting your items, now kill these guards.')
	enemies = []
	enemies.append(OrcPeon(set_enemy_level(playerParty)))
	enemies.append(OrcPeon(set_enemy_level(playerParty)))
	enemyParty = Party(enemies)
	won = battle(playerParty, enemyParty)

	if not won:
		game_over()
		return

	input('Oh no, reinforcements!')

	enemies = []
	enemies.append(OrcPeon(set_enemy_level(playerParty)))
	enemies.append(OrcPeon(set_enemy_level(playerParty)))
	enemies.append(Orc(set_enemy_level(playerParty)))
	enemyParty = Party(enemies)
	won = battle(playerParty, enemyParty)

	if not won:
		game_over()
		return

	input('You WILL lose this fight.')


	enemies = []
	enemies.append(OrcBerserker(50))
	enemyParty = Party(enemies)
	won = battle(playerParty, enemyParty)

	if not won:
		print()
		print('Despite getting the whalloping of your lives, you')
		input('manage to get out of there and meet a traveling salesman.')
		shopItems = []
		shopItems.append(Potion(2, 4))
		shopItems.append(Ether(2, 4))
		shopItems.append(Spear(2, 4))
		shop = Shop(shopItems)
		shop.use_shop(playerParty)
		play(playerParty)
		print('After buying items from his shop, the salesman')
		print('sets up his camp and allows you to stay the')
		print('night with him. Refreshed, you head back to the')
		input('orc hideout the following morning.')
		playerParty.heal_and_revive_party()
		
	else:
		input('Good job, you win I guess')








































