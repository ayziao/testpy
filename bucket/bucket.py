from pprint import pprint


def hoge():
	return 'piyo'


if __name__ == '__main__':
	pprint(globals())

	import sys
	from pprint import pprint

	a = {}
	a['a'] = 2
	m = a.get('b')
	n = None
	pprint(a)
	pprint(globals())
	# pprint(locals())

	pprint(dir())

	pprint(sys.path)
