# Orc Hideout
from partyBattle import battle
from enemies import Orc, OrcShaman, OrcPeon, OrcBerserker, OrcLeader
from item import Potion, Ether, Spear
from random import choice
from party import Party

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
		game_over()
		return







































