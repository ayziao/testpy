"""
テスト
"""
# import hoge
#import myapp.common.Utility
#print(myapp.common.Utility.config)


__status_code = None


@property
def status_code():
	"""
	test
	@return:
	"""
	return __status_code


@status_code.setter
def status_code(val):
	"""
	test
	@param val:
	@return:
	"""
	global __status_code
	__status_code = val
