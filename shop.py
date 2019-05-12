# shop function

from item import *
from misc import isInt
class Shop:

	def __init__(self, items):
		self.items = items


	def use_shop(self, party):
		print()
		print('------------- Welcome to Shoppe\'s shop ---------------')
		leave = False
		while leave == False:
			self.items = self.update_items()
			buy, leave = self.buy_or_sell()
			if buy:
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
		if len(self.items) == 0:
			input('Shop has no items for sale.')
			return

		print('------------- Shop items ------------------------------')
		for i in range(len(self.items)):
			print('[%i] %s' % (i, self.items[i].shop_list()))

		print()
		print('Party has %i gold' % party.party_gold())
		selection = -1
		while selection not in range(len(self.items)):
			stream = input('Choose item number to buy: ').rstrip()
			if isInt(stream):
				selection = int(stream)
		item = self.items[selection]

		num = -1
		# plus one because human vs computer counting
		while num not in range(item.num + 1):
			stream = input('Buy how many? ').rstrip()
			if isInt(stream):
				num = int(stream)
		
		buyItem = item.copy(num)
		buyItem.set_num(num)
		if party.get_gold() >= buyItem.total_value():
			party.buy_item(buyItem)
			self.items[selection].shop_sell(num)
		else:
			input('Not enough gold to buy.')


	def sell_items(self, party):
		if len(party.inventory) == 0:
			input('Party has no items to sell.')
			return

		items = list(party.inventory.keys())
		print('------------- Party items -----------------------------')
		for i in range(len(items)):
			print('[%i] %s' % (i, party.inventory[items[i]]))
			selection = -1
		while selection not in range(len(items)):
			stream = input('Choose item number to sell: ').rstrip()
			if isInt(stream):
				selection = int(stream)
		sellItem = party.inventory[items[selection]]

		num = -1
		while num not in range(sellItem.num + 1):
			stream = input('Sell how many? ').rstrip()
			if isInt(stream):
				num = int(stream)
		party.sell_item(sellItem, num)
		
	def update_items(self):
		items = []
		for item in self.items:
			if item.num == 0:
				continue
			else:
				items.append(item)

		return items