# Battle functions
from random import randint

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
		action = input('Choose action [Attack, Defend, Nothing]\n').lower().rstrip()
	return action

def do_attack(user, target):
	damage, text = user.choose_attack()
	input('%s %s %s!' % (user.name, text, target.name))
	if target.isDefending:
		input('%s is defending!' % target.name)
		damage = int(damage / 2)
	target.take_damage(damage)

def do_defend(user):
	user.defend()
	input('\n%s is now defending!' % user.name)

def do_nothing(user):
	input('\n%s is doing nothing!' % user.name)

# Main battle

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
		print('%s defeated %s! You win!' % (player.name, enemy.name))
		input('%s gained %i exp points!' % (player.name, enemy.get_exp()))
		player.gain_exp(enemy.get_exp())

	elif player.hp == 0:
		input('%s defeated by %s! You lose!' % (player.name, enemy.name))