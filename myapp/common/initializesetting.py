# initializesetting

import configparser

config_path = '../config/'
conf = {}


def set_path(str):
	global config_path
	config_path = str
	_load_conf()


def _load_conf():
	global conf
	if conf:
		return conf
	else:
		conf = configparser.ConfigParser()
		conf.read(config_path + 'setting.ini')
		return conf


def get_ini(section):
	if section:
		return _load_conf()[section]
	else:
		return _load_conf()
