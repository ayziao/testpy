#mac用
/Library/Frameworks/Python.framework/Versions/3.3/bin/coverage -e
/Library/Frameworks/Python.framework/Versions/3.3/bin/coverage run --source=myapp tests/all_test.py
/Library/Frameworks/Python.framework/Versions/3.3/bin/coverage report -m
/Library/Frameworks/Python.framework/Versions/3.3/bin/coverage html
