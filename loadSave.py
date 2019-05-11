# Load and Save characters
from playerClasses import *
from party import Party
from misc import isInt
import os

def save_character(character, saveFile):
	with open(saveFile, 'a') as f:
		f.write('Character:\n')
		f.write('Name:%s\n' % character.name)
		f.write('Level:%i\n' % character.level)
		f.write('HP:%i\n' % character.maxHP)
		f.write('MANA:%i\n' % character.maxMANA)
		f.write('exp:%i\n' % character.exp)
		f.write('TotalEXP:%i\n' % character.totalEXP)
		f.write('Kind:%s\n' % character.kind)
		for name, attack in character.attacks.items():
			f.write('Attack:%s\n' % attack.save())
		if character.heals:
			for name, heal in character.heals.items():
				f.write('Heal:%s\n' % heal.save())

	

def save_party(party):
	print('Saving progress...')
	members = party.get_members()
	saveFile = '.' + party.name + '_partySave.txt'
	gold = party.get_gold()
	gold += party.party_items_value()

	with open(saveFile, 'w') as f:
		f.write('Party:%s\n' % party.name)
		f.write('Gold:%i\n' % gold)
	for member in members:
		save_character(member, saveFile)

	add_to_save_list(party.name)
	print('Progress saved.')

def load_party(partyName):
	saveFile = '.' + partyName + '_partySave.txt'
	members = []
	readCharacter = False
	with open(saveFile) as f:
		for line in f:
			line = line.rstrip()
			if readCharacter:
				if 'Character' in line:
					members.append(load_character(characterInfo))
					characterInfo = []
					continue
				else:
					characterInfo.append(line)
			else:
				if 'Party' in line:
					name = line.split(':')[1]
				if 'Gold' in line:
					gold = int(line.split(':')[1])
				if 'Character' in line:
					readCharacter = True
					characterInfo = []
					continue

	members.append(load_character(characterInfo))

	party = Party(members, name)
	party.add_gold(gold)
	return party

def load_character(characterInfo):
	attacks = []
	heals = []

	for line in characterInfo:
		line = line.rstrip()
		if 'Name' in line:
			name = line.split(':')[1]
		if 'Level' in line:
			level = int(line.split(':')[1])
		if 'HP' in line:
			hp = int(line.split(':')[1])
		if 'MANA' in line:
			mana = int(line.split(':')[1])
		if 'exp' in line:
			exp = int(line.split(':')[1])
		if 'TotalEXP' in line:
			totalEXP = int(line.split(':')[1])
		if 'Kind' in line:
			kind = line.split(':')[1]
		if 'Attack' in line:
			attacks.append(line.split(':')[1])
		if 'Heal' in line:
			heals.append(line.split(':')[1])

	if kind == 'Mage':
		character = Mage(name)
	elif kind == 'Warrior':
		character = Warrior(name)
	elif kind == 'Sage':
		character = Sage(name)
	elif kind == 'Berserker':
		character = Berserker(name)

	character.load_character(level, hp, mana, exp, totalEXP, attacks, heals)
	return character
	

def add_to_save_list(name):
	listFile = '.saveList.txt'
	saves = [name]
	if os.path.isfile(listFile):
		with open(listFile) as f:
			for line in f:
				saves.append(line.rstrip())
		saves = list(set(saves))
		f.close()

	with open(listFile, 'w') as f:
		for save in saves:
			f.write('%s\n' % save)
		f.close()

def choose_save():
	listFile = '.saveList.txt'
	saves = []

	if not os.path.isfile(listFile):
		input('No saves found, creating new save.')
		return new_party()
	with open(listFile) as f:
		for line in f:
			saves.append(line.rstrip())
		f.close()
	print('------------- Saves -----------------------------------')
	for i in range(len(saves)):
		print('[%i] %s' % (i, saves[i]))

	saveNum = -1
	while saveNum not in range(len(saves)):
		stream = input('Load save number: ').rstrip()
		if isInt(stream):
			saveNum = int(stream)

	return load_party(saves[saveNum])

def new_or_load():
	choice = ''
	while choice not in ['load','new']:
		choice = input('Load save or start a new game? [Load/New]\n').rstrip().lower()

	if choice == 'load':
		return choose_save()
	if choice == 'new':
		return new_party()

def new_character():
	
	for i in range(len(classes)):
		print('[%i] %s' % (i, classes[i]))
	selection = -1	
	while selection not in range(len(classes)):
		stream = input('Choose number of class: ').rstrip().lower().title()
		if isInt(stream):
			selection = int(stream)

	choice = classes[selection]
	name = input('Name your %s: ' % choice)

	if choice == 'Warrior':
		return Warrior(name)
	if choice == 'Mage':
		return Mage(name)
	if choice == 'Sage':
		return Sage(name)
	if choice == 'Berserker':
		return Berserker(name)

def new_party():
	members = []
	partyName = input('Name your party: ')
	while len(members) < 3:
		print('Player %i class:' % (len(members)+1) )
		members.append(new_character())

	return Party(members, partyName)