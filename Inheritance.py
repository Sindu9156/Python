class Main:
	def __init__(self,name):
		self.name=name
	def print(self):
		print(self.name)
class A(Main):
	def __init__(self,name):
		super().__init__(name)
	def print(self):
		super().print()
	
ob=Main("Main")
ob.print()
ob2=A("A")
ob2.print()
