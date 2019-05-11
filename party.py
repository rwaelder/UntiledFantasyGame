# Party class

from playerClasses import Player
from enemies import Enemy
from misc import isInt

class Party:

	def __init__(self, members, name=''):
		self.members = []

		if type(members) is list:
			for member in members:
				self.members.append(member)
		else:
			self.members.append(members)

		if name:
			self.name = name
		else:
			self.name = self.members[0].name

		self.gold = 0
		for member in members:
			self.gold += member.gold

		self.inventory = {}

	def __str__(self):
		string = ''
		for member in self.members:
			string += '%s\n' % member
		return string

	def as_list(self):
		return self.members

	def get_members(self):
		return self.members

	def names(self):
		names = []
		for member in self.members:
			names.append(member.name)
		return names

	def add_member(self, member):
		self.members.append(member)

	def remove_member_by_number(self, memberNumber, ret=False):
		member = self.members[memberNumber]
		del self.members[memberNumber]
		if ret:
			return member

	def remove_member_by_name(self, memberName, ret=False):
		for i in range(len(self.members)):
			if self.members[i].name == memberName:
				member = self.members[i]
				del self.members[i]
				if ret:
					return member

	def heal_party(self):
		for member in self.get_alive_members():
			member.full_hp()
			member.full_mana()

	def heal_and_revive_party(self):
		for member in self.members:
			member.full_hp()
			member.full_mana()

	def choose_actions(self):
		for member in self.members:
			member.choose_action(self)

	def party_hp(self):
		hp = 0
		for member in self.members:
			hp += member.get_hp()
		return hp

	def party_exp(self):
		exp = 0
		for member in self.members:
			exp += member.get_exp()
		return exp

	def party_gold(self):
		return self.gold

	def get_gold(self):
		return self.gold

	def add_gold(self, amount):
		self.gold += amount

	def spend_gold(self, amount):
		self.gold -= amount

	def party_items_value(self):
		value = 0
		for item in self.inventory.keys():
			value += self.inventory[item].gold_for_save()
		return value

	def reset_actions(self):
		for member in self.members:
			member.reset()

	def end_battle(self):
		for member in self.members:
			member.end_battle_reset()

	def get_actions(self):
		actions = []
		for member in self.get_alive_members():
			actions.append(member.action)
		return self.members, actions

	def get_defending_members(self):
		defendingMembers = []
		for member in self.members:
			if member.action == 'defend' and not member.isDead:
				defendingMembers.append(member)
		return defendingMembers

	def get_alive_members(self):
		aliveMembers = []
		for member in self.members:
			if not member.isDead:
				aliveMembers.append(member)
		return aliveMembers


	def add_item(self, item):
		input('%s got a(n) %s' % (self.name, item))
		if item.name in self.inventory:
			self.inventory[item.name].num += 1
		else:
			self.inventory[item.name] = item

	def use_item(self, user, item, target):
		input('%s used %s!' % (user.name, item.name))
		item.use(target)
		if item.num == 0:
			del self.inventory[item.name]

	def has_battle_items(self):
		for itmName, item in self.inventory.items():
			if item.isBattleItem:
				return True
		return False

	def choose_battle_item(self, user):
		print('------------- Items -----------------------------------')
		itms = list(self.inventory.keys())
		for i in range(len(itms)):
			if self.inventory[itms[i]].isBattleItem:
				print('[%i] %s' % (i, self.inventory[itms[i]]))
		selection = -1
		while selection not in range(len(itms)):
			stream = input('Choose item number for %s: ' % user.name).rstrip()
			if isInt(stream):
				selection = int(stream)
		return self.inventory[itms[selection]]

	def get_level(self):
		return self.members[1].level

