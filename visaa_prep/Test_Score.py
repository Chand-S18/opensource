N,X,Y=map(int,input().split())
if (N*X)>=Y>=0 and Y%X==0:
    print("YES")
else:
    print("NO")
