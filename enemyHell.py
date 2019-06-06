# Enemy Hell
from partyBattle import battle
from enemies import Orc, OrcShaman, OrcPeon, OrcBerserker, OrcLeader, Goblin
from item import Potion, Ether, Spear
from random import choice, randint
from party import Party
from shop import Shop


def set_enemy_level(party, gauntletNum):
	level = party.get_level()
	lowerLim = level - 1 + (gauntletNum - 1)
	upperLim = level + gauntletNum + 1
	if level == 1:
		return 1
	else:
		level = choice(range(lowerLim, upperLim))
		if level == 0:
			level += 1
		return level

def game_over(roundNum):
	input('Your party died. You survived %i rounds.' % roundNum)

def make_party(party, gauntletNum):
	numEnemies = randint(1, 4)
	enemies = []

	for i in range(numEnemies):
		level = set_enemy_level(party, gauntletNum)
		chance = randint(1,100)
		if chance <= 5:
			enemies.append(OrcLeader(level))
		elif chance <= 15:
			enemies.append(OrcShaman(level))
		elif chance <= 25:
			enemies.append(OrcBerserker(level))
		elif chance <= 50:
			enemies.append(Orc(level))
		elif chance <= 75:
			enemies.append(Goblin(level))
		else:
			enemies.append(OrcPeon(level))

	return Party(enemies)

def make_shop(gauntletNum):
	if gauntletNum <= 5:
		itemLevel = 5
	else:
		itemLevel = gauntletNum + 1

	shopItems = []
	shopItems.append(Potion(itemLevel, randint(2,5)))
	shopItems.append(Ether(itemLevel, randint(2,5)))
	shopItems.append(Spear(itemLevel, randint(1,6)))

	shop = Shop(shopItems)

	return shop



def play(party):


	print('\n\n')
	print('--------------------------------------------------------------')
	print('--------------------------------------------------------------')
	print('------------------------- Welcome to -------------------------')
	print('--------------------------------------------------------------')
	print('------------------------- Enemy Hell -------------------------')
	print('--------------------------------------------------------------')
	input('\n\n')

	gauntletNum = 1
	roundNum = 1

	won = battle(party, make_party(party, gauntletNum))

	while won:

		roundNum += 1
		if roundNum % 5 == 0:
			gauntletNum += 1
			input('Enemies now stronger!')
			party.heal_and_revive_party()
			input('Party healed!')

		if roundNum % 10 == 0:
			shop = make_shop(gauntletNum)
			shop.use_shop(party)


		won = battle(party, make_party(party, gauntletNum))

	game_over(roundNum)
