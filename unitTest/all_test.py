import unittest
import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path.rstrip('/unitTest'))

import unitTest.test_main
import unitTest.common.test_application

aaa = unitTest.test_main.TestMyapp
bbb = unitTest.common.test_application.TestApplication

unittest.main()

#unittest.main()