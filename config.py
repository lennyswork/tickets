from configparser import ConfigParser

class Config(object):
	"""read the config"""
	def __init__(self, arg):
		super(Config, self).__init__()
		self.arg = arg
