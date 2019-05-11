# campaigns
import orcHideout
from misc import isInt


def choose_campaign(party):
	campaigns = ['Orc Hideout']
	print()
	print('------------- Campaigns -------------------------------')
	for i in range(len(campaigns)):
		print('[%i] %s' % (i, campaigns[i]))

	choice = -1
	while choice not in range(len(campaigns)):
		stream = input('Choose campaign number: ').rstrip()
		if isInt(stream):
			choice = int(stream)

	campaign = campaigns[choice]

	if campaign == 'Orc Hideout':
		orc_hideout(party)


def orc_hideout(party):
	orcHideout.play(party)