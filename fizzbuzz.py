
import sys

def FizzBuzz(valor):
	'''Retorna Fizz para multiplos de 3, Buzz para multiplos de 5
	e FizzBuzz para multiplos de 3 e 5
	>>> FizzBuzz(1)
	1
	>>> FizzBuzz(6)
	'Fizz'
	>>> FizzBuzz(10)
	'Buzz'
	>>> FizzBuzz(600)
	'FizzBuzz'
	'''
	return (not(valor % 3) and 'Fizz' or '') + \
	( not(valor % 5) and 'Buzz' or '') \
 	 or valor


if __name__ == '__main__':
	print FizzBuzz(int(sys.argv[1]))