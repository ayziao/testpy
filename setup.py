import os
import sys


path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

from myapp.common import settings

settings.set_config_path(path + '/config/')
settings.setting_encode()

from setuptools.command.test import test as TestCommand
from setuptools import setup


class PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True

	def run_tests(self):
		import pytest

		errno = pytest.main(self.test_args)
		sys.exit(errno)


setup(
	name='myapp',
	packages=['myapp'],
	entry_points={
	'console_scripts': [
		'coveralls = myapp.main:main',
	],
	},
	tests_require=['mock', 'pytest'],
	cmdclass={'test': PyTest},
)


