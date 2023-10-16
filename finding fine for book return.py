D1,M1,Y1=[int(x) for x in input().split()]
D2,M2,Y2=[int(x) for x in input().split()]
print(D1,Y1,M1,D2,Y2,M2)
if Y1>Y2:
  print(10000)
elif M1>M2 and Y1==Y2:
  print(500*(M1-M2))
elif D1>D2 and Y1==Y2 and M1==M2:
  print(15*(D1-D2))
else:
  print("No fine")
