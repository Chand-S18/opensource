X,Y,Z=map(int, input().split())
sum=Y
c=0
while(sum+X<=Z):
    sum+=X
    c+=1
print(c)
