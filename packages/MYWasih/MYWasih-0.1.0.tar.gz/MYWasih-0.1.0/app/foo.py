import termcolor
class duck(object):
	mins = 0
	sec = 0
	def __init__(self, mins, sec):
		self.mins = mins
		self.sec = sec

def print_hello():
	D = duck(0,0)
	print "Hello!!!!\n"
