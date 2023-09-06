a=input("enter the string")
c=a
b=['a','e','i','o','u']

for i in range(0,5):
	a=a.replace(a[i],'')
	
print("the string ",c,"after removed vowel letters ",a)
	
