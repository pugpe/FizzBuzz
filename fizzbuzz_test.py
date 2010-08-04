# -*- encoding:utf-8 -*-

import unittest
import doctest
from fizzbuzz import FizzBuzz
from pprint import pprint as pp


class FizzBuzzTest(unittest.TestCase):
	def testTres(self):
		self.assertEqual(FizzBuzz(3), 'Fizz')
	def testCinco(self):
		self.assertEqual(FizzBuzz(5), 'Buzz')
	def testSeis(self):
		self.assertEqual(FizzBuzz(6), 'Fizz')
	def testDez(self):
		self.assertEqual(FizzBuzz(10), 'Buzz')
	def testUm(self):
		self.assertEqual(FizzBuzz(1),1)
	def testQuatro(self):
		self.assertEqual(FizzBuzz(4),4)
	def testQuinze(self):
		self.assertEqual(FizzBuzz(15),'FizzBuzz')	 	
	def testTrinta(self):
		self.assertEqual(FizzBuzz(30),'FizzBuzz')
	def testQuinzePontoCinco(self):
		self.assertEqual(FizzBuzz(15.5),15.5)
	def testString(self):
		self.assertRaises(TypeError, FizzBuzz, 'teste')
def main():
	unittest.main()




if __name__ == '__main__':
	main()
	doctest.testmod()