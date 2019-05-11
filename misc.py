# misc functions

def isInt(num):
	try:
		int(num)
		return True
	except ValueError:
		return False