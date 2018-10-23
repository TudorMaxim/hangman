'''
Created on 30 ian. 2018

@author: Asus
'''
import test_repository
import test_controller
import unittest

all_suites = unittest.TestSuite([test_repository.suite(), test_controller.suite()])

test = unittest.TextTestRunner()
test.run(all_suites)