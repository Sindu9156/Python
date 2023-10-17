from datetime import datetime
s=datetime.today()
print("today is ",s)
print("this month is",s.strftime("%b"))
print("today is ",s.strftime("%A"))
print("this year is ",s.year)
print("this month is",s.month)
print("this date is",s.day)
