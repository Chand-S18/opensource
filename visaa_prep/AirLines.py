X,N=map(int,input().split())
people=X*100
if N>people:
    rem=N-people
    if rem%100==0:
        planes=rem//100
    else:
        planes=(rem//100)+1
else:
    planes=0
print(planes)
