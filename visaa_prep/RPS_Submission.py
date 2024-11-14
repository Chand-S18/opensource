vig,cha=input().split()
if vig==cha:
    print("NULL")
elif (vig=='P' and cha=='R') or (vig=='R' and cha=='S') or (vig=='S' and cha=='P'):
    print("Vignesh")
else:
    print("Charan")
