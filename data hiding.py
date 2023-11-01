class Main:
	def __init__(self):
		self.price=1000
	def  setPrice(self,p):
		self.price=p
	def sell(self):
		print("price{}".format(self.price))
ob=Main()
print(ob.sell())
ob.setPrice(10000)
print(ob.sell())
