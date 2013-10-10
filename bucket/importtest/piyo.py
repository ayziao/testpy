# import hoge
#import myapp.common.Utility
#print(myapp.common.Utility.config)


__status_code = None


@property
def status_code():
	return __status_code


@status_code.setter
def status_code(val):
	global __status_code
	__status_code = val
