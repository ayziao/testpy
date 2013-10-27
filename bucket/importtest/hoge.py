"""
テスト
"""
print('hoge')

import myapp.common.Utility

myapp.common.Utility.pppp()

myapp.common.Utility.config = 1

print(myapp.common.Utility.config)
print(myapp.common.Utility.__config2)