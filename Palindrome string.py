import sys
class Solution:
	d=[]
	f=[]
	def pushCharacter(self,a):
		self.d.append(a)
	def enqueueCharacter(self,a):
		self.f.append(a)
	def popCharacter(self):
		return self.d.pop()
	def dequeueCharacter(self):
		return self.f.pop(0)
s=input()
obj=Solution()   
l=len(s)
for i in range(l):
	obj.pushCharacter(s[i])
	obj.enqueueCharacter(s[i])

isPalindrome=True
for i in range(l // 2):
	if obj.popCharacter()!=obj.dequeueCharacter():
		isPalindrome=False
		break
if isPalindrome:
	print("The word, "+s+", is a palindrome.")
else:
	print("The word, "+s+", is not a palindrome.")    

