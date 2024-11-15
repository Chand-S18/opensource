N=int(input())
X=1
for i in range(1,N+1):
    for j in range(1,i+1):
        print(X,end=" ")
        X+=1
    print("")
