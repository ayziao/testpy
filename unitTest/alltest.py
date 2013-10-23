import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

import test_main

test_main.unittest.main()

#unittest.main()