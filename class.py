class abc:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("Name:",self.name,"age:",self.age)
obj=abc("abc",18)
print(obj.age)
obj.display()
