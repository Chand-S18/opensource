n=int(input())
arr=list(map(int,input().split()))
t=[]
for i in range(n):
    l_weight=sum(arr[:i])
    r_weight=sum(arr[i+1:])
    diff=abs(l_weight-r_weight)
    t.append(diff)
print(*t)
