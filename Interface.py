class AdvancedArithmetic(object):
	def divisorSum(n):
		raise NotImplementedError
class Calculator(AdvancedArithmetic):
	def divisorSum(self, n):
		sum=0
		for i in range(1,n+1):
			if n%i==0:
				sum=sum+i
		return sum
n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("the sum of duvisors of ",n," is ",s)
