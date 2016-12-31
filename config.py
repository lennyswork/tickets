#!/usr/bin/env python3

# 读取配置文件
from configparser import ConfigParser

class Config(object):
	"""加载配置文件"""
	def __init__(self):
		self.config = self.read('config.ini')


	def read(self, filenames):
		cfg = ConfigParser()
		cfg.read(filenames)
		return cfg



if __name__ == '__main__':
	config = Config().config
	print(config.get('url','simple_sample_url'))
	



