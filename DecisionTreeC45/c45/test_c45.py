#!/usr/bin/env python
import unittest
from c45 import C45

class testC45Methods(unittest.TestCase):
	c1 = C45("DecisionTreeC45/data/iris/iris.data", "DecisionTreeC45/data/iris/iris.names")

	def testFoo(self):
		self.assertEqual(True, True)


def main():
	unittest.main()

if __name__ == '__main__':
	main()

