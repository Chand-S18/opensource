N=input()
N1=""
count=1
for i in range(1,len(N)):
    if N[i]==N[i-1]:
        count+=1
    else:
        N1+=N[i-1]+str(count)
        count=1
N1+=N[-1]+str(count)
print(N1)
