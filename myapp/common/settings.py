"""
# myapp.common.settings
"""

from configparser import ConfigParser
from datetime import datetime

config_path = '../config/'
ini = None
environ = None
start_time = datetime.utcnow()


def get_ini(section=None):
	global ini
	if ini is None:
		ini = ConfigParser()
		ini.read(config_path + 'setting.ini')
	if section is None:
		return ini
	else:
		return ini[section]
