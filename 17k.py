k1,k2=map(int,input().split())
for i in range(1,100000):
   if(i%k1==0 and i%k2==0):
      print(i)
      break
