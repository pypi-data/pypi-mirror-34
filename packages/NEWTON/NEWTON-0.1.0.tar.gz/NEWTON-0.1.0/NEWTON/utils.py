from Fun1 import plus, mult
from Fun2 import minus, divide

def adder(n1, n2):
	ans = plus.add(n1, n2)
	print '+ ', ans, '\n'
	

def subtracter(n1, n2):
	ans = minus.subt(n1, n2)
	print '- ', ans, '\n'
	
	
def product(n1, n2):
	ans = mult.prod(n1, n2)
	print '* ', ans, '\n'
		
	
def division(n1, n2):
	ans = divide.div(n1, n2)
	print '/ ', ans, '\n'
		
