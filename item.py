# Item class

class Item:

	def __init__(self, name, isEquippable, num=1):
		self.name = name
		self.isEquippable = isEquippable
		self.isBattleItem = False
		self.num = num
		self.value = 0

	def __str__(self):
		return '%s x%i' % (self.name, self.num)

	def sell(self):
		self.num -= 1
		return int(self.value * 0.8)

	def sell_all(self):
		tot = self.num
		self.num = 0
		return int(self.value * tot * 0.8)

	def gold_for_save(self):
		return self.value * self.num


class Campfire(Item):
	# Heals living party members
	def __init__(self, num=1):
		super().__init__('Campfire', False, num)
		self.value = 10

	def use(self, party):
		self.num -= 1
		party.heal_party()

class Cabin(Item):
	# Heals and revives party
	def __init__(self, num=1):
		super().__init__('Cabin', False, num)
		self.value = 30

	def use(self, party):
		self.num -= 1
		party.heal_and_revive_party()	


class BattleItem(Item):

	def __init__(self, name, power, num=1):
		super().__init__(name, False, num)
		self.isBattleItem = True
		self.isFriendly = False
		self.power = power

	def __str__(self):
		return '%s x%i' % (self.name, self.num)


class Potion(BattleItem):
	# Restores some % of hp, increments of 20%
	# Power between 1-5
	def __init__(self, power, num=1):
		name = 'Potion-%i' % power
		super().__init__(name, power, num)
		self.isFriendly = True
		self.value = 5 * power**2

	def use(self, target):
		self.num -= 1
		target.restore_hp(int(self.power * target.maxHP / 5))

class Ether(BattleItem):
	# Restores some % of mana, increments of 20%
	# Power between 1-5
	def __init__(self, power, num=1):
		name = 'Ether-%i' % power
		super().__init__(name, power, num)
		self.isFriendly = True
		self.value = 5 * power**2

	def use(self, target):
		self.num -= 1
		target.restore_mana(int(self.power * target.maxHP / 5))

class Elixir(BattleItem):
	# Restores some % of hp & mana, increments of 20%
	# Power between 1-5
	def __init__(self, power, num=1):
		name = 'Elixir-%i' % power
		super().__init__(name, power, num)
		self.isFriendly = True
		self.value = 10 * power**2

	def use(self, target):
		self.num -= 1
		target.restore_hp(int(self.power * target.maxHP / 5))
		target.restore_mana(int(self.power * target.maxHP / 5))


class Spear(BattleItem):
	# Power between 1-5
	def __init__(self, power, num=1):
		names = {1 : 'Flint', 2 : 'Copper', 3 : 'Bronze', 4 : 'Iron', 5 : 'Steel'}
		name = '%s spear' % names[power]
		super().__init__(name, power, num)
		self.value = 7 * power**2

	def use(self, target):
		self.num -= 1
		damage = self.power*15
		input('%s stuck in %s!' % (self.name, target.name))
		target.take_damage(damage)


