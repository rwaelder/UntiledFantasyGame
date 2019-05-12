# Party battle
from misc import isInt
from random import choice

def new_turn(playerParty, enemyParty):
	playerParty.reset_actions()
	enemyParty.reset_actions()


def print_turn(playerParty, enemyParty):
	print('\n\n')
	print('------------- Enemy Party -----------------------------')
	print(enemyParty)
	print('\n')
	print('------------- Player Party ----------------------------')
	print(playerParty)
	print('\n')


def get_players_target(user, targetParty):
	party = targetParty.get_alive_members()
	defendingPlayers = targetParty.get_defending_members()
	if defendingPlayers:
		party = defendingPlayers
	print()
	for i in range(len(party)):
		print('[%i] %s' % (i, party[i]))
	target = -1
	while target not in range(len(party)):
		stream = input('Choose target number for %s: ' % user.name).rstrip()
		if isInt(stream):
			target = int(stream)
	print()
	return party[target]

def get_heal_target(user, targetParty):
	party = targetParty.get_members()

	print()
	for i in range(len(party)):
		print('[%i] %s' % (i, party[i]))
	target = -1
	while target not in range(len(party)):
		stream = input('Choose target number for %s: ' % user.name).rstrip()
		if isInt(stream):
			target = int(stream)
	print()
	return party[target]

def get_item_target(user, targetParty):
	print()
	for i in range(len(targetParty)):
		print('[%i] %s' % (i, targetParty[i]))
	target = -1
	while target not in range(len(targetParty)):
		stream = input('Choose target number for %s: ' % user.name).rstrip()
		if isInt(stream):
			target = int(stream)
	print()
	return targetParty[target]

def get_enemys_target(targetParty):
	defendingPlayers = targetParty.get_defending_members()
	if defendingPlayers:
		return choice(defendingPlayers)
	return choice(targetParty.get_alive_members())

def do_attack(user, targetParty):
	attack = user.choose_attack()
	damage, text = attack.use_attack(user)
	if user.is_player():
		target = get_players_target(user, targetParty)
	else:
		target = get_enemys_target(targetParty)
	input('%s %s %s!' % (user.name, text, target.name))
	
	target.take_damage(damage)

def do_heal(user, targetParty):
	heal = user.choose_heal()
	healPower, text = heal.use_heal(user)
	if user.is_player():
		target = get_heal_target(user, targetParty)
	else:
		target = get_enemys_target(targetParty)
	input('%s %s %s!' % (user.name, text, target.name))
	
	target.restore_hp(healPower)

def start_move(user, targetParty, teamParty):
	if user.isDead:
		return 0
	else:
		print()
		if user.action == 'heal':
			do_heal(user, teamParty)
		else:
			do_attack(user, targetParty)
		
def do_item_use(user, teamParty, targetParty):
	if user.isDead:
		return
	elif teamParty.has_battle_items():
		item = teamParty.choose_battle_item(user)
	else:
		print('\n%s has no usable items for %s!' % (teamParty.name, user.name))
		do_nothing(user)
		return
	if item.isFriendly:
		teamParty.use_item(user, item, get_item_target(user, teamParty.get_members()))
	else:
		teamParty.use_item(user, item, get_players_target(user, targetParty))

def do_defend(user):
	if user.isDead:
		return 
	user.defend()
	input('\n%s is now defending!' % user.name)

def do_nothing(user):
	if user.isDead:
		return
	input('\n%s is doing nothing!' % user.name)


def battle(playerParty, enemyParty):

	while playerParty.party_hp() > 0 and enemyParty.party_hp() > 0:
		new_turn(playerParty, enemyParty)
		print_turn(playerParty, enemyParty)

		playerParty.choose_actions()
		enemyParty.choose_actions()


		for player in playerParty.get_defending_members():
			do_defend(player)

		for enemy in enemyParty.get_defending_members():
			do_defend(enemy)

		for player in playerParty.get_members():
			if player.action == 'item':
				do_item_use(player, playerParty, enemyParty)
			if player.action in ['attack', 'heal']:
				start_move(player, enemyParty, playerParty)
				if enemyParty.party_hp() == 0:
					break
			if player.action == 'nothing':
				do_nothing(player)

		if enemyParty.party_hp() == 0:
			break
		for enemy in enemyParty.get_members():
			if enemy.action in ['attack', 'heal']:
				start_move(enemy, playerParty, enemyParty)
				if playerParty.party_hp() == 0:
					break
			if enemy.action == 'nothing':
				do_nothing(enemy)

	if enemyParty.party_hp() == 0:
		print()
		exp = enemyParty.party_exp()	
		gold = enemyParty.party_gold()	
		print('%s party defeated %s party! You win!' % (playerParty.name, enemyParty.name))
		input('%s party gained %i exp points!' % (playerParty.name, exp))
		input('%s party got %i gold!' % (playerParty.name, gold))

		for player in playerParty.get_members():
			player.gain_exp(int(exp/len(playerParty.get_members())))

		playerParty.add_gold(gold)

		won = True
	elif playerParty.party_hp() == 0:
		print()
		input('%s party defeated by %s party! You lose!' % (playerParty.name, enemyParty.name))
		won = False
	playerParty.end_battle()

	return won