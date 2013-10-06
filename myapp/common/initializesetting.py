"""
# myapp.common.initializesetting
"""

import configparser

config_path = '../config/'
conf = None


def set_config_directory(str_):
	global config_path
	config_path = str_


def get_ini(section=None):
	global conf
	if conf is None:
		conf = configparser.ConfigParser()
		conf.read(config_path + 'setting.ini')
	if section is None:
		return conf
	else:
		return conf[section]
