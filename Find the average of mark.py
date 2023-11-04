class A:
	marks=[]
	def __init__(self,name,marks):
		self.name=name
		for i in range(0,len(marks)):
			self.marks.append(marks[i])
	def display(self):
		sum=0
		print(self.name)
		for i in range(0,len(self.marks)):
			sum=sum+self.marks[i]
	
		print("Average mark is",sum/len(self.marks))
m=[100,90,80]
ob=A("raju",m)
ob.display()
		
