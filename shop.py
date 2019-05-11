# shop function

from item import *
from misc import isInt
class Shop:

	def __init__(self, items):
		self.items = items


	def use_shop(self, party):
		print('------------- Welcome to Shoppe\'s shop ---------------')
		buy, leave = self.buy_or_sell()
		if leave:
			return
		elif buy:
			self.buy_items(party)
		else:
			self.sell_items(party)


	def buy_or_sell(self):
		options = ['buy','sell']
		action = ''
		buy = False
		leave = False
		while action not in options:
			action = input('Buy or sell items or leave? [Buy, Sell, Leave]\n').rstrip().lower()
		if action == 'buy':
			buy = True
		elif action == 'sell':
			buy = False
		elif action == 'leave':
			leave = True
		return buy, leave

	def buy_items(self, party):
		print('------------- Shop items ------------------------------')
		for i in range(len(self.items)):
			print('[%i] %s' % (i, self.items[i]))
			selection = -1
		while selection not in range(len(self.items)):
			stream = input('Choose item number to buy: ').rstrip()
			if isInt(stream):
				selection = int(stream)


